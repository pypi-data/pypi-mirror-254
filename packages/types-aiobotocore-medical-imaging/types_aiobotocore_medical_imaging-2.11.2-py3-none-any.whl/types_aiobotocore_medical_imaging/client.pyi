"""
Type annotations for medical-imaging service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_medical_imaging.client import HealthImagingClient

    session = get_session()
    async with session.create_client("medical-imaging") as client:
        client: HealthImagingClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import DatastoreStatusType, JobStatusType
from .paginator import (
    ListDatastoresPaginator,
    ListDICOMImportJobsPaginator,
    ListImageSetVersionsPaginator,
    SearchImageSetsPaginator,
)
from .type_defs import (
    CopyImageSetInformationTypeDef,
    CopyImageSetResponseTypeDef,
    CreateDatastoreResponseTypeDef,
    DeleteDatastoreResponseTypeDef,
    DeleteImageSetResponseTypeDef,
    GetDatastoreResponseTypeDef,
    GetDICOMImportJobResponseTypeDef,
    GetImageFrameResponseTypeDef,
    GetImageSetMetadataResponseTypeDef,
    GetImageSetResponseTypeDef,
    ImageFrameInformationTypeDef,
    ListDatastoresResponseTypeDef,
    ListDICOMImportJobsResponseTypeDef,
    ListImageSetVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetadataUpdatesTypeDef,
    SearchCriteriaTypeDef,
    SearchImageSetsResponseTypeDef,
    StartDICOMImportJobResponseTypeDef,
    UpdateImageSetMetadataResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("HealthImagingClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class HealthImagingClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        HealthImagingClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#close)
        """

    async def copy_image_set(
        self,
        *,
        datastoreId: str,
        sourceImageSetId: str,
        copyImageSetInformation: CopyImageSetInformationTypeDef,
    ) -> CopyImageSetResponseTypeDef:
        """
        Copy an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.copy_image_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#copy_image_set)
        """

    async def create_datastore(
        self,
        *,
        clientToken: str,
        datastoreName: str = ...,
        tags: Mapping[str, str] = ...,
        kmsKeyArn: str = ...,
    ) -> CreateDatastoreResponseTypeDef:
        """
        Create a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.create_datastore)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#create_datastore)
        """

    async def delete_datastore(self, *, datastoreId: str) -> DeleteDatastoreResponseTypeDef:
        """
        Delete a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.delete_datastore)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#delete_datastore)
        """

    async def delete_image_set(
        self, *, datastoreId: str, imageSetId: str
    ) -> DeleteImageSetResponseTypeDef:
        """
        Delete an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.delete_image_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#delete_image_set)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#generate_presigned_url)
        """

    async def get_datastore(self, *, datastoreId: str) -> GetDatastoreResponseTypeDef:
        """
        Get data store properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_datastore)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_datastore)
        """

    async def get_dicom_import_job(
        self, *, datastoreId: str, jobId: str
    ) -> GetDICOMImportJobResponseTypeDef:
        """
        Get the import job properties to learn more about the job or job progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_dicom_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_dicom_import_job)
        """

    async def get_image_frame(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        imageFrameInformation: ImageFrameInformationTypeDef,
    ) -> GetImageFrameResponseTypeDef:
        """
        Get an image frame (pixel data) for an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_image_frame)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_image_frame)
        """

    async def get_image_set(
        self, *, datastoreId: str, imageSetId: str, versionId: str = ...
    ) -> GetImageSetResponseTypeDef:
        """
        Get image set properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_image_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_image_set)
        """

    async def get_image_set_metadata(
        self, *, datastoreId: str, imageSetId: str, versionId: str = ...
    ) -> GetImageSetMetadataResponseTypeDef:
        """
        Get metadata attributes for an image set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_image_set_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_image_set_metadata)
        """

    async def list_datastores(
        self,
        *,
        datastoreStatus: DatastoreStatusType = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListDatastoresResponseTypeDef:
        """
        List data stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.list_datastores)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#list_datastores)
        """

    async def list_dicom_import_jobs(
        self,
        *,
        datastoreId: str,
        jobStatus: JobStatusType = ...,
        nextToken: str = ...,
        maxResults: int = ...,
    ) -> ListDICOMImportJobsResponseTypeDef:
        """
        List import jobs created for a specific data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.list_dicom_import_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#list_dicom_import_jobs)
        """

    async def list_image_set_versions(
        self, *, datastoreId: str, imageSetId: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListImageSetVersionsResponseTypeDef:
        """
        List image set versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.list_image_set_versions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#list_image_set_versions)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#list_tags_for_resource)
        """

    async def search_image_sets(
        self,
        *,
        datastoreId: str,
        searchCriteria: SearchCriteriaTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
    ) -> SearchImageSetsResponseTypeDef:
        """
        Search image sets based on defined input attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.search_image_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#search_image_sets)
        """

    async def start_dicom_import_job(
        self,
        *,
        dataAccessRoleArn: str,
        clientToken: str,
        datastoreId: str,
        inputS3Uri: str,
        outputS3Uri: str,
        jobName: str = ...,
    ) -> StartDICOMImportJobResponseTypeDef:
        """
        Start importing bulk data into an `ACTIVE` data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.start_dicom_import_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#start_dicom_import_job)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Adds a user-specifed key and value tag to a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from a medical imaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#untag_resource)
        """

    async def update_image_set_metadata(
        self,
        *,
        datastoreId: str,
        imageSetId: str,
        latestVersionId: str,
        updateImageSetMetadataUpdates: MetadataUpdatesTypeDef,
    ) -> UpdateImageSetMetadataResponseTypeDef:
        """
        Update image set metadata attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.update_image_set_metadata)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#update_image_set_metadata)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dicom_import_jobs"]
    ) -> ListDICOMImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datastores"]) -> ListDatastoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_set_versions"]
    ) -> ListImageSetVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_image_sets"]
    ) -> SearchImageSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/#get_paginator)
        """

    async def __aenter__(self) -> "HealthImagingClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/client/)
        """
