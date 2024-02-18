from __future__ import annotations

import warnings

from typing import List, TYPE_CHECKING, Sequence
from datetime import timedelta

from google.api_core.retry import Retry
from google.cloud.storage.retry import DEFAULT_RETRY

from airflow.exceptions import AirflowException
from airflow.sensors.base import BaseSensorOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook

from airflowkit.triggers.gcs_blobs_trigger import GCSBlobsTrigger

if TYPE_CHECKING:
    from airflow.utils.context import Context


class GCSObjectsExistenceAsyncSensor(BaseSensorOperator):
    """
    Checks for the existence of files in Google Cloud Storage.

    :param bucket: The Google Cloud Storage bucket where the object is.
    :param objects: The names of the objects to check in the Google cloud
        storage bucket.
    :param google_cloud_conn_id: The connection ID to use when
        connecting to Google Cloud Storage.
    :param delegate_to: The account to impersonate using domain-wide delegation of authority,
        if any. For this to work, the service account making the request must have
        domain-wide delegation enabled.
    :param impersonation_chain: Optional service account to impersonate using short-term
        credentials, or chained list of accounts required to get the access_token
        of the last account in the list, which will be impersonated in the request.
        If set as a string, the account must grant the originating account
        the Service Account Token Creator IAM role.
        If set as a sequence, the identities from the list must grant
        Service Account Token Creator IAM role to the directly preceding identity, with first
        account from the list granting this role to the originating account (templated).
    :param retry: (Optional) How to retry the RPC
    """

    template_fields: Sequence[str] = (
        "bucket",
        "objects",
        "impersonation_chain",
    )
    ui_color = "#f0eee4"

    def __init__(
        self,
        *,
        bucket: str,
        objects: List[str],
        google_cloud_conn_id: str = "google_cloud_default",
        delegate_to: str | None = None,
        impersonation_chain: str | Sequence[str] | None = None,
        retry: Retry = DEFAULT_RETRY,
        **kwargs,
    ) -> None:

        super().__init__(**kwargs)
        self.bucket = bucket
        self.objects = objects
        self.google_cloud_conn_id = google_cloud_conn_id
        if delegate_to:
            warnings.warn(
                "'delegate_to' parameter is deprecated, please use 'impersonation_chain'",
                DeprecationWarning,
            )
        self.delegate_to = delegate_to
        self.impersonation_chain = impersonation_chain
        self.retry = retry

    def poke(self, context: Context) -> bool:
        self.log.info("Sensor checks existence of : %s, %s", self.bucket, self.objects)
        hook = GCSHook(
            gcp_conn_id=self.google_cloud_conn_id,
            delegate_to=self.delegate_to,
            impersonation_chain=self.impersonation_chain,
        )
        responses = []
        for object in self.objects:
            responses.append(hook.exists(self.bucket, object, self.retry))
        return all(responses)

    def execute(self, context: Context) -> None:
        """Airflow runs this method on the worker and defers using the trigger."""
        self.defer(
            timeout=timedelta(seconds=self.timeout),
            trigger=GCSBlobsTrigger(
                bucket=self.bucket,
                objects_names=self.objects,
                poke_interval=self.poke_interval,
                google_cloud_conn_id=self.google_cloud_conn_id,
                hook_params={
                    "delegate_to": self.delegate_to,
                    "impersonation_chain": self.impersonation_chain,
                },
            ),
            method_name="execute_complete",
        )

    def execute_complete(self, context: Context, event: dict[str, str]) -> str:
        """
        Callback for when the trigger fires - returns immediately.
        Relies on trigger to throw an exception, otherwise it assumes execution was
        successful.
        """
        if event["status"] == "error":
            raise AirflowException(event["message"])
        self.log.info(
            "%d files %s were found in bucket %s.",
            len(self.objects),
            self.objects,
            self.bucket,
        )
        return event["message"]
