"""
Type annotations for workmail service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmail/type_defs/)

Usage::

    ```python
    from types_aiobotocore_workmail.type_defs import AccessControlRuleTypeDef

    data: AccessControlRuleTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AccessControlRuleEffectType,
    AccessEffectType,
    AvailabilityProviderTypeType,
    DnsRecordVerificationStatusType,
    EntityStateType,
    EntityTypeType,
    FolderNameType,
    ImpersonationRoleTypeType,
    MailboxExportJobStateType,
    MemberTypeType,
    MobileDeviceAccessRuleEffectType,
    PermissionTypeType,
    ResourceTypeType,
    RetentionActionType,
    UserRoleType,
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
    "AccessControlRuleTypeDef",
    "AssociateDelegateToResourceRequestRequestTypeDef",
    "AssociateMemberToGroupRequestRequestTypeDef",
    "AssumeImpersonationRoleRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "LambdaAvailabilityProviderTypeDef",
    "RedactedEwsAvailabilityProviderTypeDef",
    "BookingOptionsTypeDef",
    "CancelMailboxExportJobRequestRequestTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "EwsAvailabilityProviderTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "ImpersonationRuleTypeDef",
    "CreateMobileDeviceAccessRuleRequestRequestTypeDef",
    "DomainTypeDef",
    "CreateResourceRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DelegateTypeDef",
    "DeleteAccessControlRuleRequestRequestTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteAvailabilityConfigurationRequestRequestTypeDef",
    "DeleteEmailMonitoringConfigurationRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteImpersonationRoleRequestRequestTypeDef",
    "DeleteMailboxPermissionsRequestRequestTypeDef",
    "DeleteMobileDeviceAccessOverrideRequestRequestTypeDef",
    "DeleteMobileDeviceAccessRuleRequestRequestTypeDef",
    "DeleteOrganizationRequestRequestTypeDef",
    "DeleteResourceRequestRequestTypeDef",
    "DeleteRetentionPolicyRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeregisterFromWorkMailRequestRequestTypeDef",
    "DeregisterMailDomainRequestRequestTypeDef",
    "DescribeEmailMonitoringConfigurationRequestRequestTypeDef",
    "DescribeEntityRequestRequestTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeInboundDmarcSettingsRequestRequestTypeDef",
    "DescribeMailboxExportJobRequestRequestTypeDef",
    "DescribeOrganizationRequestRequestTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DisassociateDelegateFromResourceRequestRequestTypeDef",
    "DisassociateMemberFromGroupRequestRequestTypeDef",
    "DnsRecordTypeDef",
    "FolderConfigurationTypeDef",
    "GetAccessControlEffectRequestRequestTypeDef",
    "GetDefaultRetentionPolicyRequestRequestTypeDef",
    "GetImpersonationRoleEffectRequestRequestTypeDef",
    "ImpersonationMatchedRuleTypeDef",
    "GetImpersonationRoleRequestRequestTypeDef",
    "GetMailDomainRequestRequestTypeDef",
    "GetMailboxDetailsRequestRequestTypeDef",
    "GetMobileDeviceAccessEffectRequestRequestTypeDef",
    "MobileDeviceAccessMatchedRuleTypeDef",
    "GetMobileDeviceAccessOverrideRequestRequestTypeDef",
    "GroupIdentifierTypeDef",
    "GroupTypeDef",
    "ImpersonationRoleTypeDef",
    "ListAccessControlRulesRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAvailabilityConfigurationsRequestRequestTypeDef",
    "ListGroupMembersRequestRequestTypeDef",
    "MemberTypeDef",
    "ListGroupsFiltersTypeDef",
    "ListGroupsForEntityFiltersTypeDef",
    "ListImpersonationRolesRequestRequestTypeDef",
    "ListMailDomainsRequestRequestTypeDef",
    "MailDomainSummaryTypeDef",
    "ListMailboxExportJobsRequestRequestTypeDef",
    "MailboxExportJobTypeDef",
    "ListMailboxPermissionsRequestRequestTypeDef",
    "PermissionTypeDef",
    "ListMobileDeviceAccessOverridesRequestRequestTypeDef",
    "MobileDeviceAccessOverrideTypeDef",
    "ListMobileDeviceAccessRulesRequestRequestTypeDef",
    "MobileDeviceAccessRuleTypeDef",
    "ListOrganizationsRequestRequestTypeDef",
    "OrganizationSummaryTypeDef",
    "ListResourceDelegatesRequestRequestTypeDef",
    "ListResourcesFiltersTypeDef",
    "ResourceTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ListUsersFiltersTypeDef",
    "UserTypeDef",
    "PutAccessControlRuleRequestRequestTypeDef",
    "PutEmailMonitoringConfigurationRequestRequestTypeDef",
    "PutInboundDmarcSettingsRequestRequestTypeDef",
    "PutMailboxPermissionsRequestRequestTypeDef",
    "PutMobileDeviceAccessOverrideRequestRequestTypeDef",
    "RegisterMailDomainRequestRequestTypeDef",
    "RegisterToWorkMailRequestRequestTypeDef",
    "ResetPasswordRequestRequestTypeDef",
    "StartMailboxExportJobRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDefaultMailDomainRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateMailboxQuotaRequestRequestTypeDef",
    "UpdateMobileDeviceAccessRuleRequestRequestTypeDef",
    "UpdatePrimaryEmailAddressRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "AssumeImpersonationRoleResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateImpersonationRoleResponseTypeDef",
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateResourceResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteOrganizationResponseTypeDef",
    "DescribeEmailMonitoringConfigurationResponseTypeDef",
    "DescribeEntityResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeInboundDmarcSettingsResponseTypeDef",
    "DescribeMailboxExportJobResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "GetAccessControlEffectResponseTypeDef",
    "GetMailboxDetailsResponseTypeDef",
    "GetMobileDeviceAccessOverrideResponseTypeDef",
    "ListAccessControlRulesResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "StartMailboxExportJobResponseTypeDef",
    "TestAvailabilityConfigurationResponseTypeDef",
    "AvailabilityConfigurationTypeDef",
    "DescribeResourceResponseTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "CreateAvailabilityConfigurationRequestRequestTypeDef",
    "TestAvailabilityConfigurationRequestRequestTypeDef",
    "UpdateAvailabilityConfigurationRequestRequestTypeDef",
    "CreateImpersonationRoleRequestRequestTypeDef",
    "GetImpersonationRoleResponseTypeDef",
    "UpdateImpersonationRoleRequestRequestTypeDef",
    "CreateOrganizationRequestRequestTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "GetMailDomainResponseTypeDef",
    "GetDefaultRetentionPolicyResponseTypeDef",
    "PutRetentionPolicyRequestRequestTypeDef",
    "GetImpersonationRoleEffectResponseTypeDef",
    "GetMobileDeviceAccessEffectResponseTypeDef",
    "ListGroupsForEntityResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListImpersonationRolesResponseTypeDef",
    "ListAliasesRequestListAliasesPaginateTypeDef",
    "ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef",
    "ListGroupMembersRequestListGroupMembersPaginateTypeDef",
    "ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef",
    "ListOrganizationsRequestListOrganizationsPaginateTypeDef",
    "ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef",
    "ListGroupMembersResponseTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsForEntityRequestRequestTypeDef",
    "ListMailDomainsResponseTypeDef",
    "ListMailboxExportJobsResponseTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "ListMobileDeviceAccessOverridesResponseTypeDef",
    "ListMobileDeviceAccessRulesResponseTypeDef",
    "ListOrganizationsResponseTypeDef",
    "ListResourcesRequestListResourcesPaginateTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListAvailabilityConfigurationsResponseTypeDef",
)

AccessControlRuleTypeDef = TypedDict(
    "AccessControlRuleTypeDef",
    {
        "Name": NotRequired[str],
        "Effect": NotRequired[AccessControlRuleEffectType],
        "Description": NotRequired[str],
        "IpRanges": NotRequired[List[str]],
        "NotIpRanges": NotRequired[List[str]],
        "Actions": NotRequired[List[str]],
        "NotActions": NotRequired[List[str]],
        "UserIds": NotRequired[List[str]],
        "NotUserIds": NotRequired[List[str]],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
        "ImpersonationRoleIds": NotRequired[List[str]],
        "NotImpersonationRoleIds": NotRequired[List[str]],
    },
)
AssociateDelegateToResourceRequestRequestTypeDef = TypedDict(
    "AssociateDelegateToResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "EntityId": str,
    },
)
AssociateMemberToGroupRequestRequestTypeDef = TypedDict(
    "AssociateMemberToGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "MemberId": str,
    },
)
AssumeImpersonationRoleRequestRequestTypeDef = TypedDict(
    "AssumeImpersonationRoleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ImpersonationRoleId": str,
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
LambdaAvailabilityProviderTypeDef = TypedDict(
    "LambdaAvailabilityProviderTypeDef",
    {
        "LambdaArn": str,
    },
)
RedactedEwsAvailabilityProviderTypeDef = TypedDict(
    "RedactedEwsAvailabilityProviderTypeDef",
    {
        "EwsEndpoint": NotRequired[str],
        "EwsUsername": NotRequired[str],
    },
)
BookingOptionsTypeDef = TypedDict(
    "BookingOptionsTypeDef",
    {
        "AutoAcceptRequests": NotRequired[bool],
        "AutoDeclineRecurringRequests": NotRequired[bool],
        "AutoDeclineConflictingRequests": NotRequired[bool],
    },
)
CancelMailboxExportJobRequestRequestTypeDef = TypedDict(
    "CancelMailboxExportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "JobId": str,
        "OrganizationId": str,
    },
)
CreateAliasRequestRequestTypeDef = TypedDict(
    "CreateAliasRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Alias": str,
    },
)
EwsAvailabilityProviderTypeDef = TypedDict(
    "EwsAvailabilityProviderTypeDef",
    {
        "EwsEndpoint": str,
        "EwsUsername": str,
        "EwsPassword": str,
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)
ImpersonationRuleTypeDef = TypedDict(
    "ImpersonationRuleTypeDef",
    {
        "ImpersonationRuleId": str,
        "Effect": AccessEffectType,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "TargetUsers": NotRequired[Sequence[str]],
        "NotTargetUsers": NotRequired[Sequence[str]],
    },
)
CreateMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "CreateMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "DeviceTypes": NotRequired[Sequence[str]],
        "NotDeviceTypes": NotRequired[Sequence[str]],
        "DeviceModels": NotRequired[Sequence[str]],
        "NotDeviceModels": NotRequired[Sequence[str]],
        "DeviceOperatingSystems": NotRequired[Sequence[str]],
        "NotDeviceOperatingSystems": NotRequired[Sequence[str]],
        "DeviceUserAgents": NotRequired[Sequence[str]],
        "NotDeviceUserAgents": NotRequired[Sequence[str]],
    },
)
DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "DomainName": str,
        "HostedZoneId": NotRequired[str],
    },
)
CreateResourceRequestRequestTypeDef = TypedDict(
    "CreateResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Type": ResourceTypeType,
        "Description": NotRequired[str],
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "DisplayName": str,
        "Password": NotRequired[str],
        "Role": NotRequired[UserRoleType],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)
DelegateTypeDef = TypedDict(
    "DelegateTypeDef",
    {
        "Id": str,
        "Type": MemberTypeType,
    },
)
DeleteAccessControlRuleRequestRequestTypeDef = TypedDict(
    "DeleteAccessControlRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
    },
)
DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Alias": str,
    },
)
DeleteAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
DeleteEmailMonitoringConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEmailMonitoringConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)
DeleteImpersonationRoleRequestRequestTypeDef = TypedDict(
    "DeleteImpersonationRoleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ImpersonationRoleId": str,
    },
)
DeleteMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "DeleteMailboxPermissionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "GranteeId": str,
    },
)
DeleteMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "DeleteMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "DeviceId": str,
    },
)
DeleteMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "DeleteMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "MobileDeviceAccessRuleId": str,
    },
)
DeleteOrganizationRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DeleteDirectory": bool,
        "ClientToken": NotRequired[str],
        "ForceDelete": NotRequired[bool],
    },
)
DeleteResourceRequestRequestTypeDef = TypedDict(
    "DeleteResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)
DeleteRetentionPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRetentionPolicyRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Id": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)
DeregisterFromWorkMailRequestRequestTypeDef = TypedDict(
    "DeregisterFromWorkMailRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
    },
)
DeregisterMailDomainRequestRequestTypeDef = TypedDict(
    "DeregisterMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
DescribeEmailMonitoringConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeEmailMonitoringConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
DescribeEntityRequestRequestTypeDef = TypedDict(
    "DescribeEntityRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Email": str,
    },
)
DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
    },
)
DescribeInboundDmarcSettingsRequestRequestTypeDef = TypedDict(
    "DescribeInboundDmarcSettingsRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
DescribeMailboxExportJobRequestRequestTypeDef = TypedDict(
    "DescribeMailboxExportJobRequestRequestTypeDef",
    {
        "JobId": str,
        "OrganizationId": str,
    },
)
DescribeOrganizationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
DescribeResourceRequestRequestTypeDef = TypedDict(
    "DescribeResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
    },
)
DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)
DisassociateDelegateFromResourceRequestRequestTypeDef = TypedDict(
    "DisassociateDelegateFromResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "EntityId": str,
    },
)
DisassociateMemberFromGroupRequestRequestTypeDef = TypedDict(
    "DisassociateMemberFromGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "MemberId": str,
    },
)
DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": NotRequired[str],
        "Hostname": NotRequired[str],
        "Value": NotRequired[str],
    },
)
FolderConfigurationTypeDef = TypedDict(
    "FolderConfigurationTypeDef",
    {
        "Name": FolderNameType,
        "Action": RetentionActionType,
        "Period": NotRequired[int],
    },
)
GetAccessControlEffectRequestRequestTypeDef = TypedDict(
    "GetAccessControlEffectRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "IpAddress": str,
        "Action": str,
        "UserId": NotRequired[str],
        "ImpersonationRoleId": NotRequired[str],
    },
)
GetDefaultRetentionPolicyRequestRequestTypeDef = TypedDict(
    "GetDefaultRetentionPolicyRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
GetImpersonationRoleEffectRequestRequestTypeDef = TypedDict(
    "GetImpersonationRoleEffectRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ImpersonationRoleId": str,
        "TargetUser": str,
    },
)
ImpersonationMatchedRuleTypeDef = TypedDict(
    "ImpersonationMatchedRuleTypeDef",
    {
        "ImpersonationRuleId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
GetImpersonationRoleRequestRequestTypeDef = TypedDict(
    "GetImpersonationRoleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ImpersonationRoleId": str,
    },
)
GetMailDomainRequestRequestTypeDef = TypedDict(
    "GetMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
GetMailboxDetailsRequestRequestTypeDef = TypedDict(
    "GetMailboxDetailsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
    },
)
GetMobileDeviceAccessEffectRequestRequestTypeDef = TypedDict(
    "GetMobileDeviceAccessEffectRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DeviceType": NotRequired[str],
        "DeviceModel": NotRequired[str],
        "DeviceOperatingSystem": NotRequired[str],
        "DeviceUserAgent": NotRequired[str],
    },
)
MobileDeviceAccessMatchedRuleTypeDef = TypedDict(
    "MobileDeviceAccessMatchedRuleTypeDef",
    {
        "MobileDeviceAccessRuleId": NotRequired[str],
        "Name": NotRequired[str],
    },
)
GetMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "GetMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "DeviceId": str,
    },
)
GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupId": NotRequired[str],
        "GroupName": NotRequired[str],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Id": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[EntityStateType],
        "EnabledDate": NotRequired[datetime],
        "DisabledDate": NotRequired[datetime],
    },
)
ImpersonationRoleTypeDef = TypedDict(
    "ImpersonationRoleTypeDef",
    {
        "ImpersonationRoleId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ImpersonationRoleTypeType],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
    },
)
ListAccessControlRulesRequestRequestTypeDef = TypedDict(
    "ListAccessControlRulesRequestRequestTypeDef",
    {
        "OrganizationId": str,
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
ListAliasesRequestRequestTypeDef = TypedDict(
    "ListAliasesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListAvailabilityConfigurationsRequestRequestTypeDef = TypedDict(
    "ListAvailabilityConfigurationsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListGroupMembersRequestRequestTypeDef = TypedDict(
    "ListGroupMembersRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[MemberTypeType],
        "State": NotRequired[EntityStateType],
        "EnabledDate": NotRequired[datetime],
        "DisabledDate": NotRequired[datetime],
    },
)
ListGroupsFiltersTypeDef = TypedDict(
    "ListGroupsFiltersTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "PrimaryEmailPrefix": NotRequired[str],
        "State": NotRequired[EntityStateType],
    },
)
ListGroupsForEntityFiltersTypeDef = TypedDict(
    "ListGroupsForEntityFiltersTypeDef",
    {
        "GroupNamePrefix": NotRequired[str],
    },
)
ListImpersonationRolesRequestRequestTypeDef = TypedDict(
    "ListImpersonationRolesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMailDomainsRequestRequestTypeDef = TypedDict(
    "ListMailDomainsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
MailDomainSummaryTypeDef = TypedDict(
    "MailDomainSummaryTypeDef",
    {
        "DomainName": NotRequired[str],
        "DefaultDomain": NotRequired[bool],
    },
)
ListMailboxExportJobsRequestRequestTypeDef = TypedDict(
    "ListMailboxExportJobsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MailboxExportJobTypeDef = TypedDict(
    "MailboxExportJobTypeDef",
    {
        "JobId": NotRequired[str],
        "EntityId": NotRequired[str],
        "Description": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3Path": NotRequired[str],
        "EstimatedProgress": NotRequired[int],
        "State": NotRequired[MailboxExportJobStateType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
ListMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "ListMailboxPermissionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeId": str,
        "GranteeType": MemberTypeType,
        "PermissionValues": List[PermissionTypeType],
    },
)
ListMobileDeviceAccessOverridesRequestRequestTypeDef = TypedDict(
    "ListMobileDeviceAccessOverridesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MobileDeviceAccessOverrideTypeDef = TypedDict(
    "MobileDeviceAccessOverrideTypeDef",
    {
        "UserId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "Effect": NotRequired[MobileDeviceAccessRuleEffectType],
        "Description": NotRequired[str],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
    },
)
ListMobileDeviceAccessRulesRequestRequestTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesRequestRequestTypeDef",
    {
        "OrganizationId": str,
    },
)
MobileDeviceAccessRuleTypeDef = TypedDict(
    "MobileDeviceAccessRuleTypeDef",
    {
        "MobileDeviceAccessRuleId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Effect": NotRequired[MobileDeviceAccessRuleEffectType],
        "DeviceTypes": NotRequired[List[str]],
        "NotDeviceTypes": NotRequired[List[str]],
        "DeviceModels": NotRequired[List[str]],
        "NotDeviceModels": NotRequired[List[str]],
        "DeviceOperatingSystems": NotRequired[List[str]],
        "NotDeviceOperatingSystems": NotRequired[List[str]],
        "DeviceUserAgents": NotRequired[List[str]],
        "NotDeviceUserAgents": NotRequired[List[str]],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
    },
)
ListOrganizationsRequestRequestTypeDef = TypedDict(
    "ListOrganizationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
OrganizationSummaryTypeDef = TypedDict(
    "OrganizationSummaryTypeDef",
    {
        "OrganizationId": NotRequired[str],
        "Alias": NotRequired[str],
        "DefaultMailDomain": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "State": NotRequired[str],
    },
)
ListResourceDelegatesRequestRequestTypeDef = TypedDict(
    "ListResourceDelegatesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListResourcesFiltersTypeDef = TypedDict(
    "ListResourcesFiltersTypeDef",
    {
        "NamePrefix": NotRequired[str],
        "PrimaryEmailPrefix": NotRequired[str],
        "State": NotRequired[EntityStateType],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ResourceTypeType],
        "State": NotRequired[EntityStateType],
        "EnabledDate": NotRequired[datetime],
        "DisabledDate": NotRequired[datetime],
        "Description": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ListUsersFiltersTypeDef = TypedDict(
    "ListUsersFiltersTypeDef",
    {
        "UsernamePrefix": NotRequired[str],
        "DisplayNamePrefix": NotRequired[str],
        "PrimaryEmailPrefix": NotRequired[str],
        "State": NotRequired[EntityStateType],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "DisplayName": NotRequired[str],
        "State": NotRequired[EntityStateType],
        "UserRole": NotRequired[UserRoleType],
        "EnabledDate": NotRequired[datetime],
        "DisabledDate": NotRequired[datetime],
    },
)
PutAccessControlRuleRequestRequestTypeDef = TypedDict(
    "PutAccessControlRuleRequestRequestTypeDef",
    {
        "Name": str,
        "Effect": AccessControlRuleEffectType,
        "Description": str,
        "OrganizationId": str,
        "IpRanges": NotRequired[Sequence[str]],
        "NotIpRanges": NotRequired[Sequence[str]],
        "Actions": NotRequired[Sequence[str]],
        "NotActions": NotRequired[Sequence[str]],
        "UserIds": NotRequired[Sequence[str]],
        "NotUserIds": NotRequired[Sequence[str]],
        "ImpersonationRoleIds": NotRequired[Sequence[str]],
        "NotImpersonationRoleIds": NotRequired[Sequence[str]],
    },
)
PutEmailMonitoringConfigurationRequestRequestTypeDef = TypedDict(
    "PutEmailMonitoringConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "RoleArn": str,
        "LogGroupArn": str,
    },
)
PutInboundDmarcSettingsRequestRequestTypeDef = TypedDict(
    "PutInboundDmarcSettingsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Enforced": bool,
    },
)
PutMailboxPermissionsRequestRequestTypeDef = TypedDict(
    "PutMailboxPermissionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "GranteeId": str,
        "PermissionValues": Sequence[PermissionTypeType],
    },
)
PutMobileDeviceAccessOverrideRequestRequestTypeDef = TypedDict(
    "PutMobileDeviceAccessOverrideRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "DeviceId": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "Description": NotRequired[str],
    },
)
RegisterMailDomainRequestRequestTypeDef = TypedDict(
    "RegisterMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
        "ClientToken": NotRequired[str],
    },
)
RegisterToWorkMailRequestRequestTypeDef = TypedDict(
    "RegisterToWorkMailRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Email": str,
    },
)
ResetPasswordRequestRequestTypeDef = TypedDict(
    "ResetPasswordRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "Password": str,
    },
)
StartMailboxExportJobRequestRequestTypeDef = TypedDict(
    "StartMailboxExportJobRequestRequestTypeDef",
    {
        "ClientToken": str,
        "OrganizationId": str,
        "EntityId": str,
        "RoleArn": str,
        "KmsKeyArn": str,
        "S3BucketName": str,
        "S3Prefix": str,
        "Description": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDefaultMailDomainRequestRequestTypeDef = TypedDict(
    "UpdateDefaultMailDomainRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)
UpdateMailboxQuotaRequestRequestTypeDef = TypedDict(
    "UpdateMailboxQuotaRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "MailboxQuota": int,
    },
)
UpdateMobileDeviceAccessRuleRequestRequestTypeDef = TypedDict(
    "UpdateMobileDeviceAccessRuleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "MobileDeviceAccessRuleId": str,
        "Name": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "Description": NotRequired[str],
        "DeviceTypes": NotRequired[Sequence[str]],
        "NotDeviceTypes": NotRequired[Sequence[str]],
        "DeviceModels": NotRequired[Sequence[str]],
        "NotDeviceModels": NotRequired[Sequence[str]],
        "DeviceOperatingSystems": NotRequired[Sequence[str]],
        "NotDeviceOperatingSystems": NotRequired[Sequence[str]],
        "DeviceUserAgents": NotRequired[Sequence[str]],
        "NotDeviceUserAgents": NotRequired[Sequence[str]],
    },
)
UpdatePrimaryEmailAddressRequestRequestTypeDef = TypedDict(
    "UpdatePrimaryEmailAddressRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Email": str,
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "UserId": str,
        "Role": NotRequired[UserRoleType],
        "DisplayName": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "HiddenFromGlobalAddressList": NotRequired[bool],
        "Initials": NotRequired[str],
        "Telephone": NotRequired[str],
        "Street": NotRequired[str],
        "JobTitle": NotRequired[str],
        "City": NotRequired[str],
        "Company": NotRequired[str],
        "ZipCode": NotRequired[str],
        "Department": NotRequired[str],
        "Country": NotRequired[str],
        "Office": NotRequired[str],
    },
)
AssumeImpersonationRoleResponseTypeDef = TypedDict(
    "AssumeImpersonationRoleResponseTypeDef",
    {
        "Token": str,
        "ExpiresIn": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateImpersonationRoleResponseTypeDef = TypedDict(
    "CreateImpersonationRoleResponseTypeDef",
    {
        "ImpersonationRoleId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMobileDeviceAccessRuleResponseTypeDef = TypedDict(
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    {
        "MobileDeviceAccessRuleId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceResponseTypeDef = TypedDict(
    "CreateResourceResponseTypeDef",
    {
        "ResourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteOrganizationResponseTypeDef = TypedDict(
    "DeleteOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "State": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEmailMonitoringConfigurationResponseTypeDef = TypedDict(
    "DescribeEmailMonitoringConfigurationResponseTypeDef",
    {
        "RoleArn": str,
        "LogGroupArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityId": str,
        "Name": str,
        "Type": EntityTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "Name": str,
        "Email": str,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "HiddenFromGlobalAddressList": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeInboundDmarcSettingsResponseTypeDef = TypedDict(
    "DescribeInboundDmarcSettingsResponseTypeDef",
    {
        "Enforced": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeMailboxExportJobResponseTypeDef = TypedDict(
    "DescribeMailboxExportJobResponseTypeDef",
    {
        "EntityId": str,
        "Description": str,
        "RoleArn": str,
        "KmsKeyArn": str,
        "S3BucketName": str,
        "S3Prefix": str,
        "S3Path": str,
        "EstimatedProgress": int,
        "State": MailboxExportJobStateType,
        "ErrorInfo": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeOrganizationResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseTypeDef",
    {
        "OrganizationId": str,
        "Alias": str,
        "State": str,
        "DirectoryId": str,
        "DirectoryType": str,
        "DefaultMailDomain": str,
        "CompletedDate": datetime,
        "ErrorMessage": str,
        "ARN": str,
        "MigrationAdmin": str,
        "InteroperabilityEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserId": str,
        "Name": str,
        "Email": str,
        "DisplayName": str,
        "State": EntityStateType,
        "UserRole": UserRoleType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "MailboxProvisionedDate": datetime,
        "MailboxDeprovisionedDate": datetime,
        "FirstName": str,
        "LastName": str,
        "HiddenFromGlobalAddressList": bool,
        "Initials": str,
        "Telephone": str,
        "Street": str,
        "JobTitle": str,
        "City": str,
        "Company": str,
        "ZipCode": str,
        "Department": str,
        "Country": str,
        "Office": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessControlEffectResponseTypeDef = TypedDict(
    "GetAccessControlEffectResponseTypeDef",
    {
        "Effect": AccessControlRuleEffectType,
        "MatchedRules": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMailboxDetailsResponseTypeDef = TypedDict(
    "GetMailboxDetailsResponseTypeDef",
    {
        "MailboxQuota": int,
        "MailboxSize": float,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMobileDeviceAccessOverrideResponseTypeDef = TypedDict(
    "GetMobileDeviceAccessOverrideResponseTypeDef",
    {
        "UserId": str,
        "DeviceId": str,
        "Effect": MobileDeviceAccessRuleEffectType,
        "Description": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessControlRulesResponseTypeDef = TypedDict(
    "ListAccessControlRulesResponseTypeDef",
    {
        "Rules": List[AccessControlRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "Aliases": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMailboxExportJobResponseTypeDef = TypedDict(
    "StartMailboxExportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestAvailabilityConfigurationResponseTypeDef = TypedDict(
    "TestAvailabilityConfigurationResponseTypeDef",
    {
        "TestPassed": bool,
        "FailureReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AvailabilityConfigurationTypeDef = TypedDict(
    "AvailabilityConfigurationTypeDef",
    {
        "DomainName": NotRequired[str],
        "ProviderType": NotRequired[AvailabilityProviderTypeType],
        "EwsProvider": NotRequired[RedactedEwsAvailabilityProviderTypeDef],
        "LambdaProvider": NotRequired[LambdaAvailabilityProviderTypeDef],
        "DateCreated": NotRequired[datetime],
        "DateModified": NotRequired[datetime],
    },
)
DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": ResourceTypeType,
        "BookingOptions": BookingOptionsTypeDef,
        "State": EntityStateType,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
        "Description": str,
        "HiddenFromGlobalAddressList": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceRequestRequestTypeDef = TypedDict(
    "UpdateResourceRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "Name": NotRequired[str],
        "BookingOptions": NotRequired[BookingOptionsTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[ResourceTypeType],
        "HiddenFromGlobalAddressList": NotRequired[bool],
    },
)
CreateAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "CreateAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
        "ClientToken": NotRequired[str],
        "EwsProvider": NotRequired[EwsAvailabilityProviderTypeDef],
        "LambdaProvider": NotRequired[LambdaAvailabilityProviderTypeDef],
    },
)
TestAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "TestAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": NotRequired[str],
        "EwsProvider": NotRequired[EwsAvailabilityProviderTypeDef],
        "LambdaProvider": NotRequired[LambdaAvailabilityProviderTypeDef],
    },
)
UpdateAvailabilityConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAvailabilityConfigurationRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "DomainName": str,
        "EwsProvider": NotRequired[EwsAvailabilityProviderTypeDef],
        "LambdaProvider": NotRequired[LambdaAvailabilityProviderTypeDef],
    },
)
CreateImpersonationRoleRequestRequestTypeDef = TypedDict(
    "CreateImpersonationRoleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "Type": ImpersonationRoleTypeType,
        "Rules": Sequence[ImpersonationRuleTypeDef],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
    },
)
GetImpersonationRoleResponseTypeDef = TypedDict(
    "GetImpersonationRoleResponseTypeDef",
    {
        "ImpersonationRoleId": str,
        "Name": str,
        "Type": ImpersonationRoleTypeType,
        "Description": str,
        "Rules": List[ImpersonationRuleTypeDef],
        "DateCreated": datetime,
        "DateModified": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateImpersonationRoleRequestRequestTypeDef = TypedDict(
    "UpdateImpersonationRoleRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "ImpersonationRoleId": str,
        "Name": str,
        "Type": ImpersonationRoleTypeType,
        "Rules": Sequence[ImpersonationRuleTypeDef],
        "Description": NotRequired[str],
    },
)
CreateOrganizationRequestRequestTypeDef = TypedDict(
    "CreateOrganizationRequestRequestTypeDef",
    {
        "Alias": str,
        "DirectoryId": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Domains": NotRequired[Sequence[DomainTypeDef]],
        "KmsKeyArn": NotRequired[str],
        "EnableInteroperability": NotRequired[bool],
    },
)
ListResourceDelegatesResponseTypeDef = TypedDict(
    "ListResourceDelegatesResponseTypeDef",
    {
        "Delegates": List[DelegateTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMailDomainResponseTypeDef = TypedDict(
    "GetMailDomainResponseTypeDef",
    {
        "Records": List[DnsRecordTypeDef],
        "IsTestDomain": bool,
        "IsDefault": bool,
        "OwnershipVerificationStatus": DnsRecordVerificationStatusType,
        "DkimVerificationStatus": DnsRecordVerificationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDefaultRetentionPolicyResponseTypeDef = TypedDict(
    "GetDefaultRetentionPolicyResponseTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "FolderConfigurations": List[FolderConfigurationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRetentionPolicyRequestRequestTypeDef = TypedDict(
    "PutRetentionPolicyRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Name": str,
        "FolderConfigurations": Sequence[FolderConfigurationTypeDef],
        "Id": NotRequired[str],
        "Description": NotRequired[str],
    },
)
GetImpersonationRoleEffectResponseTypeDef = TypedDict(
    "GetImpersonationRoleEffectResponseTypeDef",
    {
        "Type": ImpersonationRoleTypeType,
        "Effect": AccessEffectType,
        "MatchedRules": List[ImpersonationMatchedRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMobileDeviceAccessEffectResponseTypeDef = TypedDict(
    "GetMobileDeviceAccessEffectResponseTypeDef",
    {
        "Effect": MobileDeviceAccessRuleEffectType,
        "MatchedRules": List[MobileDeviceAccessMatchedRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsForEntityResponseTypeDef = TypedDict(
    "ListGroupsForEntityResponseTypeDef",
    {
        "Groups": List[GroupIdentifierTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImpersonationRolesResponseTypeDef = TypedDict(
    "ListImpersonationRolesResponseTypeDef",
    {
        "Roles": List[ImpersonationRoleTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAliasesRequestListAliasesPaginateTypeDef = TypedDict(
    "ListAliasesRequestListAliasesPaginateTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef = TypedDict(
    "ListAvailabilityConfigurationsRequestListAvailabilityConfigurationsPaginateTypeDef",
    {
        "OrganizationId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupMembersRequestListGroupMembersPaginateTypeDef = TypedDict(
    "ListGroupMembersRequestListGroupMembersPaginateTypeDef",
    {
        "OrganizationId": str,
        "GroupId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef = TypedDict(
    "ListMailboxPermissionsRequestListMailboxPermissionsPaginateTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOrganizationsRequestListOrganizationsPaginateTypeDef = TypedDict(
    "ListOrganizationsRequestListOrganizationsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef = TypedDict(
    "ListResourceDelegatesRequestListResourceDelegatesPaginateTypeDef",
    {
        "OrganizationId": str,
        "ResourceId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupMembersResponseTypeDef = TypedDict(
    "ListGroupMembersResponseTypeDef",
    {
        "Members": List[MemberTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "OrganizationId": str,
        "Filters": NotRequired[ListGroupsFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[ListGroupsFiltersTypeDef],
    },
)
ListGroupsForEntityRequestRequestTypeDef = TypedDict(
    "ListGroupsForEntityRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "EntityId": str,
        "Filters": NotRequired[ListGroupsForEntityFiltersTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListMailDomainsResponseTypeDef = TypedDict(
    "ListMailDomainsResponseTypeDef",
    {
        "MailDomains": List[MailDomainSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMailboxExportJobsResponseTypeDef = TypedDict(
    "ListMailboxExportJobsResponseTypeDef",
    {
        "Jobs": List[MailboxExportJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMailboxPermissionsResponseTypeDef = TypedDict(
    "ListMailboxPermissionsResponseTypeDef",
    {
        "Permissions": List[PermissionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMobileDeviceAccessOverridesResponseTypeDef = TypedDict(
    "ListMobileDeviceAccessOverridesResponseTypeDef",
    {
        "Overrides": List[MobileDeviceAccessOverrideTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMobileDeviceAccessRulesResponseTypeDef = TypedDict(
    "ListMobileDeviceAccessRulesResponseTypeDef",
    {
        "Rules": List[MobileDeviceAccessRuleTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOrganizationsResponseTypeDef = TypedDict(
    "ListOrganizationsResponseTypeDef",
    {
        "OrganizationSummaries": List[OrganizationSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListResourcesRequestListResourcesPaginateTypeDef = TypedDict(
    "ListResourcesRequestListResourcesPaginateTypeDef",
    {
        "OrganizationId": str,
        "Filters": NotRequired[ListResourcesFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[ListResourcesFiltersTypeDef],
    },
)
ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "Resources": List[ResourceTypeDef],
        "NextToken": str,
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
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "OrganizationId": str,
        "Filters": NotRequired[ListUsersFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[ListUsersFiltersTypeDef],
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAvailabilityConfigurationsResponseTypeDef = TypedDict(
    "ListAvailabilityConfigurationsResponseTypeDef",
    {
        "AvailabilityConfigurations": List[AvailabilityConfigurationTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
