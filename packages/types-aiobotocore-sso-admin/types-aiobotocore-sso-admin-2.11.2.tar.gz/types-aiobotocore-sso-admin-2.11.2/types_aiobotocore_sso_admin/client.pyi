"""
Type annotations for sso-admin service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_sso_admin.client import SSOAdminClient

    session = get_session()
    async with session.create_client("sso-admin") as client:
        client: SSOAdminClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    ApplicationStatusType,
    GrantTypeType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
)
from .paginator import (
    ListAccountAssignmentCreationStatusPaginator,
    ListAccountAssignmentDeletionStatusPaginator,
    ListAccountAssignmentsForPrincipalPaginator,
    ListAccountAssignmentsPaginator,
    ListAccountsForProvisionedPermissionSetPaginator,
    ListApplicationAccessScopesPaginator,
    ListApplicationAssignmentsForPrincipalPaginator,
    ListApplicationAssignmentsPaginator,
    ListApplicationAuthenticationMethodsPaginator,
    ListApplicationGrantsPaginator,
    ListApplicationProvidersPaginator,
    ListApplicationsPaginator,
    ListCustomerManagedPolicyReferencesInPermissionSetPaginator,
    ListInstancesPaginator,
    ListManagedPoliciesInPermissionSetPaginator,
    ListPermissionSetProvisioningStatusPaginator,
    ListPermissionSetsPaginator,
    ListPermissionSetsProvisionedToAccountPaginator,
    ListTagsForResourcePaginator,
    ListTrustedTokenIssuersPaginator,
)
from .type_defs import (
    AuthenticationMethodTypeDef,
    CreateAccountAssignmentResponseTypeDef,
    CreateApplicationResponseTypeDef,
    CreateInstanceResponseTypeDef,
    CreatePermissionSetResponseTypeDef,
    CreateTrustedTokenIssuerResponseTypeDef,
    CustomerManagedPolicyReferenceTypeDef,
    DeleteAccountAssignmentResponseTypeDef,
    DescribeAccountAssignmentCreationStatusResponseTypeDef,
    DescribeAccountAssignmentDeletionStatusResponseTypeDef,
    DescribeApplicationAssignmentResponseTypeDef,
    DescribeApplicationProviderResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef,
    DescribeInstanceResponseTypeDef,
    DescribePermissionSetProvisioningStatusResponseTypeDef,
    DescribePermissionSetResponseTypeDef,
    DescribeTrustedTokenIssuerResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetApplicationAccessScopeResponseTypeDef,
    GetApplicationAssignmentConfigurationResponseTypeDef,
    GetApplicationAuthenticationMethodResponseTypeDef,
    GetApplicationGrantResponseTypeDef,
    GetInlinePolicyForPermissionSetResponseTypeDef,
    GetPermissionsBoundaryForPermissionSetResponseTypeDef,
    GrantTypeDef,
    InstanceAccessControlAttributeConfigurationTypeDef,
    ListAccountAssignmentCreationStatusResponseTypeDef,
    ListAccountAssignmentDeletionStatusResponseTypeDef,
    ListAccountAssignmentsFilterTypeDef,
    ListAccountAssignmentsForPrincipalResponseTypeDef,
    ListAccountAssignmentsResponseTypeDef,
    ListAccountsForProvisionedPermissionSetResponseTypeDef,
    ListApplicationAccessScopesResponseTypeDef,
    ListApplicationAssignmentsFilterTypeDef,
    ListApplicationAssignmentsForPrincipalResponseTypeDef,
    ListApplicationAssignmentsResponseTypeDef,
    ListApplicationAuthenticationMethodsResponseTypeDef,
    ListApplicationGrantsResponseTypeDef,
    ListApplicationProvidersResponseTypeDef,
    ListApplicationsFilterTypeDef,
    ListApplicationsResponseTypeDef,
    ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListManagedPoliciesInPermissionSetResponseTypeDef,
    ListPermissionSetProvisioningStatusResponseTypeDef,
    ListPermissionSetsProvisionedToAccountResponseTypeDef,
    ListPermissionSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustedTokenIssuersResponseTypeDef,
    OperationStatusFilterTypeDef,
    PermissionsBoundaryTypeDef,
    PortalOptionsTypeDef,
    ProvisionPermissionSetResponseTypeDef,
    TagTypeDef,
    TrustedTokenIssuerConfigurationTypeDef,
    TrustedTokenIssuerUpdateConfigurationTypeDef,
    UpdateApplicationPortalOptionsTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SSOAdminClient",)

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

class SSOAdminClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOAdminClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#exceptions)
        """

    async def attach_customer_managed_policy_reference_to_permission_set(
        self,
        *,
        CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef,
        InstanceArn: str,
        PermissionSetArn: str,
    ) -> Dict[str, Any]:
        """
        Attaches the specified customer managed policy to the specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.attach_customer_managed_policy_reference_to_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#attach_customer_managed_policy_reference_to_permission_set)
        """

    async def attach_managed_policy_to_permission_set(
        self, *, InstanceArn: str, ManagedPolicyArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Attaches an Amazon Web Services managed policy ARN to a permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.attach_managed_policy_to_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#attach_managed_policy_to_permission_set)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#close)
        """

    async def create_account_assignment(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
    ) -> CreateAccountAssignmentResponseTypeDef:
        """
        Assigns access to a principal for a specified Amazon Web Services account using
        a specified permission
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_account_assignment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_account_assignment)
        """

    async def create_application(
        self,
        *,
        ApplicationProviderArn: str,
        InstanceArn: str,
        Name: str,
        ClientToken: str = ...,
        Description: str = ...,
        PortalOptions: PortalOptionsTypeDef = ...,
        Status: ApplicationStatusType = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an application in IAM Identity Center for the given application
        provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_application)
        """

    async def create_application_assignment(
        self, *, ApplicationArn: str, PrincipalId: str, PrincipalType: PrincipalTypeType
    ) -> Dict[str, Any]:
        """
        Grant application access to a user or group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_application_assignment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_application_assignment)
        """

    async def create_instance(
        self, *, ClientToken: str = ..., Name: str = ..., Tags: Sequence[TagTypeDef] = ...
    ) -> CreateInstanceResponseTypeDef:
        """
        Creates an instance of IAM Identity Center for a standalone Amazon Web Services
        account that is not managed by Organizations or a member Amazon Web Services
        account in an
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_instance)
        """

    async def create_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfigurationTypeDef,
        InstanceArn: str,
    ) -> Dict[str, Any]:
        """
        Enables the attributes-based access control (ABAC) feature for the specified
        IAM Identity Center
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_instance_access_control_attribute_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_instance_access_control_attribute_configuration)
        """

    async def create_permission_set(
        self,
        *,
        InstanceArn: str,
        Name: str,
        Description: str = ...,
        RelayState: str = ...,
        SessionDuration: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreatePermissionSetResponseTypeDef:
        """
        Creates a permission set within a specified IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_permission_set)
        """

    async def create_trusted_token_issuer(
        self,
        *,
        InstanceArn: str,
        Name: str,
        TrustedTokenIssuerConfiguration: TrustedTokenIssuerConfigurationTypeDef,
        TrustedTokenIssuerType: Literal["OIDC_JWT"],
        ClientToken: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> CreateTrustedTokenIssuerResponseTypeDef:
        """
        Creates a connection to a trusted token issuer in an instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.create_trusted_token_issuer)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#create_trusted_token_issuer)
        """

    async def delete_account_assignment(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
    ) -> DeleteAccountAssignmentResponseTypeDef:
        """
        Deletes a principal's access from a specified Amazon Web Services account using
        a specified permission
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_account_assignment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_account_assignment)
        """

    async def delete_application(self, *, ApplicationArn: str) -> Dict[str, Any]:
        """
        Deletes the association with the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_application)
        """

    async def delete_application_access_scope(
        self, *, ApplicationArn: str, Scope: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an IAM Identity Center access scope from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_access_scope)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_application_access_scope)
        """

    async def delete_application_assignment(
        self, *, ApplicationArn: str, PrincipalId: str, PrincipalType: PrincipalTypeType
    ) -> Dict[str, Any]:
        """
        Revoke application access to an application by deleting application assignments
        for a user or
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_assignment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_application_assignment)
        """

    async def delete_application_authentication_method(
        self, *, ApplicationArn: str, AuthenticationMethodType: Literal["IAM"]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an authentication method from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_authentication_method)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_application_authentication_method)
        """

    async def delete_application_grant(
        self, *, ApplicationArn: str, GrantType: GrantTypeType
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a grant from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_application_grant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_application_grant)
        """

    async def delete_inline_policy_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the inline policy from a specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_inline_policy_from_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_inline_policy_from_permission_set)
        """

    async def delete_instance(self, *, InstanceArn: str) -> Dict[str, Any]:
        """
        Deletes the instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_instance)
        """

    async def delete_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> Dict[str, Any]:
        """
        Disables the attributes-based access control (ABAC) feature for the specified
        IAM Identity Center instance and deletes all of the attribute mappings that
        have been
        configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance_access_control_attribute_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_instance_access_control_attribute_configuration)
        """

    async def delete_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_permission_set)
        """

    async def delete_permissions_boundary_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the permissions boundary from a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_permissions_boundary_from_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_permissions_boundary_from_permission_set)
        """

    async def delete_trusted_token_issuer(self, *, TrustedTokenIssuerArn: str) -> Dict[str, Any]:
        """
        Deletes a trusted token issuer configuration from an instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.delete_trusted_token_issuer)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#delete_trusted_token_issuer)
        """

    async def describe_account_assignment_creation_status(
        self, *, AccountAssignmentCreationRequestId: str, InstanceArn: str
    ) -> DescribeAccountAssignmentCreationStatusResponseTypeDef:
        """
        Describes the status of the assignment creation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_creation_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_account_assignment_creation_status)
        """

    async def describe_account_assignment_deletion_status(
        self, *, AccountAssignmentDeletionRequestId: str, InstanceArn: str
    ) -> DescribeAccountAssignmentDeletionStatusResponseTypeDef:
        """
        Describes the status of the assignment deletion request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_deletion_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_account_assignment_deletion_status)
        """

    async def describe_application(
        self, *, ApplicationArn: str
    ) -> DescribeApplicationResponseTypeDef:
        """
        Retrieves the details of an application associated with an instance of IAM
        Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_application)
        """

    async def describe_application_assignment(
        self, *, ApplicationArn: str, PrincipalId: str, PrincipalType: PrincipalTypeType
    ) -> DescribeApplicationAssignmentResponseTypeDef:
        """
        Retrieves a direct assignment of a user or group to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_application_assignment)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_application_assignment)
        """

    async def describe_application_provider(
        self, *, ApplicationProviderArn: str
    ) -> DescribeApplicationProviderResponseTypeDef:
        """
        Retrieves details about a provider that can be used to connect an Amazon Web
        Services managed application or customer managed application to IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_application_provider)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_application_provider)
        """

    async def describe_instance(self, *, InstanceArn: str) -> DescribeInstanceResponseTypeDef:
        """
        Returns the details of an instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_instance)
        """

    async def describe_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef:
        """
        Returns the list of IAM Identity Center identity store attributes that have
        been configured to work with attributes-based access control (ABAC) for the
        specified IAM Identity Center
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance_access_control_attribute_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_instance_access_control_attribute_configuration)
        """

    async def describe_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> DescribePermissionSetResponseTypeDef:
        """
        Gets the details of the permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_permission_set)
        """

    async def describe_permission_set_provisioning_status(
        self, *, InstanceArn: str, ProvisionPermissionSetRequestId: str
    ) -> DescribePermissionSetProvisioningStatusResponseTypeDef:
        """
        Describes the status for the given permission set provisioning request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set_provisioning_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_permission_set_provisioning_status)
        """

    async def describe_trusted_token_issuer(
        self, *, TrustedTokenIssuerArn: str
    ) -> DescribeTrustedTokenIssuerResponseTypeDef:
        """
        Retrieves details about a trusted token issuer configuration stored in an
        instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.describe_trusted_token_issuer)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#describe_trusted_token_issuer)
        """

    async def detach_customer_managed_policy_reference_from_permission_set(
        self,
        *,
        CustomerManagedPolicyReference: CustomerManagedPolicyReferenceTypeDef,
        InstanceArn: str,
        PermissionSetArn: str,
    ) -> Dict[str, Any]:
        """
        Detaches the specified customer managed policy from the specified
        PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.detach_customer_managed_policy_reference_from_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#detach_customer_managed_policy_reference_from_permission_set)
        """

    async def detach_managed_policy_from_permission_set(
        self, *, InstanceArn: str, ManagedPolicyArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Detaches the attached Amazon Web Services managed policy ARN from the specified
        permission
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.detach_managed_policy_from_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#detach_managed_policy_from_permission_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#generate_presigned_url)
        """

    async def get_application_access_scope(
        self, *, ApplicationArn: str, Scope: str
    ) -> GetApplicationAccessScopeResponseTypeDef:
        """
        Retrieves the authorized targets for an IAM Identity Center access scope for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_application_access_scope)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_application_access_scope)
        """

    async def get_application_assignment_configuration(
        self, *, ApplicationArn: str
    ) -> GetApplicationAssignmentConfigurationResponseTypeDef:
        """
        Retrieves the configuration of  PutApplicationAssignmentConfiguration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_application_assignment_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_application_assignment_configuration)
        """

    async def get_application_authentication_method(
        self, *, ApplicationArn: str, AuthenticationMethodType: Literal["IAM"]
    ) -> GetApplicationAuthenticationMethodResponseTypeDef:
        """
        Retrieves details about an authentication method used by an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_application_authentication_method)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_application_authentication_method)
        """

    async def get_application_grant(
        self, *, ApplicationArn: str, GrantType: GrantTypeType
    ) -> GetApplicationGrantResponseTypeDef:
        """
        Retrieves details about an application grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_application_grant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_application_grant)
        """

    async def get_inline_policy_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetInlinePolicyForPermissionSetResponseTypeDef:
        """
        Obtains the inline policy assigned to the permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_inline_policy_for_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_inline_policy_for_permission_set)
        """

    async def get_permissions_boundary_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetPermissionsBoundaryForPermissionSetResponseTypeDef:
        """
        Obtains the permissions boundary for a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_permissions_boundary_for_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_permissions_boundary_for_permission_set)
        """

    async def list_account_assignment_creation_status(
        self,
        *,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAccountAssignmentCreationStatusResponseTypeDef:
        """
        Lists the status of the Amazon Web Services account assignment creation
        requests for a specified IAM Identity Center
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_creation_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_account_assignment_creation_status)
        """

    async def list_account_assignment_deletion_status(
        self,
        *,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAccountAssignmentDeletionStatusResponseTypeDef:
        """
        Lists the status of the Amazon Web Services account assignment deletion
        requests for a specified IAM Identity Center
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_deletion_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_account_assignment_deletion_status)
        """

    async def list_account_assignments(
        self,
        *,
        AccountId: str,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAccountAssignmentsResponseTypeDef:
        """
        Lists the assignee of the specified Amazon Web Services account with the
        specified permission
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_account_assignments)
        """

    async def list_account_assignments_for_principal(
        self,
        *,
        InstanceArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        Filter: ListAccountAssignmentsFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListAccountAssignmentsForPrincipalResponseTypeDef:
        """
        Retrieves a list of the IAM Identity Center associated Amazon Web Services
        accounts that the principal has access
        to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments_for_principal)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_account_assignments_for_principal)
        """

    async def list_accounts_for_provisioned_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        ProvisioningStatus: ProvisioningStatusType = ...,
    ) -> ListAccountsForProvisionedPermissionSetResponseTypeDef:
        """
        Lists all the Amazon Web Services accounts where the specified permission set
        is
        provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_accounts_for_provisioned_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_accounts_for_provisioned_permission_set)
        """

    async def list_application_access_scopes(
        self, *, ApplicationArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListApplicationAccessScopesResponseTypeDef:
        """
        Lists the access scopes and authorized targets associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_application_access_scopes)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_application_access_scopes)
        """

    async def list_application_assignments(
        self, *, ApplicationArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListApplicationAssignmentsResponseTypeDef:
        """
        Lists Amazon Web Services account users that are assigned to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_application_assignments)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_application_assignments)
        """

    async def list_application_assignments_for_principal(
        self,
        *,
        InstanceArn: str,
        PrincipalId: str,
        PrincipalType: PrincipalTypeType,
        Filter: ListApplicationAssignmentsFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListApplicationAssignmentsForPrincipalResponseTypeDef:
        """
        Lists the applications to which a specified principal is assigned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_application_assignments_for_principal)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_application_assignments_for_principal)
        """

    async def list_application_authentication_methods(
        self, *, ApplicationArn: str, NextToken: str = ...
    ) -> ListApplicationAuthenticationMethodsResponseTypeDef:
        """
        Lists all of the authentication methods supported by the specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_application_authentication_methods)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_application_authentication_methods)
        """

    async def list_application_grants(
        self, *, ApplicationArn: str, NextToken: str = ...
    ) -> ListApplicationGrantsResponseTypeDef:
        """
        List the grants associated with an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_application_grants)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_application_grants)
        """

    async def list_application_providers(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListApplicationProvidersResponseTypeDef:
        """
        Lists the application providers configured in the IAM Identity Center identity
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_application_providers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_application_providers)
        """

    async def list_applications(
        self,
        *,
        InstanceArn: str,
        Filter: ListApplicationsFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists all applications associated with the instance of IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_applications)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_applications)
        """

    async def list_customer_managed_policy_references_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef:
        """
        Lists all customer managed policies attached to a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_customer_managed_policy_references_in_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_customer_managed_policy_references_in_permission_set)
        """

    async def list_instances(
        self, *, MaxResults: int = ..., NextToken: str = ...
    ) -> ListInstancesResponseTypeDef:
        """
        Lists the details of the organization and account instances of IAM Identity
        Center that were created in or visible to the account calling this
        API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_instances)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_instances)
        """

    async def list_managed_policies_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListManagedPoliciesInPermissionSetResponseTypeDef:
        """
        Lists the Amazon Web Services managed policy that is attached to a specified
        permission
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_managed_policies_in_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_managed_policies_in_permission_set)
        """

    async def list_permission_set_provisioning_status(
        self,
        *,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
    ) -> ListPermissionSetProvisioningStatusResponseTypeDef:
        """
        Lists the status of the permission set provisioning requests for a specified
        IAM Identity Center
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_set_provisioning_status)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_permission_set_provisioning_status)
        """

    async def list_permission_sets(
        self, *, InstanceArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListPermissionSetsResponseTypeDef:
        """
        Lists the  PermissionSets in an IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_permission_sets)
        """

    async def list_permission_sets_provisioned_to_account(
        self,
        *,
        AccountId: str,
        InstanceArn: str,
        MaxResults: int = ...,
        NextToken: str = ...,
        ProvisioningStatus: ProvisioningStatusType = ...,
    ) -> ListPermissionSetsProvisionedToAccountResponseTypeDef:
        """
        Lists all the permission sets that are provisioned to a specified Amazon Web
        Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets_provisioned_to_account)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_permission_sets_provisioned_to_account)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str, InstanceArn: str = ..., NextToken: str = ...
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are attached to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_tags_for_resource)
        """

    async def list_trusted_token_issuers(
        self, *, InstanceArn: str, MaxResults: int = ..., NextToken: str = ...
    ) -> ListTrustedTokenIssuersResponseTypeDef:
        """
        Lists all the trusted token issuers configured in an instance of IAM Identity
        Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.list_trusted_token_issuers)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#list_trusted_token_issuers)
        """

    async def provision_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        TargetType: ProvisionTargetTypeType,
        TargetId: str = ...,
    ) -> ProvisionPermissionSetResponseTypeDef:
        """
        The process by which a specified permission set is provisioned to the specified
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.provision_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#provision_permission_set)
        """

    async def put_application_access_scope(
        self, *, ApplicationArn: str, Scope: str, AuthorizedTargets: Sequence[str] = ...
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates the list of authorized targets for an IAM Identity Center
        access scope for an
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_application_access_scope)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#put_application_access_scope)
        """

    async def put_application_assignment_configuration(
        self, *, ApplicationArn: str, AssignmentRequired: bool
    ) -> Dict[str, Any]:
        """
        Configure how users gain access to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_application_assignment_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#put_application_assignment_configuration)
        """

    async def put_application_authentication_method(
        self,
        *,
        ApplicationArn: str,
        AuthenticationMethod: AuthenticationMethodTypeDef,
        AuthenticationMethodType: Literal["IAM"],
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates an authentication method for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_application_authentication_method)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#put_application_authentication_method)
        """

    async def put_application_grant(
        self, *, ApplicationArn: str, Grant: GrantTypeDef, GrantType: GrantTypeType
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a grant to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_application_grant)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#put_application_grant)
        """

    async def put_inline_policy_to_permission_set(
        self, *, InlinePolicy: str, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Attaches an inline policy to a permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_inline_policy_to_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#put_inline_policy_to_permission_set)
        """

    async def put_permissions_boundary_to_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PermissionsBoundary: PermissionsBoundaryTypeDef,
    ) -> Dict[str, Any]:
        """
        Attaches an Amazon Web Services managed or customer managed policy to the
        specified  PermissionSet as a permissions
        boundary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.put_permissions_boundary_to_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#put_permissions_boundary_to_permission_set)
        """

    async def tag_resource(
        self, *, ResourceArn: str, Tags: Sequence[TagTypeDef], InstanceArn: str = ...
    ) -> Dict[str, Any]:
        """
        Associates a set of tags with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#tag_resource)
        """

    async def untag_resource(
        self, *, ResourceArn: str, TagKeys: Sequence[str], InstanceArn: str = ...
    ) -> Dict[str, Any]:
        """
        Disassociates a set of tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#untag_resource)
        """

    async def update_application(
        self,
        *,
        ApplicationArn: str,
        Description: str = ...,
        Name: str = ...,
        PortalOptions: UpdateApplicationPortalOptionsTypeDef = ...,
        Status: ApplicationStatusType = ...,
    ) -> Dict[str, Any]:
        """
        Updates application properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_application)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#update_application)
        """

    async def update_instance(self, *, InstanceArn: str, Name: str) -> Dict[str, Any]:
        """
        Update the details for the instance of IAM Identity Center that is owned by the
        Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_instance)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#update_instance)
        """

    async def update_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceAccessControlAttributeConfiguration: InstanceAccessControlAttributeConfigurationTypeDef,
        InstanceArn: str,
    ) -> Dict[str, Any]:
        """
        Updates the IAM Identity Center identity store attributes that you can use with
        the IAM Identity Center instance for attributes-based access control
        (ABAC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_instance_access_control_attribute_configuration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#update_instance_access_control_attribute_configuration)
        """

    async def update_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        Description: str = ...,
        RelayState: str = ...,
        SessionDuration: str = ...,
    ) -> Dict[str, Any]:
        """
        Updates an existing permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_permission_set)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#update_permission_set)
        """

    async def update_trusted_token_issuer(
        self,
        *,
        TrustedTokenIssuerArn: str,
        Name: str = ...,
        TrustedTokenIssuerConfiguration: TrustedTokenIssuerUpdateConfigurationTypeDef = ...,
    ) -> Dict[str, Any]:
        """
        Updates the name of the trusted token issuer, or the path of a source attribute
        or destination attribute for a trusted token issuer
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.update_trusted_token_issuer)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#update_trusted_token_issuer)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_creation_status"]
    ) -> ListAccountAssignmentCreationStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_deletion_status"]
    ) -> ListAccountAssignmentDeletionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments"]
    ) -> ListAccountAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments_for_principal"]
    ) -> ListAccountAssignmentsForPrincipalPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_provisioned_permission_set"]
    ) -> ListAccountsForProvisionedPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_access_scopes"]
    ) -> ListApplicationAccessScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_assignments"]
    ) -> ListApplicationAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_assignments_for_principal"]
    ) -> ListApplicationAssignmentsForPrincipalPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_authentication_methods"]
    ) -> ListApplicationAuthenticationMethodsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_grants"]
    ) -> ListApplicationGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_providers"]
    ) -> ListApplicationProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_customer_managed_policy_references_in_permission_set"]
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_policies_in_permission_set"]
    ) -> ListManagedPoliciesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_set_provisioning_status"]
    ) -> ListPermissionSetProvisioningStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets"]
    ) -> ListPermissionSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets_provisioned_to_account"]
    ) -> ListPermissionSetsProvisionedToAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trusted_token_issuers"]
    ) -> ListTrustedTokenIssuersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/#get_paginator)
        """

    async def __aenter__(self) -> "SSOAdminClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin.html#SSOAdmin.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sso_admin/client/)
        """
