from __future__ import annotations

import asyncio
from aiohttp import ClientSession

from typing import List, Tuple, Dict, Any, AsyncIterator

from airflow.providers.google.cloud.hooks.gcs import GCSAsyncHook
from airflow.triggers.base import BaseTrigger, TriggerEvent


class GCSAnyBlobsTrigger(BaseTrigger):
    """
    A trigger that fires if it finds at least one of requested files or folders present in the given bucket.

    :param bucket: the bucket in the google cloud storage where the objects are residing.
    :param objects_names: list of files or folders present in the bucket
    :param google_cloud_conn_id: reference to the Google Connection
    :param poke_interval: polling period in seconds to check for file/folder
    """

    def __init__(
        self,
        bucket: str,
        objects_names: List[str],
        poke_interval: float,
        google_cloud_conn_id: str,
        hook_params: Dict[str, Any],
    ):
        super().__init__()
        self.bucket = bucket
        self.objects_names = objects_names
        self.poke_interval = poke_interval
        self.google_cloud_conn_id: str = google_cloud_conn_id
        self.hook_params = hook_params

    def serialize(self) -> Tuple[str, Dict[str, Any]]:
        """Serializes GCSBlobsTrigger arguments and classpath."""
        return (
            "airflowkit.triggers.gcs_any_blobs_trigger.GCSAnyBlobsTrigger",
            {
                "bucket": self.bucket,
                "objects_names": self.objects_names,
                "poke_interval": self.poke_interval,
                "google_cloud_conn_id": self.google_cloud_conn_id,
                "hook_params": self.hook_params,
            },
        )

    async def run(self) -> AsyncIterator["TriggerEvent"]:
        """Simple loop until the relevant files/folders are found."""
        try:
            hook = self._get_async_hook()
            while True:
                res = await self._at_least_one_object_exist(
                    hook=hook, bucket_name=self.bucket, objects_names=self.objects_names
                )
                if res == "success":
                    yield TriggerEvent({"status": "success", "message": res})
                await asyncio.sleep(self.poke_interval)
        except Exception as e:
            yield TriggerEvent({"status": "error", "message": str(e)})
            return

    def _get_async_hook(self) -> GCSAsyncHook:
        return GCSAsyncHook(gcp_conn_id=self.google_cloud_conn_id, **self.hook_params)

    async def _at_least_one_object_exist(
        self, hook: GCSAsyncHook, bucket_name: str, objects_names: List[str]
    ) -> str:
        """
        Checks for the existence of at least one files/folders in Google Cloud Storage.

        :param bucket_name: The Google Cloud Storage bucket where the object is.
        :param objects_names: The names of the blobs to check in the Google cloud
            storage bucket.
        """
        async with ClientSession() as s:
            client = await hook.get_storage_client(s)
            bucket = client.get_bucket(bucket_name)
            responses = []
            for object_name in objects_names:
                object_response = await bucket.blob_exists(blob_name=object_name)
                if object_response:
                    self.log.debug(f"Found GCS blob {object_name}!")
                    responses.append(True)
                else:
                    self.log.debug(f"Not found GCS blob: {object_name}!")
                    responses.append(False)

            if any(responses) or len(objects_names) == 0:
                return "success"
            return "pending"
