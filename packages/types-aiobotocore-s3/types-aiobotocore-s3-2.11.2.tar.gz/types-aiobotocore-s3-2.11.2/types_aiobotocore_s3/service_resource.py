"""
Type annotations for s3 service ServiceResource

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_s3.service_resource import S3ServiceResource
    import types_aiobotocore_s3.service_resource as s3_resources

    session = get_session()
    async with session.resource("s3") as resource:
        resource: S3ServiceResource

        my_bucket: s3_resources.Bucket = resource.Bucket(...)
        my_bucket_acl: s3_resources.BucketAcl = resource.BucketAcl(...)
        my_bucket_cors: s3_resources.BucketCors = resource.BucketCors(...)
        my_bucket_lifecycle: s3_resources.BucketLifecycle = resource.BucketLifecycle(...)
        my_bucket_lifecycle_configuration: s3_resources.BucketLifecycleConfiguration = resource.BucketLifecycleConfiguration(...)
        my_bucket_logging: s3_resources.BucketLogging = resource.BucketLogging(...)
        my_bucket_notification: s3_resources.BucketNotification = resource.BucketNotification(...)
        my_bucket_policy: s3_resources.BucketPolicy = resource.BucketPolicy(...)
        my_bucket_request_payment: s3_resources.BucketRequestPayment = resource.BucketRequestPayment(...)
        my_bucket_tagging: s3_resources.BucketTagging = resource.BucketTagging(...)
        my_bucket_versioning: s3_resources.BucketVersioning = resource.BucketVersioning(...)
        my_bucket_website: s3_resources.BucketWebsite = resource.BucketWebsite(...)
        my_multipart_upload: s3_resources.MultipartUpload = resource.MultipartUpload(...)
        my_multipart_upload_part: s3_resources.MultipartUploadPart = resource.MultipartUploadPart(...)
        my_object: s3_resources.Object = resource.Object(...)
        my_object_acl: s3_resources.ObjectAcl = resource.ObjectAcl(...)
        my_object_summary: s3_resources.ObjectSummary = resource.ObjectSummary(...)
        my_object_version: s3_resources.ObjectVersion = resource.ObjectVersion(...)
```
"""

import sys
from datetime import datetime
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Dict,
    List,
    Mapping,
    NoReturn,
    Optional,
    Sequence,
)

from aiobotocore.client import AioBaseClient

from .client import S3Client
from .literals import (
    ArchiveStatusType,
    BucketCannedACLType,
    BucketVersioningStatusType,
    ChecksumAlgorithmType,
    MetadataDirectiveType,
    MFADeleteStatusType,
    ObjectCannedACLType,
    ObjectLockLegalHoldStatusType,
    ObjectLockModeType,
    ObjectOwnershipType,
    ObjectStorageClassType,
    PayerType,
    ReplicationStatusType,
    ServerSideEncryptionType,
    StorageClassType,
    TaggingDirectiveType,
)
from .type_defs import (
    AbortMultipartUploadOutputTypeDef,
    AccessControlPolicyTypeDef,
    BlobTypeDef,
    BucketLifecycleConfigurationBucketLifecycleConfigurationTypeDef,
    BucketLoggingStatusBucketLoggingTypeDef,
    CompletedMultipartUploadTypeDef,
    CopyObjectOutputTypeDef,
    CopySourceOrStrTypeDef,
    CopySourceTypeDef,
    CORSConfigurationBucketCorsTypeDef,
    CORSRuleBucketCorsTypeDef,
    CreateBucketConfigurationTypeDef,
    CreateBucketOutputTypeDef,
    DeleteObjectOutputTypeDef,
    DeleteObjectsOutputTypeDef,
    DeleteTypeDef,
    ErrorDocumentResponseTypeDef,
    FileobjTypeDef,
    GetObjectOutputTypeDef,
    GrantTypeDef,
    HeadObjectOutputTypeDef,
    IndexDocumentResponseTypeDef,
    InitiatorResponseTypeDef,
    LambdaFunctionConfigurationBucketNotificationTypeDef,
    LifecycleConfigurationBucketLifecycleTypeDef,
    LifecycleRuleBucketLifecycleConfigurationTypeDef,
    LoggingEnabledResponseTypeDef,
    NotificationConfigurationBucketNotificationTypeDef,
    OwnerResponseTypeDef,
    OwnerTypeDef,
    PutObjectAclOutputTypeDef,
    PutObjectOutputTypeDef,
    QueueConfigurationBucketNotificationTypeDef,
    RedirectAllRequestsToResponseTypeDef,
    RequestPaymentConfigurationTypeDef,
    RestoreObjectOutputTypeDef,
    RestoreRequestTypeDef,
    RestoreStatusResponseTypeDef,
    RestoreStatusTypeDef,
    RoutingRuleTypeDef,
    RuleBucketLifecycleTypeDef,
    TaggingTypeDef,
    TagTypeDef,
    TimestampTypeDef,
    TopicConfigurationBucketNotificationTypeDef,
    UploadPartCopyOutputTypeDef,
    UploadPartOutputTypeDef,
    VersioningConfigurationTypeDef,
    WebsiteConfigurationTypeDef,
)

try:
    from aioboto3.resources.base import AIOBoto3ServiceResource
except ImportError:
    from builtins import object as AIOBoto3ServiceResource
try:
    from aioboto3.resources.collection import AIOResourceCollection
except ImportError:
    from builtins import object as AIOResourceCollection
if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
try:
    from boto3.resources.base import ResourceMeta
except ImportError:
    from builtins import object as ResourceMeta
try:
    from boto3.s3.transfer import TransferConfig
except ImportError:
    from builtins import object as TransferConfig

__all__ = (
    "S3ServiceResource",
    "Bucket",
    "BucketAcl",
    "BucketCors",
    "BucketLifecycle",
    "BucketLifecycleConfiguration",
    "BucketLogging",
    "BucketNotification",
    "BucketPolicy",
    "BucketRequestPayment",
    "BucketTagging",
    "BucketVersioning",
    "BucketWebsite",
    "MultipartUpload",
    "MultipartUploadPart",
    "Object",
    "ObjectAcl",
    "ObjectSummary",
    "ObjectVersion",
    "ServiceResourceBucketsCollection",
    "BucketMultipartUploadsCollection",
    "BucketObjectVersionsCollection",
    "BucketObjectsCollection",
    "MultipartUploadPartsCollection",
)


class ServiceResourceBucketsCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
    """

    def all(self) -> "ServiceResourceBucketsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """

    def filter(self) -> "ServiceResourceBucketsCollection":  # type: ignore
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """

    def limit(self, count: int) -> "ServiceResourceBucketsCollection":
        """
        Return at most this many Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceBucketsCollection":
        """
        Fetch at most this many Buckets per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """

    def pages(self) -> AsyncIterator[List["Bucket"]]:
        """
        A generator which yields pages of Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """

    def __aiter__(self) -> AsyncIterator["Bucket"]:
        """
        A generator which yields Buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#serviceresourcebucketscollection)
        """


class BucketMultipartUploadsCollection(AIOResourceCollection):
    def all(self) -> "BucketMultipartUploadsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Delimiter: str = ...,
        EncodingType: Literal["url"] = ...,
        KeyMarker: str = ...,
        MaxUploads: int = ...,
        Prefix: str = ...,
        UploadIdMarker: str = ...,
        ExpectedBucketOwner: str = ...,
        RequestPayer: Literal["requester"] = ...,
    ) -> "BucketMultipartUploadsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "BucketMultipartUploadsCollection":
        """
        Return at most this many MultipartUploads.
        """

    def page_size(self, count: int) -> "BucketMultipartUploadsCollection":
        """
        Fetch at most this many MultipartUploads per service request.
        """

    def pages(self) -> AsyncIterator[List["MultipartUpload"]]:
        """
        A generator which yields pages of MultipartUploads.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields MultipartUploads.
        """

    def __aiter__(self) -> AsyncIterator["MultipartUpload"]:
        """
        A generator which yields MultipartUploads.
        """


class BucketObjectVersionsCollection(AIOResourceCollection):
    def all(self) -> "BucketObjectVersionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Delimiter: str = ...,
        EncodingType: Literal["url"] = ...,
        KeyMarker: str = ...,
        MaxKeys: int = ...,
        Prefix: str = ...,
        VersionIdMarker: str = ...,
        ExpectedBucketOwner: str = ...,
        RequestPayer: Literal["requester"] = ...,
        OptionalObjectAttributes: Sequence[Literal["RestoreStatus"]] = ...,
    ) -> "BucketObjectVersionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
    ) -> List[DeleteObjectsOutputTypeDef]:
        """
        Batch method.
        """

    def limit(self, count: int) -> "BucketObjectVersionsCollection":
        """
        Return at most this many ObjectVersions.
        """

    def page_size(self, count: int) -> "BucketObjectVersionsCollection":
        """
        Fetch at most this many ObjectVersions per service request.
        """

    def pages(self) -> AsyncIterator[List["ObjectVersion"]]:
        """
        A generator which yields pages of ObjectVersions.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields ObjectVersions.
        """

    def __aiter__(self) -> AsyncIterator["ObjectVersion"]:
        """
        A generator which yields ObjectVersions.
        """


class BucketObjectsCollection(AIOResourceCollection):
    def all(self) -> "BucketObjectsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        Delimiter: str = ...,
        EncodingType: Literal["url"] = ...,
        Marker: str = ...,
        MaxKeys: int = ...,
        Prefix: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...,
        OptionalObjectAttributes: Sequence[Literal["RestoreStatus"]] = ...,
    ) -> "BucketObjectsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
    ) -> List[DeleteObjectsOutputTypeDef]:
        """
        Batch method.
        """

    def limit(self, count: int) -> "BucketObjectsCollection":
        """
        Return at most this many ObjectSummarys.
        """

    def page_size(self, count: int) -> "BucketObjectsCollection":
        """
        Fetch at most this many ObjectSummarys per service request.
        """

    def pages(self) -> AsyncIterator[List["ObjectSummary"]]:
        """
        A generator which yields pages of ObjectSummarys.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields ObjectSummarys.
        """

    def __aiter__(self) -> AsyncIterator["ObjectSummary"]:
        """
        A generator which yields ObjectSummarys.
        """


class MultipartUploadPartsCollection(AIOResourceCollection):
    def all(self) -> "MultipartUploadPartsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        MaxParts: int = ...,
        PartNumberMarker: int = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
    ) -> "MultipartUploadPartsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "MultipartUploadPartsCollection":
        """
        Return at most this many MultipartUploadParts.
        """

    def page_size(self, count: int) -> "MultipartUploadPartsCollection":
        """
        Fetch at most this many MultipartUploadParts per service request.
        """

    def pages(self) -> AsyncIterator[List["MultipartUploadPart"]]:
        """
        A generator which yields pages of MultipartUploadParts.
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields MultipartUploadParts.
        """

    def __aiter__(self) -> AsyncIterator["MultipartUploadPart"]:
        """
        A generator which yields MultipartUploadParts.
        """


class BucketAcl(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketAcl)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketacl)
    """

    owner: Awaitable[OwnerTypeDef]
    grants: Awaitable[List[GrantTypeDef]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketaclbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketaclget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_acl` to update the attributes of the
        BucketAcl
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketaclload-method)
        """

    async def put(
        self,
        *,
        ACL: BucketCannedACLType = ...,
        AccessControlPolicy: AccessControlPolicyTypeDef = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketaclput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_acl` to update the attributes of the
        BucketAcl
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketAcl.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketaclreload-method)
        """


_BucketAcl = BucketAcl


class BucketCors(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketCors)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcors)
    """

    cors_rules: Awaitable[List[CORSRuleBucketCorsTypeDef]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcorsbucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcorsdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcorsget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_cors` to update the attributes of the
        BucketCors
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcorsload-method)
        """

    async def put(
        self,
        *,
        CORSConfiguration: CORSConfigurationBucketCorsTypeDef,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcorsput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_cors` to update the attributes of the
        BucketCors
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketCors.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcorsreload-method)
        """


_BucketCors = BucketCors


class BucketLifecycle(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycle)
    """

    rules: Awaitable[List[RuleBucketLifecycleTypeDef]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecyclebucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycledelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle` to update the attributes of the
        BucketLifecycle
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleload-method)
        """

    async def put(
        self,
        *,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        LifecycleConfiguration: LifecycleConfigurationBucketLifecycleTypeDef = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle` to update the attributes of the
        BucketLifecycle
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycle.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecyclereload-method)
        """


_BucketLifecycle = BucketLifecycle


class BucketLifecycleConfiguration(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfiguration)
    """

    rules: Awaitable[List[LifecycleRuleBucketLifecycleConfigurationTypeDef]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfigurationbucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfigurationdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfigurationget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle_configuration` to update the
        attributes of the BucketLifecycleConfiguration
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfigurationload-method)
        """

    async def put(
        self,
        *,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        LifecycleConfiguration: BucketLifecycleConfigurationBucketLifecycleConfigurationTypeDef = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfigurationput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_lifecycle_configuration` to update the
        attributes of the BucketLifecycleConfiguration
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLifecycleConfiguration.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfigurationreload-method)
        """


_BucketLifecycleConfiguration = BucketLifecycleConfiguration


class BucketLogging(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLogging)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlogging)
    """

    logging_enabled: Awaitable[LoggingEnabledResponseTypeDef]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketloggingbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketloggingget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_logging` to update the attributes of the
        BucketLogging
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketloggingload-method)
        """

    async def put(
        self,
        *,
        BucketLoggingStatus: BucketLoggingStatusBucketLoggingTypeDef,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketloggingput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_logging` to update the attributes of the
        BucketLogging
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketLogging.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketloggingreload-method)
        """


_BucketLogging = BucketLogging


class BucketNotification(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketNotification)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotification)
    """

    topic_configurations: Awaitable[List[TopicConfigurationBucketNotificationTypeDef]]
    queue_configurations: Awaitable[List[QueueConfigurationBucketNotificationTypeDef]]
    lambda_function_configurations: Awaitable[
        List[LambdaFunctionConfigurationBucketNotificationTypeDef]
    ]
    event_bridge_configuration: Awaitable[Dict[str, Any]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotificationbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotificationget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_notification_configuration` to update the
        attributes of the BucketNotification
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotificationload-method)
        """

    async def put(
        self,
        *,
        NotificationConfiguration: NotificationConfigurationBucketNotificationTypeDef,
        ExpectedBucketOwner: str = ...,
        SkipDestinationValidation: bool = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotificationput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_notification_configuration` to update the
        attributes of the BucketNotification
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketNotification.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotificationreload-method)
        """


_BucketNotification = BucketNotification


class BucketPolicy(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicy)
    """

    policy: Awaitable[str]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicybucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the policy of a specified bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicydelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicyget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_policy` to update the attributes of the
        BucketPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicyload-method)
        """

    async def put(
        self,
        *,
        Policy: str,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ConfirmRemoveSelfBucketAccess: bool = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        Applies an Amazon S3 bucket policy to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicyput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_policy` to update the attributes of the
        BucketPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketPolicy.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicyreload-method)
        """


_BucketPolicy = BucketPolicy


class BucketRequestPayment(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpayment)
    """

    payer: Awaitable[PayerType]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpaymentbucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpaymentget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_request_payment` to update the attributes
        of the BucketRequestPayment
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpaymentload-method)
        """

    async def put(
        self,
        *,
        RequestPaymentConfiguration: RequestPaymentConfigurationTypeDef,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpaymentput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_request_payment` to update the attributes
        of the BucketRequestPayment
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketRequestPayment.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpaymentreload-method)
        """


_BucketRequestPayment = BucketRequestPayment


class BucketTagging(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketTagging)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettagging)
    """

    tag_set: Awaitable[List[TagTypeDef]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettaggingbucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettaggingdelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettaggingget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_tagging` to update the attributes of the
        BucketTagging
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettaggingload-method)
        """

    async def put(
        self,
        *,
        Tagging: TaggingTypeDef,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettaggingput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_tagging` to update the attributes of the
        BucketTagging
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketTagging.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettaggingreload-method)
        """


_BucketTagging = BucketTagging


class BucketVersioning(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioning)
    """

    status: Awaitable[BucketVersioningStatusType]
    mfa_delete: Awaitable[MFADeleteStatusType]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningbucket-method)
        """

    async def enable(
        self,
        *,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        MFA: str = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.enable)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningenable-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_versioning` to update the attributes of
        the BucketVersioning
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningload-method)
        """

    async def put(
        self,
        *,
        VersioningConfiguration: VersioningConfigurationTypeDef,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        MFA: str = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_versioning` to update the attributes of
        the BucketVersioning
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningreload-method)
        """

    async def suspend(
        self,
        *,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        MFA: str = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketVersioning.suspend)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioningsuspend-method)
        """


_BucketVersioning = BucketVersioning


class BucketWebsite(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsite)
    """

    redirect_all_requests_to: Awaitable[RedirectAllRequestsToResponseTypeDef]
    index_document: Awaitable[IndexDocumentResponseTypeDef]
    error_document: Awaitable[ErrorDocumentResponseTypeDef]
    routing_rules: Awaitable[List[RoutingRuleTypeDef]]
    bucket_name: str
    meta: Awaitable["S3ResourceMeta"]

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsitebucket-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsitedelete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsiteget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_website` to update the attributes of the
        BucketWebsite
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsiteload-method)
        """

    async def put(
        self,
        *,
        WebsiteConfiguration: WebsiteConfigurationTypeDef,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> None:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsiteput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_bucket_website` to update the attributes of the
        BucketWebsite
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.BucketWebsite.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsitereload-method)
        """


_BucketWebsite = BucketWebsite


class MultipartUploadPart(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadpart)
    """

    last_modified: Awaitable[datetime]
    e_tag: Awaitable[str]
    size: Awaitable[int]
    checksum_crc32: Awaitable[str]
    checksum_crc32_c: Awaitable[str]
    checksum_sha1: Awaitable[str]
    checksum_sha256: Awaitable[str]
    bucket_name: str
    object_key: str
    multipart_upload_id: str
    part_number: str
    meta: Awaitable["S3ResourceMeta"]

    async def MultipartUpload(self) -> "_MultipartUpload":
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.MultipartUpload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadpartmultipartupload-method)
        """

    async def copy_from(
        self,
        *,
        CopySource: CopySourceOrStrTypeDef,
        CopySourceIfMatch: str = ...,
        CopySourceIfModifiedSince: TimestampTypeDef = ...,
        CopySourceIfNoneMatch: str = ...,
        CopySourceIfUnmodifiedSince: TimestampTypeDef = ...,
        CopySourceRange: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        CopySourceSSECustomerAlgorithm: str = ...,
        CopySourceSSECustomerKey: str = ...,
        CopySourceSSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...,
        ExpectedSourceBucketOwner: str = ...,
    ) -> UploadPartCopyOutputTypeDef:
        """
        Uploads a part by copying data from an existing object as data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.copy_from)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadpartcopy_from-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadpartget_available_subresources-method)
        """

    async def upload(
        self,
        *,
        Body: BlobTypeDef = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ChecksumCRC32: str = ...,
        ChecksumCRC32C: str = ...,
        ChecksumSHA1: str = ...,
        ChecksumSHA256: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...,
    ) -> UploadPartOutputTypeDef:
        """
        Uploads a part in a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUploadPart.upload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadpartupload-method)
        """


_MultipartUploadPart = MultipartUploadPart


class ObjectAcl(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectacl)
    """

    owner: Awaitable[OwnerTypeDef]
    grants: Awaitable[List[GrantTypeDef]]
    request_charged: Awaitable[Literal["requester"]]
    bucket_name: str
    object_key: str
    meta: Awaitable["S3ResourceMeta"]

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.Object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectaclobject-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectaclget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_object_acl` to update the attributes of the
        ObjectAcl
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectaclload-method)
        """

    async def put(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        AccessControlPolicy: AccessControlPolicyTypeDef = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        RequestPayer: Literal["requester"] = ...,
        VersionId: str = ...,
        ExpectedBucketOwner: str = ...,
    ) -> PutObjectAclOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectaclput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.get_object_acl` to update the attributes of the
        ObjectAcl
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectAcl.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectaclreload-method)
        """


_ObjectAcl = ObjectAcl


class ObjectVersion(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversion)
    """

    e_tag: Awaitable[str]
    checksum_algorithm: Awaitable[List[ChecksumAlgorithmType]]
    size: Awaitable[int]
    storage_class: Awaitable[Literal["STANDARD"]]
    key: Awaitable[str]
    version_id: Awaitable[str]
    is_latest: Awaitable[bool]
    last_modified: Awaitable[datetime]
    owner: Awaitable[OwnerResponseTypeDef]
    restore_status: Awaitable[RestoreStatusResponseTypeDef]
    bucket_name: str
    object_key: str
    id: str
    meta: Awaitable["S3ResourceMeta"]

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.Object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversionobject-method)
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...,
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes an object from a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversiondelete-method)
        """

    async def get(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: TimestampTypeDef = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: TimestampTypeDef = ...,
        Range: str = ...,
        ResponseCacheControl: str = ...,
        ResponseContentDisposition: str = ...,
        ResponseContentEncoding: str = ...,
        ResponseContentLanguage: str = ...,
        ResponseContentType: str = ...,
        ResponseExpires: TimestampTypeDef = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumMode: Literal["ENABLED"] = ...,
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves an object from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.get)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversionget-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversionget_available_subresources-method)
        """

    async def head(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: TimestampTypeDef = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: TimestampTypeDef = ...,
        Range: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumMode: Literal["ENABLED"] = ...,
    ) -> HeadObjectOutputTypeDef:
        """
        The `HEAD` operation retrieves metadata from an object without returning the
        object
        itself.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectVersion.head)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversionhead-method)
        """


_ObjectVersion = ObjectVersion


class MultipartUpload(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartupload)
    """

    upload_id: Awaitable[str]
    key: Awaitable[str]
    initiated: Awaitable[datetime]
    storage_class: Awaitable[StorageClassType]
    owner: Awaitable[OwnerTypeDef]
    initiator: Awaitable[InitiatorResponseTypeDef]
    checksum_algorithm: Awaitable[ChecksumAlgorithmType]
    bucket_name: str
    object_key: str
    id: str
    parts: MultipartUploadPartsCollection
    meta: Awaitable["S3ResourceMeta"]

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.Object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadobject-method)
        """

    async def Part(self, part_number: str) -> "_MultipartUploadPart":
        """
        Creates a MultipartUploadPart resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.Part)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadpart-method)
        """

    async def abort(
        self, *, RequestPayer: Literal["requester"] = ..., ExpectedBucketOwner: str = ...
    ) -> AbortMultipartUploadOutputTypeDef:
        """
        This operation aborts a multipart upload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.abort)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadabort-method)
        """

    async def complete(
        self,
        *,
        MultipartUpload: CompletedMultipartUploadTypeDef = ...,
        ChecksumCRC32: str = ...,
        ChecksumCRC32C: str = ...,
        ChecksumSHA1: str = ...,
        ChecksumSHA256: str = ...,
        RequestPayer: Literal["requester"] = ...,
        ExpectedBucketOwner: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
    ) -> "_Object":
        """
        Completes a multipart upload by assembling previously uploaded parts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.complete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadcomplete-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.MultipartUpload.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#multipartuploadget_available_subresources-method)
        """


_MultipartUpload = MultipartUpload


class Object(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Object)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#object)
    """

    delete_marker: Awaitable[bool]
    accept_ranges: Awaitable[str]
    expiration: Awaitable[str]
    restore: Awaitable[str]
    archive_status: Awaitable[ArchiveStatusType]
    last_modified: Awaitable[datetime]
    content_length: Awaitable[int]
    checksum_crc32: Awaitable[str]
    checksum_crc32_c: Awaitable[str]
    checksum_sha1: Awaitable[str]
    checksum_sha256: Awaitable[str]
    e_tag: Awaitable[str]
    missing_meta: Awaitable[int]
    version_id: Awaitable[str]
    cache_control: Awaitable[str]
    content_disposition: Awaitable[str]
    content_encoding: Awaitable[str]
    content_language: Awaitable[str]
    content_type: Awaitable[str]
    expires: Awaitable[datetime]
    website_redirect_location: Awaitable[str]
    server_side_encryption: Awaitable[ServerSideEncryptionType]
    metadata: Awaitable[Dict[str, str]]
    sse_customer_algorithm: Awaitable[str]
    sse_customer_key_md5: Awaitable[str]
    ssekms_key_id: Awaitable[str]
    bucket_key_enabled: Awaitable[bool]
    storage_class: Awaitable[StorageClassType]
    request_charged: Awaitable[Literal["requester"]]
    replication_status: Awaitable[ReplicationStatusType]
    parts_count: Awaitable[int]
    object_lock_mode: Awaitable[ObjectLockModeType]
    object_lock_retain_until_date: Awaitable[datetime]
    object_lock_legal_hold_status: Awaitable[ObjectLockLegalHoldStatusType]
    bucket_name: str
    key: str
    meta: Awaitable["S3ResourceMeta"]

    async def Acl(self) -> "_ObjectAcl":
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.Acl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectacl-method)
        """

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectbucket-method)
        """

    async def MultipartUpload(self, id: str) -> "_MultipartUpload":
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.MultipartUpload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectmultipartupload-method)
        """

    async def Version(self, id: str) -> "_ObjectVersion":
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.Version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectversion-method)
        """

    async def copy(
        self,
        CopySource: CopySourceTypeDef,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        SourceClient: Optional[AioBaseClient] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Copy an object from one S3 location to this object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.copy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectcopy-method)
        """

    async def copy_from(
        self,
        *,
        CopySource: str,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        CopySourceIfMatch: str = ...,
        CopySourceIfModifiedSince: TimestampTypeDef = ...,
        CopySourceIfNoneMatch: str = ...,
        CopySourceIfUnmodifiedSince: TimestampTypeDef = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        MetadataDirective: MetadataDirectiveType = ...,
        TaggingDirective: TaggingDirectiveType = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        CopySourceSSECustomerAlgorithm: str = ...,
        CopySourceSSECustomerKey: str = ...,
        CopySourceSSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
        ExpectedSourceBucketOwner: str = ...,
    ) -> CopyObjectOutputTypeDef:
        """
        Creates a copy of an object that is already stored in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.copy_from)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectcopy_from-method)
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        VersionId: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...,
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes an object from a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectdelete-method)
        """

    async def download_file(
        self,
        Filename: str,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.download_file)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectdownload_file-method)
        """

    async def download_fileobj(
        self,
        Fileobj: FileobjTypeDef,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Download this object from S3 to a file-like object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.download_fileobj)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectdownload_fileobj-method)
        """

    async def get(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: TimestampTypeDef = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: TimestampTypeDef = ...,
        Range: str = ...,
        ResponseCacheControl: str = ...,
        ResponseContentDisposition: str = ...,
        ResponseContentEncoding: str = ...,
        ResponseContentLanguage: str = ...,
        ResponseContentType: str = ...,
        ResponseExpires: TimestampTypeDef = ...,
        VersionId: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumMode: Literal["ENABLED"] = ...,
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves an object from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.get)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectget-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectget_available_subresources-method)
        """

    async def initiate_multipart_upload(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
    ) -> "_MultipartUpload":
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.initiate_multipart_upload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectinitiate_multipart_upload-method)
        """

    async def load(self) -> None:
        """
        Calls :py:meth:`S3.Client.head_object` to update the attributes of the Object
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectload-method)
        """

    async def put(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        Body: BlobTypeDef = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ContentType: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ChecksumCRC32: str = ...,
        ChecksumCRC32C: str = ...,
        ChecksumSHA1: str = ...,
        ChecksumSHA256: str = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> PutObjectOutputTypeDef:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectput-method)
        """

    async def reload(self) -> None:
        """
        Calls :py:meth:`S3.Client.head_object` to update the attributes of the Object
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.reload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectreload-method)
        """

    async def restore_object(
        self,
        *,
        VersionId: str = ...,
        RestoreRequest: RestoreRequestTypeDef = ...,
        RequestPayer: Literal["requester"] = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> RestoreObjectOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.restore_object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectrestore_object-method)
        """

    async def upload_file(
        self,
        Filename: str,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.upload_file)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectupload_file-method)
        """

    async def upload_fileobj(
        self,
        Fileobj: FileobjTypeDef,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Upload a file-like object to this object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.upload_fileobj)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectupload_fileobj-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Object is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectwait_until_exists-method)
        """

    async def wait_until_not_exists(self) -> None:
        """
        Waits until this Object is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Object.wait_until_not_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectwait_until_not_exists-method)
        """


_Object = Object


class ObjectSummary(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummary)
    """

    last_modified: Awaitable[datetime]
    e_tag: Awaitable[str]
    checksum_algorithm: Awaitable[List[ChecksumAlgorithmType]]
    size: Awaitable[int]
    storage_class: Awaitable[ObjectStorageClassType]
    owner: Awaitable[OwnerTypeDef]
    restore_status: Awaitable[RestoreStatusTypeDef]
    bucket_name: str
    key: str
    meta: Awaitable["S3ResourceMeta"]

    async def Acl(self) -> "_ObjectAcl":
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Acl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryacl-method)
        """

    async def Bucket(self) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummarybucket-method)
        """

    async def MultipartUpload(self, id: str) -> "_MultipartUpload":
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.MultipartUpload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummarymultipartupload-method)
        """

    async def Object(self) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryobject-method)
        """

    async def Version(self, id: str) -> "_ObjectVersion":
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.Version)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryversion-method)
        """

    async def copy_from(
        self,
        *,
        CopySource: str,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        CopySourceIfMatch: str = ...,
        CopySourceIfModifiedSince: TimestampTypeDef = ...,
        CopySourceIfNoneMatch: str = ...,
        CopySourceIfUnmodifiedSince: TimestampTypeDef = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        MetadataDirective: MetadataDirectiveType = ...,
        TaggingDirective: TaggingDirectiveType = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        CopySourceSSECustomerAlgorithm: str = ...,
        CopySourceSSECustomerKey: str = ...,
        CopySourceSSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
        ExpectedSourceBucketOwner: str = ...,
    ) -> CopyObjectOutputTypeDef:
        """
        Creates a copy of an object that is already stored in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.copy_from)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummarycopy_from-method)
        """

    async def delete(
        self,
        *,
        MFA: str = ...,
        VersionId: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...,
    ) -> DeleteObjectOutputTypeDef:
        """
        Removes an object from a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummarydelete-method)
        """

    async def get(
        self,
        *,
        IfMatch: str = ...,
        IfModifiedSince: TimestampTypeDef = ...,
        IfNoneMatch: str = ...,
        IfUnmodifiedSince: TimestampTypeDef = ...,
        Range: str = ...,
        ResponseCacheControl: str = ...,
        ResponseContentDisposition: str = ...,
        ResponseContentEncoding: str = ...,
        ResponseContentLanguage: str = ...,
        ResponseContentType: str = ...,
        ResponseExpires: TimestampTypeDef = ...,
        VersionId: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        RequestPayer: Literal["requester"] = ...,
        PartNumber: int = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumMode: Literal["ENABLED"] = ...,
    ) -> GetObjectOutputTypeDef:
        """
        Retrieves an object from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.get)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryget-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryget_available_subresources-method)
        """

    async def initiate_multipart_upload(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentType: str = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
    ) -> "_MultipartUpload":
        """
        This action initiates a multipart upload and returns an upload ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.initiate_multipart_upload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryinitiate_multipart_upload-method)
        """

    async def load(self) -> None:
        """
        Calls s3.Client.head_object to update the attributes of the ObjectSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryload-method)
        """

    async def put(
        self,
        *,
        ACL: ObjectCannedACLType = ...,
        Body: BlobTypeDef = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ContentType: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ChecksumCRC32: str = ...,
        ChecksumCRC32C: str = ...,
        ChecksumSHA1: str = ...,
        ChecksumSHA256: str = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> PutObjectOutputTypeDef:
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.put)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryput-method)
        """

    async def restore_object(
        self,
        *,
        VersionId: str = ...,
        RestoreRequest: RestoreRequestTypeDef = ...,
        RequestPayer: Literal["requester"] = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> RestoreObjectOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.restore_object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummaryrestore_object-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this ObjectSummary is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummarywait_until_exists-method)
        """

    async def wait_until_not_exists(self) -> None:
        """
        Waits until this ObjectSummary is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ObjectSummary.wait_until_not_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#objectsummarywait_until_not_exists-method)
        """


_ObjectSummary = ObjectSummary


class Bucket(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Bucket)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucket)
    """

    creation_date: Awaitable[datetime]
    name: str
    multipart_uploads: BucketMultipartUploadsCollection
    object_versions: BucketObjectVersionsCollection
    objects: BucketObjectsCollection
    meta: Awaitable["S3ResourceMeta"]

    async def Acl(self) -> "_BucketAcl":
        """
        Creates a BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Acl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketacl-method)
        """

    async def Cors(self) -> "_BucketCors":
        """
        Creates a BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Cors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcors-method)
        """

    async def Lifecycle(self) -> "_BucketLifecycle":
        """
        Creates a BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Lifecycle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycle-method)
        """

    async def LifecycleConfiguration(self) -> "_BucketLifecycleConfiguration":
        """
        Creates a BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.LifecycleConfiguration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlifecycleconfiguration-method)
        """

    async def Logging(self) -> "_BucketLogging":
        """
        Creates a BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Logging)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketlogging-method)
        """

    async def Notification(self) -> "_BucketNotification":
        """
        Creates a BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Notification)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketnotification-method)
        """

    async def Object(self, key: str) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketobject-method)
        """

    async def Policy(self) -> "_BucketPolicy":
        """
        Creates a BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Policy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketpolicy-method)
        """

    async def RequestPayment(self) -> "_BucketRequestPayment":
        """
        Creates a BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.RequestPayment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketrequestpayment-method)
        """

    async def Tagging(self) -> "_BucketTagging":
        """
        Creates a BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Tagging)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#buckettagging-method)
        """

    async def Versioning(self) -> "_BucketVersioning":
        """
        Creates a BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Versioning)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketversioning-method)
        """

    async def Website(self) -> "_BucketWebsite":
        """
        Creates a BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.Website)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwebsite-method)
        """

    async def copy(
        self,
        CopySource: CopySourceTypeDef,
        Key: str,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        SourceClient: Optional[AioBaseClient] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Copy an object from one S3 location to an object in this bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.copy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcopy-method)
        """

    async def create(
        self,
        *,
        ACL: BucketCannedACLType = ...,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        ObjectLockEnabledForBucket: bool = ...,
        ObjectOwnership: ObjectOwnershipType = ...,
    ) -> CreateBucketOutputTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.create)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketcreate-method)
        """

    async def delete(self, *, ExpectedBucketOwner: str = ...) -> None:
        """
        Deletes the S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.delete)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketdelete-method)
        """

    async def delete_objects(
        self,
        *,
        Delete: DeleteTypeDef,
        MFA: str = ...,
        RequestPayer: Literal["requester"] = ...,
        BypassGovernanceRetention: bool = ...,
        ExpectedBucketOwner: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
    ) -> DeleteObjectsOutputTypeDef:
        """
        This operation enables you to delete multiple objects from a bucket using a
        single HTTP
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.delete_objects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketdelete_objects-method)
        """

    async def download_file(
        self,
        Key: str,
        Filename: str,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Download an S3 object to a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.download_file)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketdownload_file-method)
        """

    async def download_fileobj(
        self,
        Key: str,
        Fileobj: FileobjTypeDef,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Download an object from this bucket to a file-like-object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.download_fileobj)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketdownload_fileobj-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketget_available_subresources-method)
        """

    async def load(self) -> None:
        """
        Calls s3.Client.list_buckets() to update the attributes of the Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.load)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketload-method)
        """

    async def put_object(
        self,
        *,
        Key: str,
        ACL: ObjectCannedACLType = ...,
        Body: BlobTypeDef = ...,
        CacheControl: str = ...,
        ContentDisposition: str = ...,
        ContentEncoding: str = ...,
        ContentLanguage: str = ...,
        ContentLength: int = ...,
        ContentMD5: str = ...,
        ContentType: str = ...,
        ChecksumAlgorithm: ChecksumAlgorithmType = ...,
        ChecksumCRC32: str = ...,
        ChecksumCRC32C: str = ...,
        ChecksumSHA1: str = ...,
        ChecksumSHA256: str = ...,
        Expires: TimestampTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWriteACP: str = ...,
        Metadata: Mapping[str, str] = ...,
        ServerSideEncryption: ServerSideEncryptionType = ...,
        StorageClass: StorageClassType = ...,
        WebsiteRedirectLocation: str = ...,
        SSECustomerAlgorithm: str = ...,
        SSECustomerKey: str = ...,
        SSECustomerKeyMD5: str = ...,
        SSEKMSKeyId: str = ...,
        SSEKMSEncryptionContext: str = ...,
        BucketKeyEnabled: bool = ...,
        RequestPayer: Literal["requester"] = ...,
        Tagging: str = ...,
        ObjectLockMode: ObjectLockModeType = ...,
        ObjectLockRetainUntilDate: TimestampTypeDef = ...,
        ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatusType = ...,
        ExpectedBucketOwner: str = ...,
    ) -> "_Object":
        """
        Adds an object to a bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.put_object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketput_object-method)
        """

    async def upload_file(
        self,
        Filename: str,
        Key: str,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Upload a file to an S3 object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.upload_file)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketupload_file-method)
        """

    async def upload_fileobj(
        self,
        Fileobj: FileobjTypeDef,
        Key: str,
        ExtraArgs: Optional[Dict[str, Any]] = ...,
        Callback: Optional[Callable[..., Any]] = ...,
        Config: Optional[TransferConfig] = ...,
    ) -> None:
        """
        Upload a file-like object to this bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.upload_fileobj)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketupload_fileobj-method)
        """

    async def wait_until_exists(self) -> None:
        """
        Waits until this Bucket is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.wait_until_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwait_until_exists-method)
        """

    async def wait_until_not_exists(self) -> None:
        """
        Waits until this Bucket is not exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.wait_until_not_exists)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#bucketwait_until_not_exists-method)
        """


_Bucket = Bucket


class S3ResourceMeta(ResourceMeta):
    client: S3Client


class S3ServiceResource(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/)
    """

    meta: "S3ResourceMeta"
    buckets: ServiceResourceBucketsCollection

    async def Bucket(self, name: str) -> "_Bucket":
        """
        Creates a Bucket resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucket-method)
        """

    async def BucketAcl(self, bucket_name: str) -> "_BucketAcl":
        """
        Creates a BucketAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketAcl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketacl-method)
        """

    async def BucketCors(self, bucket_name: str) -> "_BucketCors":
        """
        Creates a BucketCors resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketCors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketcors-method)
        """

    async def BucketLifecycle(self, bucket_name: str) -> "_BucketLifecycle":
        """
        Creates a BucketLifecycle resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycle)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketlifecycle-method)
        """

    async def BucketLifecycleConfiguration(
        self, bucket_name: str
    ) -> "_BucketLifecycleConfiguration":
        """
        Creates a BucketLifecycleConfiguration resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLifecycleConfiguration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketlifecycleconfiguration-method)
        """

    async def BucketLogging(self, bucket_name: str) -> "_BucketLogging":
        """
        Creates a BucketLogging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketLogging)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketlogging-method)
        """

    async def BucketNotification(self, bucket_name: str) -> "_BucketNotification":
        """
        Creates a BucketNotification resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketNotification)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketnotification-method)
        """

    async def BucketPolicy(self, bucket_name: str) -> "_BucketPolicy":
        """
        Creates a BucketPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketPolicy)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketpolicy-method)
        """

    async def BucketRequestPayment(self, bucket_name: str) -> "_BucketRequestPayment":
        """
        Creates a BucketRequestPayment resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketRequestPayment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketrequestpayment-method)
        """

    async def BucketTagging(self, bucket_name: str) -> "_BucketTagging":
        """
        Creates a BucketTagging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketTagging)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebuckettagging-method)
        """

    async def BucketVersioning(self, bucket_name: str) -> "_BucketVersioning":
        """
        Creates a BucketVersioning resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketVersioning)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketversioning-method)
        """

    async def BucketWebsite(self, bucket_name: str) -> "_BucketWebsite":
        """
        Creates a BucketWebsite resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.BucketWebsite)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcebucketwebsite-method)
        """

    async def MultipartUpload(
        self, bucket_name: str, object_key: str, id: str
    ) -> "_MultipartUpload":
        """
        Creates a MultipartUpload resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUpload)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcemultipartupload-method)
        """

    async def MultipartUploadPart(
        self, bucket_name: str, object_key: str, multipart_upload_id: str, part_number: str
    ) -> "_MultipartUploadPart":
        """
        Creates a MultipartUploadPart resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.MultipartUploadPart)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcemultipartuploadpart-method)
        """

    async def Object(self, bucket_name: str, key: str) -> "_Object":
        """
        Creates a Object resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.Object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourceobject-method)
        """

    async def ObjectAcl(self, bucket_name: str, object_key: str) -> "_ObjectAcl":
        """
        Creates a ObjectAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectAcl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourceobjectacl-method)
        """

    async def ObjectSummary(self, bucket_name: str, key: str) -> "_ObjectSummary":
        """
        Creates a ObjectSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectSummary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourceobjectsummary-method)
        """

    async def ObjectVersion(self, bucket_name: str, object_key: str, id: str) -> "_ObjectVersion":
        """
        Creates a ObjectVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.ObjectVersion)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourceobjectversion-method)
        """

    async def create_bucket(
        self,
        *,
        Bucket: str,
        ACL: BucketCannedACLType = ...,
        CreateBucketConfiguration: CreateBucketConfigurationTypeDef = ...,
        GrantFullControl: str = ...,
        GrantRead: str = ...,
        GrantReadACP: str = ...,
        GrantWrite: str = ...,
        GrantWriteACP: str = ...,
        ObjectLockEnabledForBucket: bool = ...,
        ObjectOwnership: ObjectOwnershipType = ...,
    ) -> "_Bucket":
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.create_bucket)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourcecreate_bucket-method)
        """

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.get_available_subresources)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_s3/service_resource/#s3serviceresourceget_available_subresources-method)
        """
