"""
Type annotations for medical-imaging service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_medical_imaging.client import HealthImagingClient
    from types_aiobotocore_medical_imaging.paginator import (
        ListDICOMImportJobsPaginator,
        ListDatastoresPaginator,
        ListImageSetVersionsPaginator,
        SearchImageSetsPaginator,
    )

    session = get_session()
    with session.create_client("medical-imaging") as client:
        client: HealthImagingClient

        list_dicom_import_jobs_paginator: ListDICOMImportJobsPaginator = client.get_paginator("list_dicom_import_jobs")
        list_datastores_paginator: ListDatastoresPaginator = client.get_paginator("list_datastores")
        list_image_set_versions_paginator: ListImageSetVersionsPaginator = client.get_paginator("list_image_set_versions")
        search_image_sets_paginator: SearchImageSetsPaginator = client.get_paginator("search_image_sets")
    ```
"""

from typing import AsyncIterator, Generic, Iterator, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import DatastoreStatusType, JobStatusType
from .type_defs import (
    ListDatastoresResponseTypeDef,
    ListDICOMImportJobsResponseTypeDef,
    ListImageSetVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchCriteriaTypeDef,
    SearchImageSetsResponseTypeDef,
)

__all__ = (
    "ListDICOMImportJobsPaginator",
    "ListDatastoresPaginator",
    "ListImageSetVersionsPaginator",
    "SearchImageSetsPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class ListDICOMImportJobsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDICOMImportJobs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#listdicomimportjobspaginator)
    """

    def paginate(
        self,
        *,
        datastoreId: str,
        jobStatus: JobStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDICOMImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDICOMImportJobs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#listdicomimportjobspaginator)
        """

class ListDatastoresPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDatastores)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#listdatastorespaginator)
    """

    def paginate(
        self,
        *,
        datastoreStatus: DatastoreStatusType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDatastoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.ListDatastores.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#listdatastorespaginator)
        """

class ListImageSetVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.ListImageSetVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#listimagesetversionspaginator)
    """

    def paginate(
        self, *, datastoreId: str, imageSetId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListImageSetVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.ListImageSetVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#listimagesetversionspaginator)
        """

class SearchImageSetsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.SearchImageSets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#searchimagesetspaginator)
    """

    def paginate(
        self,
        *,
        datastoreId: str,
        searchCriteria: SearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchImageSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/medical-imaging.html#HealthImaging.Paginator.SearchImageSets.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/paginators/#searchimagesetspaginator)
        """
