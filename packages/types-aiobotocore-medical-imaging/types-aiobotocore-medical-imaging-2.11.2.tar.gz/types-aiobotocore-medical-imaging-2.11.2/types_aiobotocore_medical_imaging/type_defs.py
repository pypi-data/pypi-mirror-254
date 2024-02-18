"""
Type annotations for medical-imaging service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_medical_imaging/type_defs/)

Usage::

    ```python
    from types_aiobotocore_medical_imaging.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    DatastoreStatusType,
    ImageSetStateType,
    ImageSetWorkflowStatusType,
    JobStatusType,
    OperatorType,
)

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BlobTypeDef",
    "CopyDestinationImageSetPropertiesTypeDef",
    "CopyDestinationImageSetTypeDef",
    "CopySourceImageSetInformationTypeDef",
    "CopySourceImageSetPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "CreateDatastoreRequestRequestTypeDef",
    "DICOMImportJobPropertiesTypeDef",
    "DICOMImportJobSummaryTypeDef",
    "DICOMStudyDateAndTimeTypeDef",
    "DICOMTagsTypeDef",
    "DatastorePropertiesTypeDef",
    "DatastoreSummaryTypeDef",
    "DeleteDatastoreRequestRequestTypeDef",
    "DeleteImageSetRequestRequestTypeDef",
    "GetDICOMImportJobRequestRequestTypeDef",
    "GetDatastoreRequestRequestTypeDef",
    "ImageFrameInformationTypeDef",
    "GetImageSetMetadataRequestRequestTypeDef",
    "GetImageSetRequestRequestTypeDef",
    "ImageSetPropertiesTypeDef",
    "PaginatorConfigTypeDef",
    "ListDICOMImportJobsRequestRequestTypeDef",
    "ListDatastoresRequestRequestTypeDef",
    "ListImageSetVersionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TimestampTypeDef",
    "StartDICOMImportJobRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "DICOMUpdatesTypeDef",
    "CopyImageSetInformationTypeDef",
    "CopyImageSetResponseTypeDef",
    "CreateDatastoreResponseTypeDef",
    "DeleteDatastoreResponseTypeDef",
    "DeleteImageSetResponseTypeDef",
    "GetImageFrameResponseTypeDef",
    "GetImageSetMetadataResponseTypeDef",
    "GetImageSetResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartDICOMImportJobResponseTypeDef",
    "UpdateImageSetMetadataResponseTypeDef",
    "GetDICOMImportJobResponseTypeDef",
    "ListDICOMImportJobsResponseTypeDef",
    "ImageSetsMetadataSummaryTypeDef",
    "GetDatastoreResponseTypeDef",
    "ListDatastoresResponseTypeDef",
    "GetImageFrameRequestRequestTypeDef",
    "ListImageSetVersionsResponseTypeDef",
    "ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    "ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    "SearchByAttributeValueTypeDef",
    "MetadataUpdatesTypeDef",
    "CopyImageSetRequestRequestTypeDef",
    "SearchImageSetsResponseTypeDef",
    "SearchFilterTypeDef",
    "UpdateImageSetMetadataRequestRequestTypeDef",
    "SearchCriteriaTypeDef",
    "SearchImageSetsRequestRequestTypeDef",
    "SearchImageSetsRequestSearchImageSetsPaginateTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CopyDestinationImageSetPropertiesTypeDef = TypedDict(
    "CopyDestinationImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": NotRequired[ImageSetStateType],
        "imageSetWorkflowStatus": NotRequired[ImageSetWorkflowStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "imageSetArn": NotRequired[str],
    },
)
CopyDestinationImageSetTypeDef = TypedDict(
    "CopyDestinationImageSetTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
    },
)
CopySourceImageSetInformationTypeDef = TypedDict(
    "CopySourceImageSetInformationTypeDef",
    {
        "latestVersionId": str,
    },
)
CopySourceImageSetPropertiesTypeDef = TypedDict(
    "CopySourceImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": NotRequired[ImageSetStateType],
        "imageSetWorkflowStatus": NotRequired[ImageSetWorkflowStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "imageSetArn": NotRequired[str],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
CreateDatastoreRequestRequestTypeDef = TypedDict(
    "CreateDatastoreRequestRequestTypeDef",
    {
        "clientToken": str,
        "datastoreName": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "kmsKeyArn": NotRequired[str],
    },
)
DICOMImportJobPropertiesTypeDef = TypedDict(
    "DICOMImportJobPropertiesTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "datastoreId": str,
        "dataAccessRoleArn": str,
        "inputS3Uri": str,
        "outputS3Uri": str,
        "endedAt": NotRequired[datetime],
        "submittedAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
DICOMImportJobSummaryTypeDef = TypedDict(
    "DICOMImportJobSummaryTypeDef",
    {
        "jobId": str,
        "jobName": str,
        "jobStatus": JobStatusType,
        "datastoreId": str,
        "dataAccessRoleArn": NotRequired[str],
        "endedAt": NotRequired[datetime],
        "submittedAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
DICOMStudyDateAndTimeTypeDef = TypedDict(
    "DICOMStudyDateAndTimeTypeDef",
    {
        "DICOMStudyDate": str,
        "DICOMStudyTime": NotRequired[str],
    },
)
DICOMTagsTypeDef = TypedDict(
    "DICOMTagsTypeDef",
    {
        "DICOMPatientId": NotRequired[str],
        "DICOMPatientName": NotRequired[str],
        "DICOMPatientBirthDate": NotRequired[str],
        "DICOMPatientSex": NotRequired[str],
        "DICOMStudyInstanceUID": NotRequired[str],
        "DICOMStudyId": NotRequired[str],
        "DICOMStudyDescription": NotRequired[str],
        "DICOMNumberOfStudyRelatedSeries": NotRequired[int],
        "DICOMNumberOfStudyRelatedInstances": NotRequired[int],
        "DICOMAccessionNumber": NotRequired[str],
        "DICOMStudyDate": NotRequired[str],
        "DICOMStudyTime": NotRequired[str],
    },
)
DatastorePropertiesTypeDef = TypedDict(
    "DatastorePropertiesTypeDef",
    {
        "datastoreId": str,
        "datastoreName": str,
        "datastoreStatus": DatastoreStatusType,
        "kmsKeyArn": NotRequired[str],
        "datastoreArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
DatastoreSummaryTypeDef = TypedDict(
    "DatastoreSummaryTypeDef",
    {
        "datastoreId": str,
        "datastoreName": str,
        "datastoreStatus": DatastoreStatusType,
        "datastoreArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)
DeleteDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteDatastoreRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)
DeleteImageSetRequestRequestTypeDef = TypedDict(
    "DeleteImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
    },
)
GetDICOMImportJobRequestRequestTypeDef = TypedDict(
    "GetDICOMImportJobRequestRequestTypeDef",
    {
        "datastoreId": str,
        "jobId": str,
    },
)
GetDatastoreRequestRequestTypeDef = TypedDict(
    "GetDatastoreRequestRequestTypeDef",
    {
        "datastoreId": str,
    },
)
ImageFrameInformationTypeDef = TypedDict(
    "ImageFrameInformationTypeDef",
    {
        "imageFrameId": str,
    },
)
GetImageSetMetadataRequestRequestTypeDef = TypedDict(
    "GetImageSetMetadataRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": NotRequired[str],
    },
)
GetImageSetRequestRequestTypeDef = TypedDict(
    "GetImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": NotRequired[str],
    },
)
ImageSetPropertiesTypeDef = TypedDict(
    "ImageSetPropertiesTypeDef",
    {
        "imageSetId": str,
        "versionId": str,
        "imageSetState": ImageSetStateType,
        "ImageSetWorkflowStatus": NotRequired[ImageSetWorkflowStatusType],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "deletedAt": NotRequired[datetime],
        "message": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListDICOMImportJobsRequestRequestTypeDef = TypedDict(
    "ListDICOMImportJobsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "jobStatus": NotRequired[JobStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDatastoresRequestRequestTypeDef = TypedDict(
    "ListDatastoresRequestRequestTypeDef",
    {
        "datastoreStatus": NotRequired[DatastoreStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListImageSetVersionsRequestRequestTypeDef = TypedDict(
    "ListImageSetVersionsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
TimestampTypeDef = Union[datetime, str]
StartDICOMImportJobRequestRequestTypeDef = TypedDict(
    "StartDICOMImportJobRequestRequestTypeDef",
    {
        "dataAccessRoleArn": str,
        "clientToken": str,
        "datastoreId": str,
        "inputS3Uri": str,
        "outputS3Uri": str,
        "jobName": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
DICOMUpdatesTypeDef = TypedDict(
    "DICOMUpdatesTypeDef",
    {
        "removableAttributes": NotRequired[BlobTypeDef],
        "updatableAttributes": NotRequired[BlobTypeDef],
    },
)
CopyImageSetInformationTypeDef = TypedDict(
    "CopyImageSetInformationTypeDef",
    {
        "sourceImageSet": CopySourceImageSetInformationTypeDef,
        "destinationImageSet": NotRequired[CopyDestinationImageSetTypeDef],
    },
)
CopyImageSetResponseTypeDef = TypedDict(
    "CopyImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "sourceImageSetProperties": CopySourceImageSetPropertiesTypeDef,
        "destinationImageSetProperties": CopyDestinationImageSetPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatastoreResponseTypeDef = TypedDict(
    "CreateDatastoreResponseTypeDef",
    {
        "datastoreId": str,
        "datastoreStatus": DatastoreStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDatastoreResponseTypeDef = TypedDict(
    "DeleteDatastoreResponseTypeDef",
    {
        "datastoreId": str,
        "datastoreStatus": DatastoreStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteImageSetResponseTypeDef = TypedDict(
    "DeleteImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageFrameResponseTypeDef = TypedDict(
    "GetImageFrameResponseTypeDef",
    {
        "imageFrameBlob": StreamingBody,
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageSetMetadataResponseTypeDef = TypedDict(
    "GetImageSetMetadataResponseTypeDef",
    {
        "imageSetMetadataBlob": StreamingBody,
        "contentType": str,
        "contentEncoding": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageSetResponseTypeDef = TypedDict(
    "GetImageSetResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "versionId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "deletedAt": datetime,
        "message": str,
        "imageSetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDICOMImportJobResponseTypeDef = TypedDict(
    "StartDICOMImportJobResponseTypeDef",
    {
        "datastoreId": str,
        "jobId": str,
        "jobStatus": JobStatusType,
        "submittedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateImageSetMetadataResponseTypeDef = TypedDict(
    "UpdateImageSetMetadataResponseTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "latestVersionId": str,
        "imageSetState": ImageSetStateType,
        "imageSetWorkflowStatus": ImageSetWorkflowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDICOMImportJobResponseTypeDef = TypedDict(
    "GetDICOMImportJobResponseTypeDef",
    {
        "jobProperties": DICOMImportJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDICOMImportJobsResponseTypeDef = TypedDict(
    "ListDICOMImportJobsResponseTypeDef",
    {
        "jobSummaries": List[DICOMImportJobSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImageSetsMetadataSummaryTypeDef = TypedDict(
    "ImageSetsMetadataSummaryTypeDef",
    {
        "imageSetId": str,
        "version": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "DICOMTags": NotRequired[DICOMTagsTypeDef],
    },
)
GetDatastoreResponseTypeDef = TypedDict(
    "GetDatastoreResponseTypeDef",
    {
        "datastoreProperties": DatastorePropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatastoresResponseTypeDef = TypedDict(
    "ListDatastoresResponseTypeDef",
    {
        "datastoreSummaries": List[DatastoreSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImageFrameRequestRequestTypeDef = TypedDict(
    "GetImageFrameRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "imageFrameInformation": ImageFrameInformationTypeDef,
    },
)
ListImageSetVersionsResponseTypeDef = TypedDict(
    "ListImageSetVersionsResponseTypeDef",
    {
        "imageSetPropertiesList": List[ImageSetPropertiesTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef = TypedDict(
    "ListDICOMImportJobsRequestListDICOMImportJobsPaginateTypeDef",
    {
        "datastoreId": str,
        "jobStatus": NotRequired[JobStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDatastoresRequestListDatastoresPaginateTypeDef = TypedDict(
    "ListDatastoresRequestListDatastoresPaginateTypeDef",
    {
        "datastoreStatus": NotRequired[DatastoreStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef = TypedDict(
    "ListImageSetVersionsRequestListImageSetVersionsPaginateTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchByAttributeValueTypeDef = TypedDict(
    "SearchByAttributeValueTypeDef",
    {
        "DICOMPatientId": NotRequired[str],
        "DICOMAccessionNumber": NotRequired[str],
        "DICOMStudyId": NotRequired[str],
        "DICOMStudyInstanceUID": NotRequired[str],
        "createdAt": NotRequired[TimestampTypeDef],
        "DICOMStudyDateAndTime": NotRequired[DICOMStudyDateAndTimeTypeDef],
    },
)
MetadataUpdatesTypeDef = TypedDict(
    "MetadataUpdatesTypeDef",
    {
        "DICOMUpdates": NotRequired[DICOMUpdatesTypeDef],
    },
)
CopyImageSetRequestRequestTypeDef = TypedDict(
    "CopyImageSetRequestRequestTypeDef",
    {
        "datastoreId": str,
        "sourceImageSetId": str,
        "copyImageSetInformation": CopyImageSetInformationTypeDef,
    },
)
SearchImageSetsResponseTypeDef = TypedDict(
    "SearchImageSetsResponseTypeDef",
    {
        "imageSetsMetadataSummaries": List[ImageSetsMetadataSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "values": Sequence[SearchByAttributeValueTypeDef],
        "operator": OperatorType,
    },
)
UpdateImageSetMetadataRequestRequestTypeDef = TypedDict(
    "UpdateImageSetMetadataRequestRequestTypeDef",
    {
        "datastoreId": str,
        "imageSetId": str,
        "latestVersionId": str,
        "updateImageSetMetadataUpdates": MetadataUpdatesTypeDef,
    },
)
SearchCriteriaTypeDef = TypedDict(
    "SearchCriteriaTypeDef",
    {
        "filters": NotRequired[Sequence[SearchFilterTypeDef]],
    },
)
SearchImageSetsRequestRequestTypeDef = TypedDict(
    "SearchImageSetsRequestRequestTypeDef",
    {
        "datastoreId": str,
        "searchCriteria": NotRequired[SearchCriteriaTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
SearchImageSetsRequestSearchImageSetsPaginateTypeDef = TypedDict(
    "SearchImageSetsRequestSearchImageSetsPaginateTypeDef",
    {
        "datastoreId": str,
        "searchCriteria": NotRequired[SearchCriteriaTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
