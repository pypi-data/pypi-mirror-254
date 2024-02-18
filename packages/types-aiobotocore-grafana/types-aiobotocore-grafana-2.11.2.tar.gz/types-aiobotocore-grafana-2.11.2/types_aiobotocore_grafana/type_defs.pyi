"""
Type annotations for grafana service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_grafana/type_defs/)

Usage::

    ```python
    from types_aiobotocore_grafana.type_defs import AssertionAttributesTypeDef

    data: AssertionAttributesTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    AccountAccessTypeType,
    AuthenticationProviderTypesType,
    DataSourceTypeType,
    LicenseTypeType,
    PermissionTypeType,
    RoleType,
    SamlConfigurationStatusType,
    UpdateActionType,
    UserTypeType,
    WorkspaceStatusType,
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
    "AssertionAttributesTypeDef",
    "AssociateLicenseRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AwsSsoAuthenticationTypeDef",
    "AuthenticationSummaryTypeDef",
    "CreateWorkspaceApiKeyRequestRequestTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "VpcConfigurationTypeDef",
    "DeleteWorkspaceApiKeyRequestRequestTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    "DescribeWorkspaceConfigurationRequestRequestTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DisassociateLicenseRequestRequestTypeDef",
    "IdpMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListVersionsRequestRequestTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "UserTypeDef",
    "RoleValuesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateWorkspaceConfigurationRequestRequestTypeDef",
    "CreateWorkspaceApiKeyResponseTypeDef",
    "DeleteWorkspaceApiKeyResponseTypeDef",
    "DescribeWorkspaceConfigurationResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVersionsResponseTypeDef",
    "WorkspaceSummaryTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "WorkspaceDescriptionTypeDef",
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    "ListVersionsRequestListVersionsPaginateTypeDef",
    "ListWorkspacesRequestListWorkspacesPaginateTypeDef",
    "PermissionEntryTypeDef",
    "UpdateInstructionTypeDef",
    "SamlConfigurationTypeDef",
    "ListWorkspacesResponseTypeDef",
    "AssociateLicenseResponseTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DisassociateLicenseResponseTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "ListPermissionsResponseTypeDef",
    "UpdateErrorTypeDef",
    "UpdatePermissionsRequestRequestTypeDef",
    "SamlAuthenticationTypeDef",
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    "UpdatePermissionsResponseTypeDef",
    "AuthenticationDescriptionTypeDef",
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    "UpdateWorkspaceAuthenticationResponseTypeDef",
)

AssertionAttributesTypeDef = TypedDict(
    "AssertionAttributesTypeDef",
    {
        "email": NotRequired[str],
        "groups": NotRequired[str],
        "login": NotRequired[str],
        "name": NotRequired[str],
        "org": NotRequired[str],
        "role": NotRequired[str],
    },
)
AssociateLicenseRequestRequestTypeDef = TypedDict(
    "AssociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
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
AwsSsoAuthenticationTypeDef = TypedDict(
    "AwsSsoAuthenticationTypeDef",
    {
        "ssoClientId": NotRequired[str],
    },
)
AuthenticationSummaryTypeDef = TypedDict(
    "AuthenticationSummaryTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
        "samlConfigurationStatus": NotRequired[SamlConfigurationStatusType],
    },
)
CreateWorkspaceApiKeyRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceApiKeyRequestRequestTypeDef",
    {
        "keyName": str,
        "keyRole": str,
        "secondsToLive": int,
        "workspaceId": str,
    },
)
NetworkAccessConfigurationTypeDef = TypedDict(
    "NetworkAccessConfigurationTypeDef",
    {
        "prefixListIds": List[str],
        "vpceIds": List[str],
    },
)
VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
)
DeleteWorkspaceApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceApiKeyRequestRequestTypeDef",
    {
        "keyName": str,
        "workspaceId": str,
    },
)
DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DescribeWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DescribeWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DescribeWorkspaceRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
DisassociateLicenseRequestRequestTypeDef = TypedDict(
    "DisassociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
    },
)
IdpMetadataTypeDef = TypedDict(
    "IdpMetadataTypeDef",
    {
        "url": NotRequired[str],
        "xml": NotRequired[str],
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
ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "workspaceId": str,
        "groupId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "userId": NotRequired[str],
        "userType": NotRequired[UserTypeType],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListVersionsRequestRequestTypeDef = TypedDict(
    "ListVersionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "workspaceId": NotRequired[str],
    },
)
ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "id": str,
        "type": UserTypeType,
    },
)
RoleValuesTypeDef = TypedDict(
    "RoleValuesTypeDef",
    {
        "admin": NotRequired[List[str]],
        "editor": NotRequired[List[str]],
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
UpdateWorkspaceConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceConfigurationRequestRequestTypeDef",
    {
        "configuration": str,
        "workspaceId": str,
        "grafanaVersion": NotRequired[str],
    },
)
CreateWorkspaceApiKeyResponseTypeDef = TypedDict(
    "CreateWorkspaceApiKeyResponseTypeDef",
    {
        "key": str,
        "keyName": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceApiKeyResponseTypeDef = TypedDict(
    "DeleteWorkspaceApiKeyResponseTypeDef",
    {
        "keyName": str,
        "workspaceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceConfigurationResponseTypeDef = TypedDict(
    "DescribeWorkspaceConfigurationResponseTypeDef",
    {
        "configuration": str,
        "grafanaVersion": str,
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
ListVersionsResponseTypeDef = TypedDict(
    "ListVersionsResponseTypeDef",
    {
        "grafanaVersions": List[str],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "authentication": AuthenticationSummaryTypeDef,
        "created": datetime,
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "description": NotRequired[str],
        "name": NotRequired[str],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "tags": NotRequired[Dict[str, str]],
    },
)
CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "accountAccessType": AccountAccessTypeType,
        "authenticationProviders": Sequence[AuthenticationProviderTypesType],
        "permissionType": PermissionTypeType,
        "clientToken": NotRequired[str],
        "configuration": NotRequired[str],
        "grafanaVersion": NotRequired[str],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationTypeDef],
        "organizationRoleName": NotRequired[str],
        "stackSetName": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "vpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "workspaceDataSources": NotRequired[Sequence[DataSourceTypeType]],
        "workspaceDescription": NotRequired[str],
        "workspaceName": NotRequired[str],
        "workspaceNotificationDestinations": NotRequired[Sequence[Literal["SNS"]]],
        "workspaceOrganizationalUnits": NotRequired[Sequence[str]],
        "workspaceRoleArn": NotRequired[str],
    },
)
UpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationTypeDef],
        "organizationRoleName": NotRequired[str],
        "permissionType": NotRequired[PermissionTypeType],
        "removeNetworkAccessConfiguration": NotRequired[bool],
        "removeVpcConfiguration": NotRequired[bool],
        "stackSetName": NotRequired[str],
        "vpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "workspaceDataSources": NotRequired[Sequence[DataSourceTypeType]],
        "workspaceDescription": NotRequired[str],
        "workspaceName": NotRequired[str],
        "workspaceNotificationDestinations": NotRequired[Sequence[Literal["SNS"]]],
        "workspaceOrganizationalUnits": NotRequired[Sequence[str]],
        "workspaceRoleArn": NotRequired[str],
    },
)
WorkspaceDescriptionTypeDef = TypedDict(
    "WorkspaceDescriptionTypeDef",
    {
        "authentication": AuthenticationSummaryTypeDef,
        "created": datetime,
        "dataSources": List[DataSourceTypeType],
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "description": NotRequired[str],
        "freeTrialConsumed": NotRequired[bool],
        "freeTrialExpiration": NotRequired[datetime],
        "licenseExpiration": NotRequired[datetime],
        "licenseType": NotRequired[LicenseTypeType],
        "name": NotRequired[str],
        "networkAccessControl": NotRequired[NetworkAccessConfigurationTypeDef],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "organizationRoleName": NotRequired[str],
        "organizationalUnits": NotRequired[List[str]],
        "permissionType": NotRequired[PermissionTypeType],
        "stackSetName": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "vpcConfiguration": NotRequired[VpcConfigurationTypeDef],
        "workspaceRoleArn": NotRequired[str],
    },
)
ListPermissionsRequestListPermissionsPaginateTypeDef = TypedDict(
    "ListPermissionsRequestListPermissionsPaginateTypeDef",
    {
        "workspaceId": str,
        "groupId": NotRequired[str],
        "userId": NotRequired[str],
        "userType": NotRequired[UserTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVersionsRequestListVersionsPaginateTypeDef = TypedDict(
    "ListVersionsRequestListVersionsPaginateTypeDef",
    {
        "workspaceId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListWorkspacesRequestListWorkspacesPaginateTypeDef = TypedDict(
    "ListWorkspacesRequestListWorkspacesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
PermissionEntryTypeDef = TypedDict(
    "PermissionEntryTypeDef",
    {
        "role": RoleType,
        "user": UserTypeDef,
    },
)
UpdateInstructionTypeDef = TypedDict(
    "UpdateInstructionTypeDef",
    {
        "action": UpdateActionType,
        "role": RoleType,
        "users": Sequence[UserTypeDef],
    },
)
SamlConfigurationTypeDef = TypedDict(
    "SamlConfigurationTypeDef",
    {
        "idpMetadata": IdpMetadataTypeDef,
        "allowedOrganizations": NotRequired[List[str]],
        "assertionAttributes": NotRequired[AssertionAttributesTypeDef],
        "loginValidityDuration": NotRequired[int],
        "roleValues": NotRequired[RoleValuesTypeDef],
    },
)
ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List[WorkspaceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssociateLicenseResponseTypeDef = TypedDict(
    "AssociateLicenseResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteWorkspaceResponseTypeDef = TypedDict(
    "DeleteWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DisassociateLicenseResponseTypeDef = TypedDict(
    "DisassociateLicenseResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "workspace": WorkspaceDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List[PermissionEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "causedBy": UpdateInstructionTypeDef,
        "code": int,
        "message": str,
    },
)
UpdatePermissionsRequestRequestTypeDef = TypedDict(
    "UpdatePermissionsRequestRequestTypeDef",
    {
        "updateInstructionBatch": Sequence[UpdateInstructionTypeDef],
        "workspaceId": str,
    },
)
SamlAuthenticationTypeDef = TypedDict(
    "SamlAuthenticationTypeDef",
    {
        "status": SamlConfigurationStatusType,
        "configuration": NotRequired[SamlConfigurationTypeDef],
    },
)
UpdateWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "authenticationProviders": Sequence[AuthenticationProviderTypesType],
        "workspaceId": str,
        "samlConfiguration": NotRequired[SamlConfigurationTypeDef],
    },
)
UpdatePermissionsResponseTypeDef = TypedDict(
    "UpdatePermissionsResponseTypeDef",
    {
        "errors": List[UpdateErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthenticationDescriptionTypeDef = TypedDict(
    "AuthenticationDescriptionTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
        "awsSso": NotRequired[AwsSsoAuthenticationTypeDef],
        "saml": NotRequired[SamlAuthenticationTypeDef],
    },
)
DescribeWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": AuthenticationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": AuthenticationDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
