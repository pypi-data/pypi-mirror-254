"""
Type annotations for codeartifact service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_codeartifact/type_defs/)

Usage::

    ```python
    from types_aiobotocore_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    AllowPublishType,
    AllowUpstreamType,
    DomainStatusType,
    HashAlgorithmType,
    PackageFormatType,
    PackageVersionErrorCodeType,
    PackageVersionOriginTypeType,
    PackageVersionStatusType,
)

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
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BlobTypeDef",
    "CopyPackageVersionsRequestRequestTypeDef",
    "PackageVersionErrorTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagTypeDef",
    "DomainDescriptionTypeDef",
    "UpstreamRepositoryTypeDef",
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    "ResourcePolicyTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageVersionsRequestRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribeRepositoryRequestRequestTypeDef",
    "DisassociateExternalConnectionRequestRequestTypeDef",
    "DisposePackageVersionsRequestRequestTypeDef",
    "DomainEntryPointTypeDef",
    "DomainSummaryTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetDomainPermissionsPolicyRequestRequestTypeDef",
    "GetPackageVersionAssetRequestRequestTypeDef",
    "GetPackageVersionReadmeRequestRequestTypeDef",
    "GetRepositoryEndpointRequestRequestTypeDef",
    "GetRepositoryPermissionsPolicyRequestRequestTypeDef",
    "LicenseInfoTypeDef",
    "PaginatorConfigTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListPackageVersionAssetsRequestRequestTypeDef",
    "ListPackageVersionDependenciesRequestRequestTypeDef",
    "PackageDependencyTypeDef",
    "ListPackageVersionsRequestRequestTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "ListRepositoriesInDomainRequestRequestTypeDef",
    "RepositorySummaryTypeDef",
    "ListRepositoriesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PackageOriginRestrictionsTypeDef",
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    "PutRepositoryPermissionsPolicyRequestRequestTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackageVersionsStatusRequestRequestTypeDef",
    "GetAuthorizationTokenResultTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "PublishPackageVersionResultTypeDef",
    "PublishPackageVersionRequestRequestTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "DeleteDomainResultTypeDef",
    "DescribeDomainResultTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "UpdateRepositoryRequestRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "PackageVersionOriginTypeDef",
    "ListDomainsResultTypeDef",
    "ListDomainsRequestListDomainsPaginateTypeDef",
    "ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef",
    "ListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    "ListPackagesRequestListPackagesPaginateTypeDef",
    "ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef",
    "ListRepositoriesRequestListRepositoriesPaginateTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesResultTypeDef",
    "PackageOriginConfigurationTypeDef",
    "PutPackageOriginConfigurationRequestRequestTypeDef",
    "RepositoryDescriptionTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionSummaryTypeDef",
    "PackageDescriptionTypeDef",
    "PackageSummaryTypeDef",
    "PutPackageOriginConfigurationResultTypeDef",
    "AssociateExternalConnectionResultTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "UpdateRepositoryResultTypeDef",
    "DescribePackageVersionResultTypeDef",
    "ListPackageVersionsResultTypeDef",
    "DescribePackageResultTypeDef",
    "DeletePackageResultTypeDef",
    "ListPackagesResultTypeDef",
)

AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "name": str,
        "size": NotRequired[int],
        "hashes": NotRequired[Dict[HashAlgorithmType, str]],
    },
)
AssociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "AssociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
        "domainOwner": NotRequired[str],
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
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CopyPackageVersionsRequestRequestTypeDef = TypedDict(
    "CopyPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "sourceRepository": str,
        "destinationRepository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versions": NotRequired[Sequence[str]],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "allowOverwrite": NotRequired[bool],
        "includeFromUpstream": NotRequired[bool],
    },
)
PackageVersionErrorTypeDef = TypedDict(
    "PackageVersionErrorTypeDef",
    {
        "errorCode": NotRequired[PackageVersionErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)
SuccessfulPackageVersionInfoTypeDef = TypedDict(
    "SuccessfulPackageVersionInfoTypeDef",
    {
        "revision": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)
DomainDescriptionTypeDef = TypedDict(
    "DomainDescriptionTypeDef",
    {
        "name": NotRequired[str],
        "owner": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[DomainStatusType],
        "createdTime": NotRequired[datetime],
        "encryptionKey": NotRequired[str],
        "repositoryCount": NotRequired[int],
        "assetSizeBytes": NotRequired[int],
        "s3BucketArn": NotRequired[str],
    },
)
UpstreamRepositoryTypeDef = TypedDict(
    "UpstreamRepositoryTypeDef",
    {
        "repositoryName": str,
    },
)
DeleteDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)
ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "resourceArn": NotRequired[str],
        "revision": NotRequired[str],
        "document": NotRequired[str],
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
    },
)
DeletePackageRequestRequestTypeDef = TypedDict(
    "DeletePackageRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
DeletePackageVersionsRequestRequestTypeDef = TypedDict(
    "DeletePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)
DeleteRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)
DeleteRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
    },
)
DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
    },
)
DescribePackageRequestRequestTypeDef = TypedDict(
    "DescribePackageRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
DescribePackageVersionRequestRequestTypeDef = TypedDict(
    "DescribePackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
DescribeRepositoryRequestRequestTypeDef = TypedDict(
    "DescribeRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
    },
)
DisassociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "DisassociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
        "domainOwner": NotRequired[str],
    },
)
DisposePackageVersionsRequestRequestTypeDef = TypedDict(
    "DisposePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)
DomainEntryPointTypeDef = TypedDict(
    "DomainEntryPointTypeDef",
    {
        "repositoryName": NotRequired[str],
        "externalConnectionName": NotRequired[str],
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "name": NotRequired[str],
        "owner": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[DomainStatusType],
        "createdTime": NotRequired[datetime],
        "encryptionKey": NotRequired[str],
    },
)
GetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "durationSeconds": NotRequired[int],
    },
)
GetDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "GetDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
    },
)
GetPackageVersionAssetRequestRequestTypeDef = TypedDict(
    "GetPackageVersionAssetRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "asset": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "packageVersionRevision": NotRequired[str],
    },
)
GetPackageVersionReadmeRequestRequestTypeDef = TypedDict(
    "GetPackageVersionReadmeRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
GetRepositoryEndpointRequestRequestTypeDef = TypedDict(
    "GetRepositoryEndpointRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "domainOwner": NotRequired[str],
    },
)
GetRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
    },
)
LicenseInfoTypeDef = TypedDict(
    "LicenseInfoTypeDef",
    {
        "name": NotRequired[str],
        "url": NotRequired[str],
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
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListPackageVersionAssetsRequestRequestTypeDef = TypedDict(
    "ListPackageVersionAssetsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListPackageVersionDependenciesRequestRequestTypeDef = TypedDict(
    "ListPackageVersionDependenciesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
PackageDependencyTypeDef = TypedDict(
    "PackageDependencyTypeDef",
    {
        "namespace": NotRequired[str],
        "package": NotRequired[str],
        "dependencyType": NotRequired[str],
        "versionRequirement": NotRequired[str],
    },
)
ListPackageVersionsRequestRequestTypeDef = TypedDict(
    "ListPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "sortBy": NotRequired[Literal["PUBLISHED_TIME"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "originType": NotRequired[PackageVersionOriginTypeType],
    },
)
ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packagePrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "publish": NotRequired[AllowPublishType],
        "upstream": NotRequired[AllowUpstreamType],
    },
)
ListRepositoriesInDomainRequestRequestTypeDef = TypedDict(
    "ListRepositoriesInDomainRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "repositoryPrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "name": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "domainName": NotRequired[str],
        "domainOwner": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "createdTime": NotRequired[datetime],
    },
)
ListRepositoriesRequestRequestTypeDef = TypedDict(
    "ListRepositoriesRequestRequestTypeDef",
    {
        "repositoryPrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PackageOriginRestrictionsTypeDef = TypedDict(
    "PackageOriginRestrictionsTypeDef",
    {
        "publish": AllowPublishType,
        "upstream": AllowUpstreamType,
    },
)
PutDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "policyDocument": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)
PutRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "policyDocument": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)
RepositoryExternalConnectionInfoTypeDef = TypedDict(
    "RepositoryExternalConnectionInfoTypeDef",
    {
        "externalConnectionName": NotRequired[str],
        "packageFormat": NotRequired[PackageFormatType],
        "status": NotRequired[Literal["Available"]],
    },
)
UpstreamRepositoryInfoTypeDef = TypedDict(
    "UpstreamRepositoryInfoTypeDef",
    {
        "repositoryName": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdatePackageVersionsStatusRequestRequestTypeDef = TypedDict(
    "UpdatePackageVersionsStatusRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "targetStatus": PackageVersionStatusType,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)
GetAuthorizationTokenResultTypeDef = TypedDict(
    "GetAuthorizationTokenResultTypeDef",
    {
        "authorizationToken": str,
        "expiration": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPackageVersionAssetResultTypeDef = TypedDict(
    "GetPackageVersionAssetResultTypeDef",
    {
        "asset": StreamingBody,
        "assetName": str,
        "packageVersion": str,
        "packageVersionRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPackageVersionReadmeResultTypeDef = TypedDict(
    "GetPackageVersionReadmeResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryEndpointResultTypeDef = TypedDict(
    "GetRepositoryEndpointResultTypeDef",
    {
        "repositoryEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPackageVersionAssetsResultTypeDef = TypedDict(
    "ListPackageVersionAssetsResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "assets": List[AssetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishPackageVersionResultTypeDef = TypedDict(
    "PublishPackageVersionResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "status": PackageVersionStatusType,
        "asset": AssetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishPackageVersionRequestRequestTypeDef = TypedDict(
    "PublishPackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "assetContent": BlobTypeDef,
        "assetName": str,
        "assetSHA256": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "unfinished": NotRequired[bool],
    },
)
CopyPackageVersionsResultTypeDef = TypedDict(
    "CopyPackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePackageVersionsResultTypeDef = TypedDict(
    "DeletePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisposePackageVersionsResultTypeDef = TypedDict(
    "DisposePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePackageVersionsStatusResultTypeDef = TypedDict(
    "UpdatePackageVersionsStatusResultTypeDef",
    {
        "successfulVersions": Dict[str, SuccessfulPackageVersionInfoTypeDef],
        "failedVersions": Dict[str, PackageVersionErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "domain": str,
        "encryptionKey": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "domain": DomainDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "domain": DomainDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDomainResultTypeDef = TypedDict(
    "DescribeDomainResultTypeDef",
    {
        "domain": DomainDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryRequestRequestTypeDef = TypedDict(
    "CreateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "description": NotRequired[str],
        "upstreams": NotRequired[Sequence[UpstreamRepositoryTypeDef]],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UpdateRepositoryRequestRequestTypeDef = TypedDict(
    "UpdateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "description": NotRequired[str],
        "upstreams": NotRequired[Sequence[UpstreamRepositoryTypeDef]],
    },
)
DeleteDomainPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainPermissionsPolicyResultTypeDef = TypedDict(
    "GetDomainPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutDomainPermissionsPolicyResultTypeDef = TypedDict(
    "PutDomainPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PackageVersionOriginTypeDef = TypedDict(
    "PackageVersionOriginTypeDef",
    {
        "domainEntryPoint": NotRequired[DomainEntryPointTypeDef],
        "originType": NotRequired[PackageVersionOriginTypeType],
    },
)
ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "domains": List[DomainSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDomainsRequestListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsRequestListDomainsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef = TypedDict(
    "ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackageVersionsRequestListPackageVersionsPaginateTypeDef = TypedDict(
    "ListPackageVersionsRequestListPackageVersionsPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "sortBy": NotRequired[Literal["PUBLISHED_TIME"]],
        "originType": NotRequired[PackageVersionOriginTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagesRequestListPackagesPaginateTypeDef = TypedDict(
    "ListPackagesRequestListPackagesPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packagePrefix": NotRequired[str],
        "publish": NotRequired[AllowPublishType],
        "upstream": NotRequired[AllowUpstreamType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef = TypedDict(
    "ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "repositoryPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRepositoriesRequestListRepositoriesPaginateTypeDef = TypedDict(
    "ListRepositoriesRequestListRepositoriesPaginateTypeDef",
    {
        "repositoryPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackageVersionDependenciesResultTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "dependencies": List[PackageDependencyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositoriesInDomainResultTypeDef = TypedDict(
    "ListRepositoriesInDomainResultTypeDef",
    {
        "repositories": List[RepositorySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRepositoriesResultTypeDef = TypedDict(
    "ListRepositoriesResultTypeDef",
    {
        "repositories": List[RepositorySummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PackageOriginConfigurationTypeDef = TypedDict(
    "PackageOriginConfigurationTypeDef",
    {
        "restrictions": NotRequired[PackageOriginRestrictionsTypeDef],
    },
)
PutPackageOriginConfigurationRequestRequestTypeDef = TypedDict(
    "PutPackageOriginConfigurationRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "restrictions": PackageOriginRestrictionsTypeDef,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
RepositoryDescriptionTypeDef = TypedDict(
    "RepositoryDescriptionTypeDef",
    {
        "name": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "domainName": NotRequired[str],
        "domainOwner": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "upstreams": NotRequired[List[UpstreamRepositoryInfoTypeDef]],
        "externalConnections": NotRequired[List[RepositoryExternalConnectionInfoTypeDef]],
        "createdTime": NotRequired[datetime],
    },
)
PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packageName": NotRequired[str],
        "displayName": NotRequired[str],
        "version": NotRequired[str],
        "summary": NotRequired[str],
        "homePage": NotRequired[str],
        "sourceCodeRepository": NotRequired[str],
        "publishedTime": NotRequired[datetime],
        "licenses": NotRequired[List[LicenseInfoTypeDef]],
        "revision": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "origin": NotRequired[PackageVersionOriginTypeDef],
    },
)
PackageVersionSummaryTypeDef = TypedDict(
    "PackageVersionSummaryTypeDef",
    {
        "version": str,
        "status": PackageVersionStatusType,
        "revision": NotRequired[str],
        "origin": NotRequired[PackageVersionOriginTypeDef],
    },
)
PackageDescriptionTypeDef = TypedDict(
    "PackageDescriptionTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "name": NotRequired[str],
        "originConfiguration": NotRequired[PackageOriginConfigurationTypeDef],
    },
)
PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "package": NotRequired[str],
        "originConfiguration": NotRequired[PackageOriginConfigurationTypeDef],
    },
)
PutPackageOriginConfigurationResultTypeDef = TypedDict(
    "PutPackageOriginConfigurationResultTypeDef",
    {
        "originConfiguration": PackageOriginConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateExternalConnectionResultTypeDef = TypedDict(
    "AssociateExternalConnectionResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRepositoryResultTypeDef = TypedDict(
    "CreateRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteRepositoryResultTypeDef = TypedDict(
    "DeleteRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRepositoryResultTypeDef = TypedDict(
    "DescribeRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateExternalConnectionResultTypeDef = TypedDict(
    "DisassociateExternalConnectionResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRepositoryResultTypeDef = TypedDict(
    "UpdateRepositoryResultTypeDef",
    {
        "repository": RepositoryDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackageVersionResultTypeDef = TypedDict(
    "DescribePackageVersionResultTypeDef",
    {
        "packageVersion": PackageVersionDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPackageVersionsResultTypeDef = TypedDict(
    "ListPackageVersionsResultTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "versions": List[PackageVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePackageResultTypeDef = TypedDict(
    "DescribePackageResultTypeDef",
    {
        "package": PackageDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletePackageResultTypeDef = TypedDict(
    "DeletePackageResultTypeDef",
    {
        "deletedPackage": PackageSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPackagesResultTypeDef = TypedDict(
    "ListPackagesResultTypeDef",
    {
        "packages": List[PackageSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
