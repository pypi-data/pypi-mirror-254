"""
Type annotations for healthlake service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_healthlake/type_defs/)

Usage::

    ```python
    from types_aiobotocore_healthlake.type_defs import IdentityProviderConfigurationTypeDef

    data: IdentityProviderConfigurationTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import AuthorizationStrategyType, CmkTypeType, DatastoreStatusType, JobStatusType

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "IdentityProviderConfigurationTypeDef",
    "PreloadDataConfigTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampTypeDef",
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    "DescribeFHIRExportJobRequestRequestTypeDef",
    "DescribeFHIRImportJobRequestRequestTypeDef",
    "InputDataConfigTypeDef",
    "KmsEncryptionConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "S3ConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobResponseTypeDef",
    "DatastoreFilterTypeDef",
    "ListFHIRExportJobsRequestRequestTypeDef",
    "ListFHIRImportJobsRequestRequestTypeDef",
    "SseConfigurationTypeDef",
    "OutputDataConfigTypeDef",
    "ListFHIRDatastoresRequestRequestTypeDef",
    "CreateFHIRDatastoreRequestRequestTypeDef",
    "DatastorePropertiesTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "StartFHIRExportJobRequestRequestTypeDef",
    "StartFHIRImportJobRequestRequestTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "ListFHIRExportJobsResponseTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ListFHIRImportJobsResponseTypeDef",
)

IdentityProviderConfigurationTypeDef = TypedDict(
    "IdentityProviderConfigurationTypeDef",
    {
        "AuthorizationStrategy": AuthorizationStrategyType,
        "FineGrainedAuthorizationEnabled": NotRequired[bool],
        "Metadata": NotRequired[str],
        "IdpLambdaArn": NotRequired[str],
    },
)
PreloadDataConfigTypeDef = TypedDict(
    "PreloadDataConfigTypeDef",
    {
        "PreloadDataType": Literal["SYNTHEA"],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
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
TimestampTypeDef = Union[datetime, str]
DeleteFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)
DescribeFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)
DescribeFHIRExportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRExportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)
DescribeFHIRImportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRImportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)
InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": NotRequired[str],
    },
)
KmsEncryptionConfigTypeDef = TypedDict(
    "KmsEncryptionConfigTypeDef",
    {
        "CmkType": CmkTypeType,
        "KmsKeyId": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateFHIRDatastoreResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFHIRDatastoreResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFHIRExportJobResponseTypeDef = TypedDict(
    "StartFHIRExportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFHIRImportJobResponseTypeDef = TypedDict(
    "StartFHIRImportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DatastoreFilterTypeDef = TypedDict(
    "DatastoreFilterTypeDef",
    {
        "DatastoreName": NotRequired[str],
        "DatastoreStatus": NotRequired[DatastoreStatusType],
        "CreatedBefore": NotRequired[TimestampTypeDef],
        "CreatedAfter": NotRequired[TimestampTypeDef],
    },
)
ListFHIRExportJobsRequestRequestTypeDef = TypedDict(
    "ListFHIRExportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmittedBefore": NotRequired[TimestampTypeDef],
        "SubmittedAfter": NotRequired[TimestampTypeDef],
    },
)
ListFHIRImportJobsRequestRequestTypeDef = TypedDict(
    "ListFHIRImportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmittedBefore": NotRequired[TimestampTypeDef],
        "SubmittedAfter": NotRequired[TimestampTypeDef],
    },
)
SseConfigurationTypeDef = TypedDict(
    "SseConfigurationTypeDef",
    {
        "KmsEncryptionConfig": KmsEncryptionConfigTypeDef,
    },
)
OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Configuration": NotRequired[S3ConfigurationTypeDef],
    },
)
ListFHIRDatastoresRequestRequestTypeDef = TypedDict(
    "ListFHIRDatastoresRequestRequestTypeDef",
    {
        "Filter": NotRequired[DatastoreFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
CreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "CreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreName": NotRequired[str],
        "SseConfiguration": NotRequired[SseConfigurationTypeDef],
        "PreloadDataConfig": NotRequired[PreloadDataConfigTypeDef],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "IdentityProviderConfiguration": NotRequired[IdentityProviderConfigurationTypeDef],
    },
)
DatastorePropertiesTypeDef = TypedDict(
    "DatastorePropertiesTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreEndpoint": str,
        "DatastoreName": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "SseConfiguration": NotRequired[SseConfigurationTypeDef],
        "PreloadDataConfig": NotRequired[PreloadDataConfigTypeDef],
        "IdentityProviderConfiguration": NotRequired[IdentityProviderConfigurationTypeDef],
    },
)
ExportJobPropertiesTypeDef = TypedDict(
    "ExportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "JobName": NotRequired[str],
        "EndTime": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ImportJobPropertiesTypeDef = TypedDict(
    "ImportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "InputDataConfig": InputDataConfigTypeDef,
        "JobName": NotRequired[str],
        "EndTime": NotRequired[datetime],
        "JobOutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "Message": NotRequired[str],
    },
)
StartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "StartFHIRExportJobRequestRequestTypeDef",
    {
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
        "JobName": NotRequired[str],
    },
)
StartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "StartFHIRImportJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "JobOutputDataConfig": OutputDataConfigTypeDef,
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
        "JobName": NotRequired[str],
    },
)
DescribeFHIRDatastoreResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseTypeDef",
    {
        "DatastoreProperties": DatastorePropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFHIRDatastoresResponseTypeDef = TypedDict(
    "ListFHIRDatastoresResponseTypeDef",
    {
        "DatastorePropertiesList": List[DatastorePropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFHIRExportJobResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseTypeDef",
    {
        "ExportJobProperties": ExportJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFHIRExportJobsResponseTypeDef = TypedDict(
    "ListFHIRExportJobsResponseTypeDef",
    {
        "ExportJobPropertiesList": List[ExportJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFHIRImportJobResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseTypeDef",
    {
        "ImportJobProperties": ImportJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFHIRImportJobsResponseTypeDef = TypedDict(
    "ListFHIRImportJobsResponseTypeDef",
    {
        "ImportJobPropertiesList": List[ImportJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
