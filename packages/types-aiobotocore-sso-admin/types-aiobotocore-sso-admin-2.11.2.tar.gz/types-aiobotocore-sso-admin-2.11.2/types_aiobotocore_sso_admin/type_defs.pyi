"""
Type annotations for sso-admin service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/type_defs/)

Usage::

    ```python
    from types_aiobotocore_sso_admin.type_defs import AccessControlAttributeValueTypeDef

    data: AccessControlAttributeValueTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence

from .literals import (
    ApplicationStatusType,
    ApplicationVisibilityType,
    FederationProtocolType,
    GrantTypeType,
    InstanceAccessControlAttributeConfigurationStatusType,
    InstanceStatusType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
    SignInOriginType,
    StatusValuesType,
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
    "AccessControlAttributeValueTypeDef",
    "AccountAssignmentForPrincipalTypeDef",
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "ApplicationAssignmentForPrincipalTypeDef",
    "ApplicationAssignmentTypeDef",
    "DisplayDataTypeDef",
    "CustomerManagedPolicyReferenceTypeDef",
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    "AttachedManagedPolicyTypeDef",
    "IamAuthenticationMethodTypeDef",
    "AuthorizationCodeGrantTypeDef",
    "AuthorizedTokenIssuerTypeDef",
    "CreateAccountAssignmentRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateApplicationAssignmentRequestRequestTypeDef",
    "TagTypeDef",
    "PermissionSetTypeDef",
    "DeleteAccountAssignmentRequestRequestTypeDef",
    "DeleteApplicationAccessScopeRequestRequestTypeDef",
    "DeleteApplicationAssignmentRequestRequestTypeDef",
    "DeleteApplicationAuthenticationMethodRequestRequestTypeDef",
    "DeleteApplicationGrantRequestRequestTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeletePermissionSetRequestRequestTypeDef",
    "DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef",
    "DeleteTrustedTokenIssuerRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "DescribeApplicationAssignmentRequestRequestTypeDef",
    "DescribeApplicationProviderRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DescribeInstanceRequestRequestTypeDef",
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "DescribePermissionSetRequestRequestTypeDef",
    "DescribeTrustedTokenIssuerRequestRequestTypeDef",
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    "GetApplicationAccessScopeRequestRequestTypeDef",
    "GetApplicationAssignmentConfigurationRequestRequestTypeDef",
    "GetApplicationAuthenticationMethodRequestRequestTypeDef",
    "GetApplicationGrantRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    "GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef",
    "InstanceMetadataTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ListAccountAssignmentsFilterTypeDef",
    "ListAccountAssignmentsRequestRequestTypeDef",
    "ListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    "ListApplicationAccessScopesRequestRequestTypeDef",
    "ScopeDetailsTypeDef",
    "ListApplicationAssignmentsFilterTypeDef",
    "ListApplicationAssignmentsRequestRequestTypeDef",
    "ListApplicationAuthenticationMethodsRequestRequestTypeDef",
    "ListApplicationGrantsRequestRequestTypeDef",
    "ListApplicationProvidersRequestRequestTypeDef",
    "ListApplicationsFilterTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "ListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    "ListPermissionSetsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTrustedTokenIssuersRequestRequestTypeDef",
    "TrustedTokenIssuerMetadataTypeDef",
    "OidcJwtConfigurationTypeDef",
    "OidcJwtUpdateConfigurationTypeDef",
    "SignInOptionsTypeDef",
    "ProvisionPermissionSetRequestRequestTypeDef",
    "PutApplicationAccessScopeRequestRequestTypeDef",
    "PutApplicationAssignmentConfigurationRequestRequestTypeDef",
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    "ResourceServerScopeDetailsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateInstanceRequestRequestTypeDef",
    "UpdatePermissionSetRequestRequestTypeDef",
    "AccessControlAttributeTypeDef",
    "AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef",
    "DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef",
    "PermissionsBoundaryTypeDef",
    "AuthenticationMethodTypeDef",
    "JwtBearerGrantTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateTrustedTokenIssuerResponseTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    "DescribeApplicationAssignmentResponseTypeDef",
    "DescribeInstanceResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetApplicationAccessScopeResponseTypeDef",
    "GetApplicationAssignmentConfigurationResponseTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    "ListAccountAssignmentsForPrincipalResponseTypeDef",
    "ListAccountAssignmentsResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    "ListApplicationAssignmentsForPrincipalResponseTypeDef",
    "ListApplicationAssignmentsResponseTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    "ListPermissionSetsResponseTypeDef",
    "CreateInstanceRequestRequestTypeDef",
    "CreatePermissionSetRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "DescribePermissionSetResponseTypeDef",
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
    "ListInstancesResponseTypeDef",
    "ListAccountAssignmentCreationStatusRequestRequestTypeDef",
    "ListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "ListPermissionSetProvisioningStatusRequestRequestTypeDef",
    "ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateTypeDef",
    "ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateTypeDef",
    "ListAccountAssignmentsRequestListAccountAssignmentsPaginateTypeDef",
    "ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateTypeDef",
    "ListApplicationAccessScopesRequestListApplicationAccessScopesPaginateTypeDef",
    "ListApplicationAssignmentsRequestListApplicationAssignmentsPaginateTypeDef",
    "ListApplicationAuthenticationMethodsRequestListApplicationAuthenticationMethodsPaginateTypeDef",
    "ListApplicationGrantsRequestListApplicationGrantsPaginateTypeDef",
    "ListApplicationProvidersRequestListApplicationProvidersPaginateTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateTypeDef",
    "ListInstancesRequestListInstancesPaginateTypeDef",
    "ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateTypeDef",
    "ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateTypeDef",
    "ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateTypeDef",
    "ListPermissionSetsRequestListPermissionSetsPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "ListTrustedTokenIssuersRequestListTrustedTokenIssuersPaginateTypeDef",
    "ListAccountAssignmentsForPrincipalRequestListAccountAssignmentsForPrincipalPaginateTypeDef",
    "ListAccountAssignmentsForPrincipalRequestRequestTypeDef",
    "ListApplicationAccessScopesResponseTypeDef",
    "ListApplicationAssignmentsForPrincipalRequestListApplicationAssignmentsForPrincipalPaginateTypeDef",
    "ListApplicationAssignmentsForPrincipalRequestRequestTypeDef",
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    "ListTrustedTokenIssuersResponseTypeDef",
    "TrustedTokenIssuerConfigurationTypeDef",
    "TrustedTokenIssuerUpdateConfigurationTypeDef",
    "PortalOptionsTypeDef",
    "UpdateApplicationPortalOptionsTypeDef",
    "ResourceServerConfigTypeDef",
    "InstanceAccessControlAttributeConfigurationTypeDef",
    "GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    "PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef",
    "AuthenticationMethodItemTypeDef",
    "GetApplicationAuthenticationMethodResponseTypeDef",
    "PutApplicationAuthenticationMethodRequestRequestTypeDef",
    "GrantTypeDef",
    "CreateTrustedTokenIssuerRequestRequestTypeDef",
    "DescribeTrustedTokenIssuerResponseTypeDef",
    "UpdateTrustedTokenIssuerRequestRequestTypeDef",
    "ApplicationTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "ApplicationProviderTypeDef",
    "DescribeApplicationProviderResponseTypeDef",
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "ListApplicationAuthenticationMethodsResponseTypeDef",
    "GetApplicationGrantResponseTypeDef",
    "GrantItemTypeDef",
    "PutApplicationGrantRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListApplicationProvidersResponseTypeDef",
    "ListApplicationGrantsResponseTypeDef",
)

AccessControlAttributeValueTypeDef = TypedDict(
    "AccessControlAttributeValueTypeDef",
    {
        "Source": Sequence[str],
    },
)
AccountAssignmentForPrincipalTypeDef = TypedDict(
    "AccountAssignmentForPrincipalTypeDef",
    {
        "AccountId": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)
AccountAssignmentOperationStatusMetadataTypeDef = TypedDict(
    "AccountAssignmentOperationStatusMetadataTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "RequestId": NotRequired[str],
        "Status": NotRequired[StatusValuesType],
    },
)
AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
        "RequestId": NotRequired[str],
        "Status": NotRequired[StatusValuesType],
        "TargetId": NotRequired[str],
        "TargetType": NotRequired[Literal["AWS_ACCOUNT"]],
    },
)
AccountAssignmentTypeDef = TypedDict(
    "AccountAssignmentTypeDef",
    {
        "AccountId": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)
ApplicationAssignmentForPrincipalTypeDef = TypedDict(
    "ApplicationAssignmentForPrincipalTypeDef",
    {
        "ApplicationArn": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)
ApplicationAssignmentTypeDef = TypedDict(
    "ApplicationAssignmentTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)
DisplayDataTypeDef = TypedDict(
    "DisplayDataTypeDef",
    {
        "Description": NotRequired[str],
        "DisplayName": NotRequired[str],
        "IconUrl": NotRequired[str],
    },
)
CustomerManagedPolicyReferenceTypeDef = TypedDict(
    "CustomerManagedPolicyReferenceTypeDef",
    {
        "Name": str,
        "Path": NotRequired[str],
    },
)
AttachManagedPolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ManagedPolicyArn": str,
        "PermissionSetArn": str,
    },
)
AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)
IamAuthenticationMethodTypeDef = TypedDict(
    "IamAuthenticationMethodTypeDef",
    {
        "ActorPolicy": Dict[str, Any],
    },
)
AuthorizationCodeGrantTypeDef = TypedDict(
    "AuthorizationCodeGrantTypeDef",
    {
        "RedirectUris": NotRequired[List[str]],
    },
)
AuthorizedTokenIssuerTypeDef = TypedDict(
    "AuthorizedTokenIssuerTypeDef",
    {
        "AuthorizedAudiences": NotRequired[List[str]],
        "TrustedTokenIssuerArn": NotRequired[str],
    },
)
CreateAccountAssignmentRequestRequestTypeDef = TypedDict(
    "CreateAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
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
CreateApplicationAssignmentRequestRequestTypeDef = TypedDict(
    "CreateApplicationAssignmentRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PermissionSetTypeDef = TypedDict(
    "PermissionSetTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "RelayState": NotRequired[str],
        "SessionDuration": NotRequired[str],
    },
)
DeleteAccountAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
)
DeleteApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "DeleteApplicationAccessScopeRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Scope": str,
    },
)
DeleteApplicationAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteApplicationAssignmentRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)
DeleteApplicationAuthenticationMethodRequestRequestTypeDef = TypedDict(
    "DeleteApplicationAuthenticationMethodRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AuthenticationMethodType": Literal["IAM"],
    },
)
DeleteApplicationGrantRequestRequestTypeDef = TypedDict(
    "DeleteApplicationGrantRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "GrantType": GrantTypeType,
    },
)
DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
DeleteInstanceRequestRequestTypeDef = TypedDict(
    "DeleteInstanceRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
DeletePermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
DeleteTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "DeleteTrustedTokenIssuerRequestRequestTypeDef",
    {
        "TrustedTokenIssuerArn": str,
    },
)
DescribeAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "AccountAssignmentCreationRequestId": str,
        "InstanceArn": str,
    },
)
DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "AccountAssignmentDeletionRequestId": str,
        "InstanceArn": str,
    },
)
DescribeApplicationAssignmentRequestRequestTypeDef = TypedDict(
    "DescribeApplicationAssignmentRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
)
DescribeApplicationProviderRequestRequestTypeDef = TypedDict(
    "DescribeApplicationProviderRequestRequestTypeDef",
    {
        "ApplicationProviderArn": str,
    },
)
DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
DescribeInstanceRequestRequestTypeDef = TypedDict(
    "DescribeInstanceRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
DescribePermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ProvisionPermissionSetRequestId": str,
    },
)
PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "AccountId": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "FailureReason": NotRequired[str],
        "PermissionSetArn": NotRequired[str],
        "RequestId": NotRequired[str],
        "Status": NotRequired[StatusValuesType],
    },
)
DescribePermissionSetRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
DescribeTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "DescribeTrustedTokenIssuerRequestRequestTypeDef",
    {
        "TrustedTokenIssuerArn": str,
    },
)
DetachManagedPolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ManagedPolicyArn": str,
        "PermissionSetArn": str,
    },
)
GetApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "GetApplicationAccessScopeRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Scope": str,
    },
)
GetApplicationAssignmentConfigurationRequestRequestTypeDef = TypedDict(
    "GetApplicationAssignmentConfigurationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
    },
)
GetApplicationAuthenticationMethodRequestRequestTypeDef = TypedDict(
    "GetApplicationAuthenticationMethodRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AuthenticationMethodType": Literal["IAM"],
    },
)
GetApplicationGrantRequestRequestTypeDef = TypedDict(
    "GetApplicationGrantRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "GrantType": GrantTypeType,
    },
)
GetInlinePolicyForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "IdentityStoreId": NotRequired[str],
        "InstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "Status": NotRequired[InstanceStatusType],
    },
)
OperationStatusFilterTypeDef = TypedDict(
    "OperationStatusFilterTypeDef",
    {
        "Status": NotRequired[StatusValuesType],
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
ListAccountAssignmentsFilterTypeDef = TypedDict(
    "ListAccountAssignmentsFilterTypeDef",
    {
        "AccountId": NotRequired[str],
    },
)
ListAccountAssignmentsRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentsRequestRequestTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAccountsForProvisionedPermissionSetRequestRequestTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProvisioningStatus": NotRequired[ProvisioningStatusType],
    },
)
ListApplicationAccessScopesRequestRequestTypeDef = TypedDict(
    "ListApplicationAccessScopesRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ScopeDetailsTypeDef = TypedDict(
    "ScopeDetailsTypeDef",
    {
        "Scope": str,
        "AuthorizedTargets": NotRequired[List[str]],
    },
)
ListApplicationAssignmentsFilterTypeDef = TypedDict(
    "ListApplicationAssignmentsFilterTypeDef",
    {
        "ApplicationArn": NotRequired[str],
    },
)
ListApplicationAssignmentsRequestRequestTypeDef = TypedDict(
    "ListApplicationAssignmentsRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListApplicationAuthenticationMethodsRequestRequestTypeDef = TypedDict(
    "ListApplicationAuthenticationMethodsRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "NextToken": NotRequired[str],
    },
)
ListApplicationGrantsRequestRequestTypeDef = TypedDict(
    "ListApplicationGrantsRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "NextToken": NotRequired[str],
    },
)
ListApplicationProvidersRequestRequestTypeDef = TypedDict(
    "ListApplicationProvidersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListApplicationsFilterTypeDef = TypedDict(
    "ListApplicationsFilterTypeDef",
    {
        "ApplicationAccount": NotRequired[str],
        "ApplicationProvider": NotRequired[str],
    },
)
ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef = TypedDict(
    "ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListManagedPoliciesInPermissionSetRequestRequestTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
PermissionSetProvisioningStatusMetadataTypeDef = TypedDict(
    "PermissionSetProvisioningStatusMetadataTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "RequestId": NotRequired[str],
        "Status": NotRequired[StatusValuesType],
    },
)
ListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProvisioningStatus": NotRequired[ProvisioningStatusType],
    },
)
ListPermissionSetsRequestRequestTypeDef = TypedDict(
    "ListPermissionSetsRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "InstanceArn": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListTrustedTokenIssuersRequestRequestTypeDef = TypedDict(
    "ListTrustedTokenIssuersRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TrustedTokenIssuerMetadataTypeDef = TypedDict(
    "TrustedTokenIssuerMetadataTypeDef",
    {
        "Name": NotRequired[str],
        "TrustedTokenIssuerArn": NotRequired[str],
        "TrustedTokenIssuerType": NotRequired[Literal["OIDC_JWT"]],
    },
)
OidcJwtConfigurationTypeDef = TypedDict(
    "OidcJwtConfigurationTypeDef",
    {
        "ClaimAttributePath": str,
        "IdentityStoreAttributePath": str,
        "IssuerUrl": str,
        "JwksRetrievalOption": Literal["OPEN_ID_DISCOVERY"],
    },
)
OidcJwtUpdateConfigurationTypeDef = TypedDict(
    "OidcJwtUpdateConfigurationTypeDef",
    {
        "ClaimAttributePath": NotRequired[str],
        "IdentityStoreAttributePath": NotRequired[str],
        "JwksRetrievalOption": NotRequired[Literal["OPEN_ID_DISCOVERY"]],
    },
)
SignInOptionsTypeDef = TypedDict(
    "SignInOptionsTypeDef",
    {
        "Origin": SignInOriginType,
        "ApplicationUrl": NotRequired[str],
    },
)
ProvisionPermissionSetRequestRequestTypeDef = TypedDict(
    "ProvisionPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "TargetType": ProvisionTargetTypeType,
        "TargetId": NotRequired[str],
    },
)
PutApplicationAccessScopeRequestRequestTypeDef = TypedDict(
    "PutApplicationAccessScopeRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Scope": str,
        "AuthorizedTargets": NotRequired[Sequence[str]],
    },
)
PutApplicationAssignmentConfigurationRequestRequestTypeDef = TypedDict(
    "PutApplicationAssignmentConfigurationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AssignmentRequired": bool,
    },
)
PutInlinePolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    {
        "InlinePolicy": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
ResourceServerScopeDetailsTypeDef = TypedDict(
    "ResourceServerScopeDetailsTypeDef",
    {
        "DetailedTitle": NotRequired[str],
        "LongDescription": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
        "InstanceArn": NotRequired[str],
    },
)
UpdateInstanceRequestRequestTypeDef = TypedDict(
    "UpdateInstanceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
    },
)
UpdatePermissionSetRequestRequestTypeDef = TypedDict(
    "UpdatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "Description": NotRequired[str],
        "RelayState": NotRequired[str],
        "SessionDuration": NotRequired[str],
    },
)
AccessControlAttributeTypeDef = TypedDict(
    "AccessControlAttributeTypeDef",
    {
        "Key": str,
        "Value": AccessControlAttributeValueTypeDef,
    },
)
AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef",
    {
        "CustomerManagedPolicyReference": CustomerManagedPolicyReferenceTypeDef,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef",
    {
        "CustomerManagedPolicyReference": CustomerManagedPolicyReferenceTypeDef,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
PermissionsBoundaryTypeDef = TypedDict(
    "PermissionsBoundaryTypeDef",
    {
        "CustomerManagedPolicyReference": NotRequired[CustomerManagedPolicyReferenceTypeDef],
        "ManagedPolicyArn": NotRequired[str],
    },
)
AuthenticationMethodTypeDef = TypedDict(
    "AuthenticationMethodTypeDef",
    {
        "Iam": NotRequired[IamAuthenticationMethodTypeDef],
    },
)
JwtBearerGrantTypeDef = TypedDict(
    "JwtBearerGrantTypeDef",
    {
        "AuthorizedTokenIssuers": NotRequired[List[AuthorizedTokenIssuerTypeDef]],
    },
)
CreateAccountAssignmentResponseTypeDef = TypedDict(
    "CreateAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": AccountAssignmentOperationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef",
    {
        "InstanceArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateTrustedTokenIssuerResponseTypeDef = TypedDict(
    "CreateTrustedTokenIssuerResponseTypeDef",
    {
        "TrustedTokenIssuerArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteAccountAssignmentResponseTypeDef = TypedDict(
    "DeleteAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": AccountAssignmentOperationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": AccountAssignmentOperationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": AccountAssignmentOperationStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeApplicationAssignmentResponseTypeDef = TypedDict(
    "DescribeApplicationAssignmentResponseTypeDef",
    {
        "ApplicationArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef",
    {
        "CreatedDate": datetime,
        "IdentityStoreId": str,
        "InstanceArn": str,
        "Name": str,
        "OwnerAccountId": str,
        "Status": InstanceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationAccessScopeResponseTypeDef = TypedDict(
    "GetApplicationAccessScopeResponseTypeDef",
    {
        "AuthorizedTargets": List[str],
        "Scope": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationAssignmentConfigurationResponseTypeDef = TypedDict(
    "GetApplicationAssignmentConfigurationResponseTypeDef",
    {
        "AssignmentRequired": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInlinePolicyForPermissionSetResponseTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    {
        "InlinePolicy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentsCreationStatus": List[AccountAssignmentOperationStatusMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentsDeletionStatus": List[AccountAssignmentOperationStatusMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAssignmentsForPrincipalResponseTypeDef = TypedDict(
    "ListAccountAssignmentsForPrincipalResponseTypeDef",
    {
        "AccountAssignments": List[AccountAssignmentForPrincipalTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAssignmentsResponseTypeDef = TypedDict(
    "ListAccountAssignmentsResponseTypeDef",
    {
        "AccountAssignments": List[AccountAssignmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountsForProvisionedPermissionSetResponseTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    {
        "AccountIds": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationAssignmentsForPrincipalResponseTypeDef = TypedDict(
    "ListApplicationAssignmentsForPrincipalResponseTypeDef",
    {
        "ApplicationAssignments": List[ApplicationAssignmentForPrincipalTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationAssignmentsResponseTypeDef = TypedDict(
    "ListApplicationAssignmentsResponseTypeDef",
    {
        "ApplicationAssignments": List[ApplicationAssignmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef = TypedDict(
    "ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    {
        "CustomerManagedPolicyReferences": List[CustomerManagedPolicyReferenceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListManagedPoliciesInPermissionSetResponseTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    {
        "AttachedManagedPolicies": List[AttachedManagedPolicyTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionSetsProvisionedToAccountResponseTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPermissionSetsResponseTypeDef = TypedDict(
    "ListPermissionSetsResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceRequestRequestTypeDef = TypedDict(
    "CreateInstanceRequestRequestTypeDef",
    {
        "ClientToken": NotRequired[str],
        "Name": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePermissionSetRequestRequestTypeDef = TypedDict(
    "CreatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
        "Description": NotRequired[str],
        "RelayState": NotRequired[str],
        "SessionDuration": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
        "InstanceArn": NotRequired[str],
    },
)
CreatePermissionSetResponseTypeDef = TypedDict(
    "CreatePermissionSetResponseTypeDef",
    {
        "PermissionSet": PermissionSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePermissionSetResponseTypeDef = TypedDict(
    "DescribePermissionSetResponseTypeDef",
    {
        "PermissionSet": PermissionSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": PermissionSetProvisioningStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProvisionPermissionSetResponseTypeDef = TypedDict(
    "ProvisionPermissionSetResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": PermissionSetProvisioningStatusTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List[InstanceMetadataTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[OperationStatusFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[OperationStatusFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[OperationStatusFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[OperationStatusFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[OperationStatusFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountAssignmentsRequestListAccountAssignmentsPaginateTypeDef = TypedDict(
    "ListAccountAssignmentsRequestListAccountAssignmentsPaginateTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ProvisioningStatus": NotRequired[ProvisioningStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationAccessScopesRequestListApplicationAccessScopesPaginateTypeDef = TypedDict(
    "ListApplicationAccessScopesRequestListApplicationAccessScopesPaginateTypeDef",
    {
        "ApplicationArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationAssignmentsRequestListApplicationAssignmentsPaginateTypeDef = TypedDict(
    "ListApplicationAssignmentsRequestListApplicationAssignmentsPaginateTypeDef",
    {
        "ApplicationArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationAuthenticationMethodsRequestListApplicationAuthenticationMethodsPaginateTypeDef = TypedDict(
    "ListApplicationAuthenticationMethodsRequestListApplicationAuthenticationMethodsPaginateTypeDef",
    {
        "ApplicationArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationGrantsRequestListApplicationGrantsPaginateTypeDef = TypedDict(
    "ListApplicationGrantsRequestListApplicationGrantsPaginateTypeDef",
    {
        "ApplicationArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationProvidersRequestListApplicationProvidersPaginateTypeDef = TypedDict(
    "ListApplicationProvidersRequestListApplicationProvidersPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateTypeDef = TypedDict(
    "ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstancesRequestListInstancesPaginateTypeDef = TypedDict(
    "ListInstancesRequestListInstancesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[OperationStatusFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
        "ProvisioningStatus": NotRequired[ProvisioningStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPermissionSetsRequestListPermissionSetsPaginateTypeDef = TypedDict(
    "ListPermissionSetsRequestListPermissionSetsPaginateTypeDef",
    {
        "InstanceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceArn": str,
        "InstanceArn": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTrustedTokenIssuersRequestListTrustedTokenIssuersPaginateTypeDef = TypedDict(
    "ListTrustedTokenIssuersRequestListTrustedTokenIssuersPaginateTypeDef",
    {
        "InstanceArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountAssignmentsForPrincipalRequestListAccountAssignmentsForPrincipalPaginateTypeDef = TypedDict(
    "ListAccountAssignmentsForPrincipalRequestListAccountAssignmentsForPrincipalPaginateTypeDef",
    {
        "InstanceArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "Filter": NotRequired[ListAccountAssignmentsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountAssignmentsForPrincipalRequestRequestTypeDef = TypedDict(
    "ListAccountAssignmentsForPrincipalRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "Filter": NotRequired[ListAccountAssignmentsFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListApplicationAccessScopesResponseTypeDef = TypedDict(
    "ListApplicationAccessScopesResponseTypeDef",
    {
        "NextToken": str,
        "Scopes": List[ScopeDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationAssignmentsForPrincipalRequestListApplicationAssignmentsForPrincipalPaginateTypeDef = TypedDict(
    "ListApplicationAssignmentsForPrincipalRequestListApplicationAssignmentsForPrincipalPaginateTypeDef",
    {
        "InstanceArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "Filter": NotRequired[ListApplicationAssignmentsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationAssignmentsForPrincipalRequestRequestTypeDef = TypedDict(
    "ListApplicationAssignmentsForPrincipalRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "Filter": NotRequired[ListApplicationAssignmentsFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListApplicationsRequestListApplicationsPaginateTypeDef = TypedDict(
    "ListApplicationsRequestListApplicationsPaginateTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[ListApplicationsFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Filter": NotRequired[ListApplicationsFilterTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListPermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSetsProvisioningStatus": List[PermissionSetProvisioningStatusMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTrustedTokenIssuersResponseTypeDef = TypedDict(
    "ListTrustedTokenIssuersResponseTypeDef",
    {
        "NextToken": str,
        "TrustedTokenIssuers": List[TrustedTokenIssuerMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TrustedTokenIssuerConfigurationTypeDef = TypedDict(
    "TrustedTokenIssuerConfigurationTypeDef",
    {
        "OidcJwtConfiguration": NotRequired[OidcJwtConfigurationTypeDef],
    },
)
TrustedTokenIssuerUpdateConfigurationTypeDef = TypedDict(
    "TrustedTokenIssuerUpdateConfigurationTypeDef",
    {
        "OidcJwtConfiguration": NotRequired[OidcJwtUpdateConfigurationTypeDef],
    },
)
PortalOptionsTypeDef = TypedDict(
    "PortalOptionsTypeDef",
    {
        "SignInOptions": NotRequired[SignInOptionsTypeDef],
        "Visibility": NotRequired[ApplicationVisibilityType],
    },
)
UpdateApplicationPortalOptionsTypeDef = TypedDict(
    "UpdateApplicationPortalOptionsTypeDef",
    {
        "SignInOptions": NotRequired[SignInOptionsTypeDef],
    },
)
ResourceServerConfigTypeDef = TypedDict(
    "ResourceServerConfigTypeDef",
    {
        "Scopes": NotRequired[Dict[str, ResourceServerScopeDetailsTypeDef]],
    },
)
InstanceAccessControlAttributeConfigurationTypeDef = TypedDict(
    "InstanceAccessControlAttributeConfigurationTypeDef",
    {
        "AccessControlAttributes": Sequence[AccessControlAttributeTypeDef],
    },
)
GetPermissionsBoundaryForPermissionSetResponseTypeDef = TypedDict(
    "GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    {
        "PermissionsBoundary": PermissionsBoundaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PermissionsBoundary": PermissionsBoundaryTypeDef,
    },
)
AuthenticationMethodItemTypeDef = TypedDict(
    "AuthenticationMethodItemTypeDef",
    {
        "AuthenticationMethod": NotRequired[AuthenticationMethodTypeDef],
        "AuthenticationMethodType": NotRequired[Literal["IAM"]],
    },
)
GetApplicationAuthenticationMethodResponseTypeDef = TypedDict(
    "GetApplicationAuthenticationMethodResponseTypeDef",
    {
        "AuthenticationMethod": AuthenticationMethodTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutApplicationAuthenticationMethodRequestRequestTypeDef = TypedDict(
    "PutApplicationAuthenticationMethodRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "AuthenticationMethod": AuthenticationMethodTypeDef,
        "AuthenticationMethodType": Literal["IAM"],
    },
)
GrantTypeDef = TypedDict(
    "GrantTypeDef",
    {
        "AuthorizationCode": NotRequired[AuthorizationCodeGrantTypeDef],
        "JwtBearer": NotRequired[JwtBearerGrantTypeDef],
        "RefreshToken": NotRequired[Dict[str, Any]],
        "TokenExchange": NotRequired[Dict[str, Any]],
    },
)
CreateTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "CreateTrustedTokenIssuerRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
        "TrustedTokenIssuerConfiguration": TrustedTokenIssuerConfigurationTypeDef,
        "TrustedTokenIssuerType": Literal["OIDC_JWT"],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeTrustedTokenIssuerResponseTypeDef = TypedDict(
    "DescribeTrustedTokenIssuerResponseTypeDef",
    {
        "Name": str,
        "TrustedTokenIssuerArn": str,
        "TrustedTokenIssuerConfiguration": TrustedTokenIssuerConfigurationTypeDef,
        "TrustedTokenIssuerType": Literal["OIDC_JWT"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTrustedTokenIssuerRequestRequestTypeDef = TypedDict(
    "UpdateTrustedTokenIssuerRequestRequestTypeDef",
    {
        "TrustedTokenIssuerArn": str,
        "Name": NotRequired[str],
        "TrustedTokenIssuerConfiguration": NotRequired[
            TrustedTokenIssuerUpdateConfigurationTypeDef
        ],
    },
)
ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "ApplicationAccount": NotRequired[str],
        "ApplicationArn": NotRequired[str],
        "ApplicationProviderArn": NotRequired[str],
        "CreatedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "InstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "PortalOptions": NotRequired[PortalOptionsTypeDef],
        "Status": NotRequired[ApplicationStatusType],
    },
)
CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ApplicationProviderArn": str,
        "InstanceArn": str,
        "Name": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "PortalOptions": NotRequired[PortalOptionsTypeDef],
        "Status": NotRequired[ApplicationStatusType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationAccount": str,
        "ApplicationArn": str,
        "ApplicationProviderArn": str,
        "CreatedDate": datetime,
        "Description": str,
        "InstanceArn": str,
        "Name": str,
        "PortalOptions": PortalOptionsTypeDef,
        "Status": ApplicationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "PortalOptions": NotRequired[UpdateApplicationPortalOptionsTypeDef],
        "Status": NotRequired[ApplicationStatusType],
    },
)
ApplicationProviderTypeDef = TypedDict(
    "ApplicationProviderTypeDef",
    {
        "ApplicationProviderArn": str,
        "DisplayData": NotRequired[DisplayDataTypeDef],
        "FederationProtocol": NotRequired[FederationProtocolType],
        "ResourceServerConfig": NotRequired[ResourceServerConfigTypeDef],
    },
)
DescribeApplicationProviderResponseTypeDef = TypedDict(
    "DescribeApplicationProviderResponseTypeDef",
    {
        "ApplicationProviderArn": str,
        "DisplayData": DisplayDataTypeDef,
        "FederationProtocol": FederationProtocolType,
        "ResourceServerConfig": ResourceServerConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": InstanceAccessControlAttributeConfigurationTypeDef,
        "InstanceArn": str,
    },
)
DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": InstanceAccessControlAttributeConfigurationTypeDef,
        "Status": InstanceAccessControlAttributeConfigurationStatusType,
        "StatusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": InstanceAccessControlAttributeConfigurationTypeDef,
        "InstanceArn": str,
    },
)
ListApplicationAuthenticationMethodsResponseTypeDef = TypedDict(
    "ListApplicationAuthenticationMethodsResponseTypeDef",
    {
        "AuthenticationMethods": List[AuthenticationMethodItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApplicationGrantResponseTypeDef = TypedDict(
    "GetApplicationGrantResponseTypeDef",
    {
        "Grant": GrantTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GrantItemTypeDef = TypedDict(
    "GrantItemTypeDef",
    {
        "Grant": GrantTypeDef,
        "GrantType": GrantTypeType,
    },
)
PutApplicationGrantRequestRequestTypeDef = TypedDict(
    "PutApplicationGrantRequestRequestTypeDef",
    {
        "ApplicationArn": str,
        "Grant": GrantTypeDef,
        "GrantType": GrantTypeType,
    },
)
ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "Applications": List[ApplicationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationProvidersResponseTypeDef = TypedDict(
    "ListApplicationProvidersResponseTypeDef",
    {
        "ApplicationProviders": List[ApplicationProviderTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListApplicationGrantsResponseTypeDef = TypedDict(
    "ListApplicationGrantsResponseTypeDef",
    {
        "Grants": List[GrantItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
