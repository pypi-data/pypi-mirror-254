import io
import os
import base64
from pathlib import Path
from typing import TYPE_CHECKING, Iterator, Iterable
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

import requests

try:
    # TODO: better way to handle this?
    # doesn't seem like it should be a hard dependency
    from PIL import Image as PILImage
except ImportError:
    PILImage = None

from lqs.transcode import Transcode
from lqs.common.utils import (
    get_relative_object_path,
    decompress_chunk_bytes,
)
from lqs.common.exceptions import ConflictException
from lqs.interface.core.models import (
    Ingestion,
    Object,
    ObjectPart,
    Record,
    Topic,
)

if TYPE_CHECKING:
    from lqs.client import RESTClient


class Utils:
    def __init__(self, app: "RESTClient"):
        self.app = app

    # Uploading

    def upload_log_object(
        self,
        log_id: str,
        file_path: str,
        object_key: str = None,
        part_size: int = 100 * 1024 * 1024,
        max_workers: int | None = 8,
        overwrite: bool = False,
    ) -> tuple["Object", list["ObjectPart"]]:
        if object_key is None:
            object_key = file_path.split("/")[-1]

        object_size = os.path.getsize(file_path)

        try:
            log_object = self.app.create.log_object(
                log_id=log_id,
                key=object_key,
            ).data
        except ConflictException as e:
            if not overwrite:
                raise e
            self.app.delete.log_object(log_id=log_id, object_key=object_key)
            log_object = self.app.create.log_object(
                log_id=log_id,
                key=object_key,
            ).data

        number_of_parts = object_size // part_size + 1
        log_object_parts = []
        if max_workers is not None:
            futures = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                for idx in range(0, number_of_parts):
                    offset = idx * part_size
                    size = min(part_size, object_size - offset)
                    futures.append(
                        executor.submit(
                            self.upload_log_object_part,
                            log_id=log_id,
                            object_key=object_key,
                            part_number=idx + 1,
                            file_path=file_path,
                            offset=offset,
                            size=size,
                        )
                    )

                for future in futures:
                    log_object_parts.append(future.result())
        else:
            for idx in range(0, number_of_parts):
                offset = idx * part_size
                size = min(part_size, object_size - offset)
                log_object_parts.append(
                    self.upload_log_object_part(
                        log_id=log_id,
                        object_key=object_key,
                        part_number=idx + 1,
                        file_path=file_path,
                        offset=offset,
                        size=size,
                    )
                )

        log_object = self.app.update.log_object(
            log_id=log_id, object_key=object_key, data={"upload_state": "complete"}
        ).data

        return log_object, log_object_parts

    def upload_log_objects(
        self,
        log_id: str,
        file_dir: str,
        key_replacement: tuple[str, str] = None,
        key_prefix: str = None,
        part_size: int = 100 * 1024 * 1024,
        max_workers: int | None = 8,
        fail_if_empty: bool = True,
    ):
        upload_result_sets = []
        for file_path in Path(file_dir).rglob("*"):
            if os.path.isfile(file_path):
                object_key = str(file_path)
                if key_replacement is not None:
                    object_key = object_key.replace(*key_replacement)
                if key_prefix is not None:
                    object_key = os.path.join(key_prefix, object_key)
                if object_key.startswith("/"):
                    object_key = object_key[1:]
                upload_result = self.upload_log_object(
                    log_id=log_id,
                    file_path=file_path,
                    object_key=object_key,
                    part_size=part_size,
                    max_workers=max_workers,
                )
                upload_result_sets.append(upload_result)
        if fail_if_empty and len(upload_result_sets) == 0:
            raise Exception(f"No files found in {file_dir}")
        return upload_result_sets

    def upload_log_object_part(
        self, log_id, object_key, part_number, file_path, offset, size
    ):
        object_part = self.app.create.log_object_part(
            log_id=log_id,
            object_key=object_key,
            size=size,
            part_number=part_number,
        ).data
        upload_object_data_url = object_part.presigned_url

        with open(file_path, "rb") as f:
            f.seek(offset)
            data = f.read(size)
            response = requests.put(
                upload_object_data_url,
                data=data,
            )

        if response.status_code != 200:
            raise Exception(f"Error while uploading object part: {response.text}")

        return self.app.fetch.log_object_part(
            log_id=log_id,
            object_key=object_key,
            part_number=part_number,
        ).data

    def upload_log_object_part_data(self, log_id, object_key, size, part_number, data):
        object_part = self.app.create.log_object_part(
            log_id=log_id,
            object_key=object_key,
            size=size,
            part_number=part_number,
        ).data

        upload_object_data_url = object_part.presigned_url
        response = requests.put(
            upload_object_data_url,
            data=data,
        )

        if response.status_code != 200:
            raise Exception(f"Error while uploading object part: {response.text}")

        return self.app.fetch.log_object_part(
            log_id=log_id,
            object_key=object_key,
            part_number=part_number,
        ).data

    # Downloading

    def load_auxiliary_data_image(self, source: Record | dict):
        if isinstance(source, Record):
            auxiliary_data = source.get_auxiliary_data()
        else:
            auxiliary_data = source

        if auxiliary_data is None:
            return None
        if "image" not in auxiliary_data:
            return None
        if PILImage is None:
            raise Exception("PIL is not installed")
        encoded_webp_data = auxiliary_data["image"]
        decoded_webp_data = base64.b64decode(encoded_webp_data)
        image = PILImage.open(io.BytesIO(decoded_webp_data))
        return image

    def get_deserialized_record_data(
        self,
        record: Record,
        topic: Topic | None = None,
        ingestion: Ingestion | None = None,
        transcoder: Transcode | None = None,
    ) -> dict:
        if transcoder is None:
            transcoder = Transcode()

        if topic is None:
            topic = self.app.fetch.topic(record.topic_id).data

        message_bytes = self.fetch_record_bytes(record=record, ingestion=ingestion)

        return transcoder.deserialize(
            type_encoding=topic.type_encoding,
            type_name=topic.type_name,
            type_data=topic.type_data,
            message_bytes=message_bytes,
        )

    def fetch_record_bytes(
        self,
        record: Record,
        ingestion: Ingestion | None = None,
        decompress_chunk: bool = True,
        return_full_chunk: bool = False,
    ) -> bytes:

        if ingestion is None:
            ingestion = self.app.fetch.ingestion(record.ingestion_id).data

        object_store_id = (
            str(ingestion.object_store_id)
            if ingestion.object_store_id is not None
            else None
        )
        object_key = str(ingestion.object_key)

        if record.source is not None:
            # if the record has a source, we need to get the relative path from the object_key
            object_key = get_relative_object_path(
                object_key=object_key, source=record.source
            )

        if object_store_id is None:
            # the data is coming from a log object
            message_bytes: bytes = self.app.fetch.log_object(
                object_key=object_key,
                log_id=record.log_id,
                redirect=True,
                offset=record.data_offset,
                length=record.data_length,
            )
        else:
            # the data is coming from an object store
            message_bytes: bytes = self.app.fetch.object(
                object_key=object_key,
                object_store_id=object_store_id,
                redirect=True,
                offset=record.data_offset,
                length=record.data_length,
            )

        if record.chunk_compression is not None:
            if decompress_chunk:
                # if the record is compressed, we need to decompress it
                message_bytes = decompress_chunk_bytes(
                    chunk_bytes=message_bytes,
                    chunk_compression=record.chunk_compression,
                    chunk_length=record.chunk_length,
                )
                if not return_full_chunk:
                    # we only return the relevant part of the chunk
                    message_bytes = message_bytes[
                        record.chunk_offset : record.chunk_offset + record.chunk_length
                    ]
            else:
                if not return_full_chunk:
                    raise Exception(
                        "Cannot return partial chunk without decompressing it."
                    )

        return message_bytes

    def get_contiguous_record_offsets(
        self, records: Iterable[Record]
    ) -> tuple[int, int]:
        start_offset = None
        end_offset = None
        ingestion_id = None
        source = None
        for record in records:
            if ingestion_id is None:
                ingestion_id = record.ingestion_id
                if record.source is not None:
                    source = record.source

            if record.ingestion_id != ingestion_id:
                raise Exception(
                    "All records must have the same ingestion. Found {record.ingestion_id} and {ingestion.id}."
                )

            if record.source != source:
                raise Exception(
                    "All records must have the same source. Found {record.source} and {source}."
                )

            if start_offset is None:
                start_offset = record.data_offset

            if end_offset is None:
                end_offset = record.data_offset + record.data_length

            current_end_offset = record.data_offset + record.data_length
            if current_end_offset < end_offset:
                raise Exception(
                    "Records must be ordered by data offset. Found current end offset {current_end_offset} less than last end offset {end_offset}."
                )
            else:
                end_offset = current_end_offset

        return start_offset, end_offset

    def get_record_sets(
        self,
        records: Iterable[Record],
        density_threshold: float = 0.9,
        max_contiguous_size: int = 100 * 1000 * 1000,  # 100 MB
        max_contiguous_records: int = 1000,
    ) -> list[list[Record]]:
        record_sets: list[list[Record]] = []
        record_set: list[Record] = []
        relevant_length = 0
        full_length = 0
        start_offset = None
        last_ingestion_id = None
        last_source = None
        last_offset = None

        for record in records:
            if start_offset is None:
                start_offset = record.data_offset
            if last_ingestion_id is None:
                last_ingestion_id = record.ingestion_id
            if last_source is None:
                last_source = record.source
            if last_offset is None:
                last_offset = record.data_offset + record.data_length

            relevant_length += record.data_length
            full_length = record.data_offset + record.data_length - start_offset
            if (
                relevant_length / full_length > density_threshold
                and last_ingestion_id == record.ingestion_id
                and last_source == record.source
                and len(record_set) < max_contiguous_records
                and full_length < max_contiguous_size
                and record.data_offset + record.data_length >= last_offset
            ):
                record_set.append(record)
                last_offset = record.data_offset + record.data_length
            else:
                if len(record_set) == 0:
                    raise Exception("Record set cannot be empty.")
                record_sets.append(record_set)
                record_set = [record]
                relevant_length = record.data_length
                full_length = record.data_length
                start_offset = record.data_offset
                last_ingestion_id = record.ingestion_id
                last_source = record.source

        if len(record_set) > 0:
            record_sets.append(record_set)
        return record_sets

    def iter_dense_record_data(
        self,
        records: Iterable[Record],
        deserialize_results: bool = True,
        transcoder: Transcode | None = None,
        stream_data: bool = True,
        ingestions: dict[str, Ingestion] = {},
        topics: dict[str, Topic] = {},
    ) -> Iterator[tuple[Record, bytes | dict]]:
        if transcoder is None:
            transcoder = Transcode()

        object_key: str | None = None
        source: str | None = None

        start_offset = None
        end_offset = None
        for record in records:
            ingestion_id = str(record.ingestion_id)
            if ingestion_id not in ingestions:
                ingestions[ingestion_id] = self.app.fetch.ingestion(ingestion_id).data
            ingestion = ingestions[ingestion_id]

            if object_key is None:
                object_key = str(ingestion.object_key)
                if record.source is not None:
                    source = record.source
                    object_key = get_relative_object_path(
                        object_key=object_key, source=record.source
                    )

            if record.ingestion_id != ingestion.id:
                raise Exception(
                    "All records must have the same ingestion. Found {record.ingestion_id} and {ingestion.id}."
                )

            if record.source != source:
                raise Exception(
                    "All records must have the same source. Found {record.source} and {source}."
                )

            if start_offset is None:
                start_offset = record.data_offset

            if end_offset is None:
                end_offset = record.data_offset + record.data_length

            current_end_offset = record.data_offset + record.data_length
            if current_end_offset < end_offset:
                raise Exception(
                    "Records must be ordered by data offset. Found current end offset {current_end_offset} less than last end offset {end_offset}."
                )
            else:
                end_offset = current_end_offset

        # Now we fetch the object meta data and open a stream to the data
        if ingestion.object_store_id is None:
            # the data is coming from a log object
            object_meta: Object = self.app.fetch.log_object(
                object_key=object_key,
                log_id=ingestion.log_id,
                redirect=False,
                offset=start_offset,
                length=end_offset - start_offset,
            ).data
        else:
            # the data is coming from an object store
            object_meta: Object = self.app.fetch.object(
                object_key=object_key,
                object_store_id=ingestion.object_store_id,
                redirect=False,
                offset=start_offset,
                length=end_offset - start_offset,
            ).data

        presigned_url = object_meta.presigned_url
        headers = {
            "Range": f"bytes={start_offset}-{end_offset - 1}",
        }
        if stream_data:
            buffer_length = 1_000_000 * 32  # 32 MB
            r = requests.get(presigned_url, headers=headers, stream=True)
            r.raise_for_status()
            data_stream = io.BufferedReader(r.raw, buffer_length)
        else:
            r = requests.get(presigned_url, headers=headers, stream=False)
            r.raise_for_status()
            data_stream = io.BytesIO(r.content)

        # Now we can iterate over the records and read the data from the stream
        decompressed_bytes: bytes | None = None
        compressed_chunk_offset: int | None = None
        current_offset = start_offset
        for record in records:
            data_offset = record.data_offset
            data_length = record.data_length

            if (
                compressed_chunk_offset is not None
                and record.chunk_compression is not None
                and record.data_offset == compressed_chunk_offset
            ):
                message_bytes = decompressed_bytes[
                    record.chunk_offset : record.chunk_offset + record.chunk_length
                ]
            else:
                data_stream.read(data_offset - current_offset)
                message_bytes = data_stream.read(data_length)
                current_offset = data_offset + data_length

            if record.chunk_compression is not None:
                decompressed_bytes = decompress_chunk_bytes(
                    chunk_bytes=message_bytes,
                    chunk_compression=record.chunk_compression,
                    chunk_length=record.chunk_length,
                )
                message_bytes = decompressed_bytes[
                    record.chunk_offset : record.chunk_offset + record.chunk_length
                ]
                compressed_chunk_offset = record.data_offset

            if deserialize_results:
                # if we want to deserialize the results, we need the topic
                topic_id = str(record.topic_id)
                if topic_id not in topics:
                    # if we haven't seen this record's topic yet, we fetch it here
                    topics[topic_id] = self.app.fetch.topic(record.topic_id).data
                topic = topics[topic_id]
                record_data = transcoder.deserialize(
                    type_encoding=topic.type_encoding,
                    type_name=topic.type_name,
                    type_data=topic.type_data,
                    message_bytes=message_bytes,
                )
                yield (record, record_data)
            else:
                yield (record, message_bytes)

    def iter_record_data(
        self,
        records: Iterable[Record],
        deserialize_results: bool = True,
        transcoder: Transcode | None = None,
        density_threshold: float = 0.9,
        max_contiguous_size: int = 100 * 1000 * 1000,
        max_contiguous_records: int = 1000,
        max_workers: int | None = 10,
        return_as_completed: bool = False,
    ) -> Iterator[tuple[Record, bytes | dict]]:

        if transcoder is None:
            transcoder = Transcode()

        record_sets = self.get_record_sets(
            records=records,
            density_threshold=density_threshold,
            max_contiguous_size=max_contiguous_size,
            max_contiguous_records=max_contiguous_records,
        )

        def generate_data(
            records: Iterable[Record],
            deserialize_results: bool = True,
            transcoder: Transcode | None = None,
            ingestions: dict[str, Ingestion] = {},
            topics: dict[str, Topic] = {},
        ):
            results = [
                d
                for d in self.iter_dense_record_data(
                    records=records,
                    deserialize_results=deserialize_results,
                    transcoder=transcoder,
                    ingestions=ingestions,
                    topics=topics,
                )
            ]
            return results

        ingestions: dict[str, Ingestion] = {}
        topics: dict[str, Topic] = {}
        futures: list[Future[list[bytes | dict]]] = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for record_set in record_sets:
                future = executor.submit(
                    generate_data,
                    records=record_set,
                    deserialize_results=deserialize_results,
                    transcoder=transcoder,
                    ingestions=ingestions,
                    topics=topics,
                )
                futures.append(future)

            future_iterator = None
            if return_as_completed:
                future_iterator = as_completed(futures)
            else:
                future_iterator = futures

            for future in future_iterator:
                results = future.result()
                for result in results:
                    yield result
