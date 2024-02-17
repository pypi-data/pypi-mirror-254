"""
Type annotations for datazone service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/type_defs/)

Usage::

    ```python
    from mypy_boto3_datazone.type_defs import AcceptChoiceTypeDef

    data: AcceptChoiceTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AcceptRuleBehaviorType,
    AuthTypeType,
    ChangeActionType,
    ConfigurableActionTypeAuthorizationType,
    DataAssetActivityStatusType,
    DataSourceErrorTypeType,
    DataSourceRunStatusType,
    DataSourceRunTypeType,
    DataSourceStatusType,
    DeploymentStatusType,
    DeploymentTypeType,
    DomainStatusType,
    EnableSettingType,
    EnvironmentStatusType,
    FilterExpressionTypeType,
    FormTypeStatusType,
    GlossaryStatusType,
    GlossaryTermStatusType,
    GroupProfileStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    ListingStatusType,
    NotificationRoleType,
    NotificationTypeType,
    ProjectStatusType,
    RejectRuleBehaviorType,
    SortKeyType,
    SortOrderType,
    SubscriptionGrantOverallStatusType,
    SubscriptionGrantStatusType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TaskStatusType,
    TimezoneType,
    TypesSearchScopeType,
    UserAssignmentType,
    UserDesignationType,
    UserProfileStatusType,
    UserProfileTypeType,
    UserSearchTypeType,
    UserTypeType,
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
    "AcceptChoiceTypeDef",
    "AcceptRuleTypeDef",
    "ResponseMetadataTypeDef",
    "AcceptSubscriptionRequestInputRequestTypeDef",
    "FormOutputTypeDef",
    "AssetListingDetailsTypeDef",
    "AssetListingItemAdditionalAttributesTypeDef",
    "DetailedGlossaryTermTypeDef",
    "AssetRevisionTypeDef",
    "AssetTargetNameMapTypeDef",
    "FormEntryOutputTypeDef",
    "BusinessNameGenerationConfigurationTypeDef",
    "CancelSubscriptionInputRequestTypeDef",
    "CloudFormationPropertiesTypeDef",
    "ConfigurableActionParameterTypeDef",
    "FormInputTypeDef",
    "FormEntryInputTypeDef",
    "RecommendationConfigurationTypeDef",
    "ScheduleConfigurationTypeDef",
    "DataSourceErrorMessageTypeDef",
    "SingleSignOnTypeDef",
    "EnvironmentParameterTypeDef",
    "CustomParameterTypeDef",
    "DeploymentPropertiesTypeDef",
    "ResourceTypeDef",
    "ModelTypeDef",
    "CreateGlossaryInputRequestTypeDef",
    "TermRelationsTypeDef",
    "CreateGroupProfileInputRequestTypeDef",
    "CreateListingChangeSetInputRequestTypeDef",
    "CreateProjectInputRequestTypeDef",
    "MemberTypeDef",
    "ProjectDeletionErrorTypeDef",
    "SubscribedListingInputTypeDef",
    "SubscriptionTargetFormTypeDef",
    "CreateUserProfileInputRequestTypeDef",
    "DataProductItemTypeDef",
    "RunStatisticsForAssetsTypeDef",
    "DeleteAssetInputRequestTypeDef",
    "DeleteAssetTypeInputRequestTypeDef",
    "DeleteDataSourceInputRequestTypeDef",
    "DeleteDomainInputRequestTypeDef",
    "DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentProfileInputRequestTypeDef",
    "DeleteFormTypeInputRequestTypeDef",
    "DeleteGlossaryInputRequestTypeDef",
    "DeleteGlossaryTermInputRequestTypeDef",
    "DeleteListingInputRequestTypeDef",
    "DeleteProjectInputRequestTypeDef",
    "DeleteSubscriptionGrantInputRequestTypeDef",
    "DeleteSubscriptionRequestInputRequestTypeDef",
    "DeleteSubscriptionTargetInputRequestTypeDef",
    "EnvironmentErrorTypeDef",
    "DomainSummaryTypeDef",
    "EnvironmentBlueprintConfigurationItemTypeDef",
    "EnvironmentProfileSummaryTypeDef",
    "EnvironmentSummaryTypeDef",
    "FailureCauseTypeDef",
    "FilterTypeDef",
    "FilterExpressionTypeDef",
    "ImportTypeDef",
    "GetAssetInputRequestTypeDef",
    "GetAssetTypeInputRequestTypeDef",
    "GetDataSourceInputRequestTypeDef",
    "GetDataSourceRunInputRequestTypeDef",
    "GetDomainInputRequestTypeDef",
    "GetEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "GetEnvironmentBlueprintInputRequestTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentProfileInputRequestTypeDef",
    "GetFormTypeInputRequestTypeDef",
    "GetGlossaryInputRequestTypeDef",
    "GetGlossaryTermInputRequestTypeDef",
    "GetGroupProfileInputRequestTypeDef",
    "GetIamPortalLoginUrlInputRequestTypeDef",
    "GetListingInputRequestTypeDef",
    "GetProjectInputRequestTypeDef",
    "GetSubscriptionGrantInputRequestTypeDef",
    "GetSubscriptionInputRequestTypeDef",
    "GetSubscriptionRequestDetailsInputRequestTypeDef",
    "GetSubscriptionTargetInputRequestTypeDef",
    "GetUserProfileInputRequestTypeDef",
    "GlossaryItemTypeDef",
    "TermRelationsPaginatorTypeDef",
    "ListingRevisionInputTypeDef",
    "ListingRevisionTypeDef",
    "GroupDetailsTypeDef",
    "GroupProfileSummaryTypeDef",
    "IamUserProfileDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ListAssetRevisionsInputRequestTypeDef",
    "ListDataSourceRunActivitiesInputRequestTypeDef",
    "ListDataSourceRunsInputRequestTypeDef",
    "ListDataSourcesInputRequestTypeDef",
    "ListDomainsInputRequestTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    "ListEnvironmentBlueprintsInputRequestTypeDef",
    "ListEnvironmentProfilesInputRequestTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "TimestampTypeDef",
    "ListProjectMembershipsInputRequestTypeDef",
    "ListProjectsInputRequestTypeDef",
    "ListSubscriptionGrantsInputRequestTypeDef",
    "ListSubscriptionRequestsInputRequestTypeDef",
    "ListSubscriptionTargetsInputRequestTypeDef",
    "ListSubscriptionsInputRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "UserDetailsTypeDef",
    "NotificationResourceTypeDef",
    "PutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    "RedshiftClusterStorageTypeDef",
    "RedshiftCredentialConfigurationTypeDef",
    "RedshiftServerlessStorageTypeDef",
    "RejectChoiceTypeDef",
    "RejectRuleTypeDef",
    "RejectSubscriptionRequestInputRequestTypeDef",
    "RevokeSubscriptionInputRequestTypeDef",
    "SearchGroupProfilesInputRequestTypeDef",
    "SearchInItemTypeDef",
    "SearchSortTypeDef",
    "SearchUserProfilesInputRequestTypeDef",
    "SsoUserProfileDetailsTypeDef",
    "StartDataSourceRunInputRequestTypeDef",
    "SubscribedProjectInputTypeDef",
    "SubscribedProjectTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateGlossaryInputRequestTypeDef",
    "UpdateGroupProfileInputRequestTypeDef",
    "UpdateProjectInputRequestTypeDef",
    "UpdateSubscriptionRequestInputRequestTypeDef",
    "UpdateUserProfileInputRequestTypeDef",
    "AcceptPredictionsInputRequestTypeDef",
    "AcceptPredictionsOutputTypeDef",
    "CreateFormTypeOutputTypeDef",
    "CreateGlossaryOutputTypeDef",
    "CreateGroupProfileOutputTypeDef",
    "CreateListingChangeSetOutputTypeDef",
    "DeleteDomainOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    "GetGlossaryOutputTypeDef",
    "GetGroupProfileOutputTypeDef",
    "GetIamPortalLoginUrlOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    "RejectPredictionsOutputTypeDef",
    "UpdateGlossaryOutputTypeDef",
    "UpdateGroupProfileOutputTypeDef",
    "AssetItemAdditionalAttributesTypeDef",
    "GetAssetOutputTypeDef",
    "AssetListingItemTypeDef",
    "AssetListingTypeDef",
    "SubscribedAssetListingTypeDef",
    "ListAssetRevisionsOutputTypeDef",
    "AssetTypeItemTypeDef",
    "CreateAssetTypeOutputTypeDef",
    "GetAssetTypeOutputTypeDef",
    "PredictionConfigurationTypeDef",
    "ProvisioningPropertiesTypeDef",
    "ConfigurableEnvironmentActionTypeDef",
    "CreateAssetTypeInputRequestTypeDef",
    "DataSourceRunActivityTypeDef",
    "DataSourceSummaryTypeDef",
    "CreateDomainInputRequestTypeDef",
    "CreateDomainOutputTypeDef",
    "GetDomainOutputTypeDef",
    "UpdateDomainInputRequestTypeDef",
    "UpdateDomainOutputTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentProfileInputRequestTypeDef",
    "UpdateEnvironmentProfileInputRequestTypeDef",
    "CreateEnvironmentProfileOutputTypeDef",
    "GetEnvironmentProfileOutputTypeDef",
    "UpdateEnvironmentProfileOutputTypeDef",
    "CreateFormTypeInputRequestTypeDef",
    "CreateGlossaryTermInputRequestTypeDef",
    "CreateGlossaryTermOutputTypeDef",
    "GetGlossaryTermOutputTypeDef",
    "GlossaryTermItemTypeDef",
    "UpdateGlossaryTermInputRequestTypeDef",
    "UpdateGlossaryTermOutputTypeDef",
    "CreateProjectMembershipInputRequestTypeDef",
    "DeleteProjectMembershipInputRequestTypeDef",
    "CreateProjectOutputTypeDef",
    "GetProjectOutputTypeDef",
    "ProjectSummaryTypeDef",
    "UpdateProjectOutputTypeDef",
    "CreateSubscriptionTargetInputRequestTypeDef",
    "CreateSubscriptionTargetOutputTypeDef",
    "GetSubscriptionTargetOutputTypeDef",
    "SubscriptionTargetSummaryTypeDef",
    "UpdateSubscriptionTargetInputRequestTypeDef",
    "UpdateSubscriptionTargetOutputTypeDef",
    "DataProductSummaryTypeDef",
    "DataSourceRunSummaryTypeDef",
    "GetDataSourceRunOutputTypeDef",
    "StartDataSourceRunOutputTypeDef",
    "DeploymentTypeDef",
    "ListDomainsOutputTypeDef",
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    "ListEnvironmentProfilesOutputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "SubscribedAssetTypeDef",
    "UpdateSubscriptionGrantStatusInputRequestTypeDef",
    "FilterClauseTypeDef",
    "RelationalFilterConfigurationTypeDef",
    "FormTypeDataTypeDef",
    "GetFormTypeOutputTypeDef",
    "GlossaryTermItemPaginatorTypeDef",
    "GrantedEntityInputTypeDef",
    "GrantedEntityTypeDef",
    "SearchGroupProfilesOutputTypeDef",
    "ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef",
    "ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef",
    "ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef",
    "ListDataSourcesInputListDataSourcesPaginateTypeDef",
    "ListDomainsInputListDomainsPaginateTypeDef",
    "ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef",
    "ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef",
    "ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef",
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    "ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef",
    "ListProjectsInputListProjectsPaginateTypeDef",
    "ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef",
    "ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef",
    "ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef",
    "ListSubscriptionsInputListSubscriptionsPaginateTypeDef",
    "SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef",
    "SearchUserProfilesInputSearchUserProfilesPaginateTypeDef",
    "ListNotificationsInputListNotificationsPaginateTypeDef",
    "ListNotificationsInputRequestTypeDef",
    "MemberDetailsTypeDef",
    "TopicTypeDef",
    "RedshiftStorageTypeDef",
    "RejectPredictionsInputRequestTypeDef",
    "SearchInputRequestTypeDef",
    "SearchListingsInputRequestTypeDef",
    "SearchTypesInputRequestTypeDef",
    "UserProfileDetailsTypeDef",
    "SubscribedPrincipalInputTypeDef",
    "SubscribedPrincipalTypeDef",
    "AssetItemTypeDef",
    "SearchResultItemTypeDef",
    "ListingItemTypeDef",
    "SubscribedListingItemTypeDef",
    "CreateAssetInputRequestTypeDef",
    "CreateAssetOutputTypeDef",
    "CreateAssetRevisionInputRequestTypeDef",
    "CreateAssetRevisionOutputTypeDef",
    "EnvironmentBlueprintSummaryTypeDef",
    "GetEnvironmentBlueprintOutputTypeDef",
    "ListDataSourceRunActivitiesOutputTypeDef",
    "ListDataSourcesOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListSubscriptionTargetsOutputTypeDef",
    "ListDataSourceRunsOutputTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "GetEnvironmentOutputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "SearchInputSearchPaginateTypeDef",
    "SearchListingsInputSearchListingsPaginateTypeDef",
    "SearchTypesInputSearchTypesPaginateTypeDef",
    "GlueRunConfigurationInputTypeDef",
    "GlueRunConfigurationOutputTypeDef",
    "SearchTypesResultItemTypeDef",
    "CreateSubscriptionGrantInputRequestTypeDef",
    "CreateSubscriptionGrantOutputTypeDef",
    "DeleteSubscriptionGrantOutputTypeDef",
    "GetSubscriptionGrantOutputTypeDef",
    "SubscriptionGrantSummaryTypeDef",
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    "ProjectMemberTypeDef",
    "NotificationOutputTypeDef",
    "RedshiftRunConfigurationInputTypeDef",
    "RedshiftRunConfigurationOutputTypeDef",
    "CreateUserProfileOutputTypeDef",
    "GetUserProfileOutputTypeDef",
    "UpdateUserProfileOutputTypeDef",
    "UserProfileSummaryTypeDef",
    "CreateSubscriptionRequestInputRequestTypeDef",
    "SearchInventoryResultItemPaginatorTypeDef",
    "SearchInventoryResultItemTypeDef",
    "SearchListingsOutputTypeDef",
    "GetListingOutputTypeDef",
    "SubscribedListingTypeDef",
    "ListEnvironmentBlueprintsOutputTypeDef",
    "SearchTypesOutputTypeDef",
    "ListSubscriptionGrantsOutputTypeDef",
    "ListProjectMembershipsOutputTypeDef",
    "ListNotificationsOutputTypeDef",
    "DataSourceConfigurationInputTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "SearchUserProfilesOutputTypeDef",
    "SearchOutputPaginatorTypeDef",
    "SearchOutputTypeDef",
    "AcceptSubscriptionRequestOutputTypeDef",
    "CancelSubscriptionOutputTypeDef",
    "CreateSubscriptionRequestOutputTypeDef",
    "GetSubscriptionOutputTypeDef",
    "GetSubscriptionRequestDetailsOutputTypeDef",
    "RejectSubscriptionRequestOutputTypeDef",
    "RevokeSubscriptionOutputTypeDef",
    "SubscriptionRequestSummaryTypeDef",
    "SubscriptionSummaryTypeDef",
    "UpdateSubscriptionRequestOutputTypeDef",
    "CreateDataSourceInputRequestTypeDef",
    "UpdateDataSourceInputRequestTypeDef",
    "CreateDataSourceOutputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "GetDataSourceOutputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "ListSubscriptionRequestsOutputTypeDef",
    "ListSubscriptionsOutputTypeDef",
)

AcceptChoiceTypeDef = TypedDict(
    "AcceptChoiceTypeDef",
    {
        "predictionChoice": NotRequired[int],
        "predictionTarget": NotRequired[str],
    },
)
AcceptRuleTypeDef = TypedDict(
    "AcceptRuleTypeDef",
    {
        "rule": NotRequired[AcceptRuleBehaviorType],
        "threshold": NotRequired[float],
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
AcceptSubscriptionRequestInputRequestTypeDef = TypedDict(
    "AcceptSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "decisionComment": NotRequired[str],
    },
)
FormOutputTypeDef = TypedDict(
    "FormOutputTypeDef",
    {
        "formName": str,
        "content": NotRequired[str],
        "typeName": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
AssetListingDetailsTypeDef = TypedDict(
    "AssetListingDetailsTypeDef",
    {
        "listingId": str,
        "listingStatus": ListingStatusType,
    },
)
AssetListingItemAdditionalAttributesTypeDef = TypedDict(
    "AssetListingItemAdditionalAttributesTypeDef",
    {
        "forms": NotRequired[str],
    },
)
DetailedGlossaryTermTypeDef = TypedDict(
    "DetailedGlossaryTermTypeDef",
    {
        "name": NotRequired[str],
        "shortDescription": NotRequired[str],
    },
)
AssetRevisionTypeDef = TypedDict(
    "AssetRevisionTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "revision": NotRequired[str],
    },
)
AssetTargetNameMapTypeDef = TypedDict(
    "AssetTargetNameMapTypeDef",
    {
        "assetId": str,
        "targetName": str,
    },
)
FormEntryOutputTypeDef = TypedDict(
    "FormEntryOutputTypeDef",
    {
        "typeName": str,
        "typeRevision": str,
        "required": NotRequired[bool],
    },
)
BusinessNameGenerationConfigurationTypeDef = TypedDict(
    "BusinessNameGenerationConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
    },
)
CancelSubscriptionInputRequestTypeDef = TypedDict(
    "CancelSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
CloudFormationPropertiesTypeDef = TypedDict(
    "CloudFormationPropertiesTypeDef",
    {
        "templateUrl": str,
    },
)
ConfigurableActionParameterTypeDef = TypedDict(
    "ConfigurableActionParameterTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)
FormInputTypeDef = TypedDict(
    "FormInputTypeDef",
    {
        "formName": str,
        "content": NotRequired[str],
        "typeIdentifier": NotRequired[str],
        "typeRevision": NotRequired[str],
    },
)
FormEntryInputTypeDef = TypedDict(
    "FormEntryInputTypeDef",
    {
        "typeIdentifier": str,
        "typeRevision": str,
        "required": NotRequired[bool],
    },
)
RecommendationConfigurationTypeDef = TypedDict(
    "RecommendationConfigurationTypeDef",
    {
        "enableBusinessNameGeneration": NotRequired[bool],
    },
)
ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "schedule": NotRequired[str],
        "timezone": NotRequired[TimezoneType],
    },
)
DataSourceErrorMessageTypeDef = TypedDict(
    "DataSourceErrorMessageTypeDef",
    {
        "errorType": DataSourceErrorTypeType,
        "errorDetail": NotRequired[str],
    },
)
SingleSignOnTypeDef = TypedDict(
    "SingleSignOnTypeDef",
    {
        "type": NotRequired[AuthTypeType],
        "userAssignment": NotRequired[UserAssignmentType],
    },
)
EnvironmentParameterTypeDef = TypedDict(
    "EnvironmentParameterTypeDef",
    {
        "name": NotRequired[str],
        "value": NotRequired[str],
    },
)
CustomParameterTypeDef = TypedDict(
    "CustomParameterTypeDef",
    {
        "fieldType": str,
        "keyName": str,
        "defaultValue": NotRequired[str],
        "description": NotRequired[str],
        "isEditable": NotRequired[bool],
        "isOptional": NotRequired[bool],
    },
)
DeploymentPropertiesTypeDef = TypedDict(
    "DeploymentPropertiesTypeDef",
    {
        "endTimeoutMinutes": NotRequired[int],
        "startTimeoutMinutes": NotRequired[int],
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "type": str,
        "value": str,
        "name": NotRequired[str],
        "provider": NotRequired[str],
    },
)
ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "smithy": NotRequired[str],
    },
)
CreateGlossaryInputRequestTypeDef = TypedDict(
    "CreateGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "status": NotRequired[GlossaryStatusType],
    },
)
TermRelationsTypeDef = TypedDict(
    "TermRelationsTypeDef",
    {
        "classifies": NotRequired[Sequence[str]],
        "isA": NotRequired[Sequence[str]],
    },
)
CreateGroupProfileInputRequestTypeDef = TypedDict(
    "CreateGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
CreateListingChangeSetInputRequestTypeDef = TypedDict(
    "CreateListingChangeSetInputRequestTypeDef",
    {
        "action": ChangeActionType,
        "domainIdentifier": str,
        "entityIdentifier": str,
        "entityType": Literal["ASSET"],
        "clientToken": NotRequired[str],
        "entityRevision": NotRequired[str],
    },
)
CreateProjectInputRequestTypeDef = TypedDict(
    "CreateProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
    },
)
MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "groupIdentifier": NotRequired[str],
        "userIdentifier": NotRequired[str],
    },
)
ProjectDeletionErrorTypeDef = TypedDict(
    "ProjectDeletionErrorTypeDef",
    {
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)
SubscribedListingInputTypeDef = TypedDict(
    "SubscribedListingInputTypeDef",
    {
        "identifier": str,
    },
)
SubscriptionTargetFormTypeDef = TypedDict(
    "SubscriptionTargetFormTypeDef",
    {
        "content": str,
        "formName": str,
    },
)
CreateUserProfileInputRequestTypeDef = TypedDict(
    "CreateUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
        "clientToken": NotRequired[str],
        "userType": NotRequired[UserTypeType],
    },
)
DataProductItemTypeDef = TypedDict(
    "DataProductItemTypeDef",
    {
        "domainId": NotRequired[str],
        "itemId": NotRequired[str],
    },
)
RunStatisticsForAssetsTypeDef = TypedDict(
    "RunStatisticsForAssetsTypeDef",
    {
        "added": NotRequired[int],
        "failed": NotRequired[int],
        "skipped": NotRequired[int],
        "unchanged": NotRequired[int],
        "updated": NotRequired[int],
    },
)
DeleteAssetInputRequestTypeDef = TypedDict(
    "DeleteAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteAssetTypeInputRequestTypeDef = TypedDict(
    "DeleteAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteDataSourceInputRequestTypeDef = TypedDict(
    "DeleteDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "clientToken": NotRequired[str],
    },
)
DeleteDomainInputRequestTypeDef = TypedDict(
    "DeleteDomainInputRequestTypeDef",
    {
        "identifier": str,
        "clientToken": NotRequired[str],
        "skipDeletionCheck": NotRequired[bool],
    },
)
DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
    },
)
DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteEnvironmentProfileInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteFormTypeInputRequestTypeDef = TypedDict(
    "DeleteFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formTypeIdentifier": str,
    },
)
DeleteGlossaryInputRequestTypeDef = TypedDict(
    "DeleteGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteGlossaryTermInputRequestTypeDef = TypedDict(
    "DeleteGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteListingInputRequestTypeDef = TypedDict(
    "DeleteListingInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteProjectInputRequestTypeDef = TypedDict(
    "DeleteProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "skipDeletionCheck": NotRequired[bool],
    },
)
DeleteSubscriptionGrantInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteSubscriptionRequestInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
DeleteSubscriptionTargetInputRequestTypeDef = TypedDict(
    "DeleteSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
EnvironmentErrorTypeDef = TypedDict(
    "EnvironmentErrorTypeDef",
    {
        "message": str,
        "code": NotRequired[str],
    },
)
DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "managedAccountId": str,
        "name": str,
        "status": DomainStatusType,
        "description": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "portalUrl": NotRequired[str],
    },
)
EnvironmentBlueprintConfigurationItemTypeDef = TypedDict(
    "EnvironmentBlueprintConfigurationItemTypeDef",
    {
        "domainId": str,
        "environmentBlueprintId": str,
        "createdAt": NotRequired[datetime],
        "enabledRegions": NotRequired[List[str]],
        "manageAccessRoleArn": NotRequired[str],
        "provisioningRoleArn": NotRequired[str],
        "regionalParameters": NotRequired[Dict[str, Dict[str, str]]],
        "updatedAt": NotRequired[datetime],
    },
)
EnvironmentProfileSummaryTypeDef = TypedDict(
    "EnvironmentProfileSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "projectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "environmentProfileId": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
FailureCauseTypeDef = TypedDict(
    "FailureCauseTypeDef",
    {
        "message": NotRequired[str],
    },
)
FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "attribute": str,
        "value": str,
    },
)
FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "expression": str,
        "type": FilterExpressionTypeType,
    },
)
ImportTypeDef = TypedDict(
    "ImportTypeDef",
    {
        "name": str,
        "revision": str,
    },
)
GetAssetInputRequestTypeDef = TypedDict(
    "GetAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "revision": NotRequired[str],
    },
)
GetAssetTypeInputRequestTypeDef = TypedDict(
    "GetAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "revision": NotRequired[str],
    },
)
GetDataSourceInputRequestTypeDef = TypedDict(
    "GetDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetDataSourceRunInputRequestTypeDef = TypedDict(
    "GetDataSourceRunInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetDomainInputRequestTypeDef = TypedDict(
    "GetDomainInputRequestTypeDef",
    {
        "identifier": str,
    },
)
GetEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "GetEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
    },
)
GetEnvironmentBlueprintInputRequestTypeDef = TypedDict(
    "GetEnvironmentBlueprintInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetEnvironmentProfileInputRequestTypeDef = TypedDict(
    "GetEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetFormTypeInputRequestTypeDef = TypedDict(
    "GetFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formTypeIdentifier": str,
        "revision": NotRequired[str],
    },
)
GetGlossaryInputRequestTypeDef = TypedDict(
    "GetGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetGlossaryTermInputRequestTypeDef = TypedDict(
    "GetGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetGroupProfileInputRequestTypeDef = TypedDict(
    "GetGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
    },
)
GetIamPortalLoginUrlInputRequestTypeDef = TypedDict(
    "GetIamPortalLoginUrlInputRequestTypeDef",
    {
        "domainIdentifier": str,
    },
)
GetListingInputRequestTypeDef = TypedDict(
    "GetListingInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "listingRevision": NotRequired[str],
    },
)
GetProjectInputRequestTypeDef = TypedDict(
    "GetProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionGrantInputRequestTypeDef = TypedDict(
    "GetSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionInputRequestTypeDef = TypedDict(
    "GetSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionRequestDetailsInputRequestTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
    },
)
GetSubscriptionTargetInputRequestTypeDef = TypedDict(
    "GetSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
    },
)
GetUserProfileInputRequestTypeDef = TypedDict(
    "GetUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userIdentifier": str,
        "type": NotRequired[UserProfileTypeType],
    },
)
GlossaryItemTypeDef = TypedDict(
    "GlossaryItemTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
TermRelationsPaginatorTypeDef = TypedDict(
    "TermRelationsPaginatorTypeDef",
    {
        "classifies": NotRequired[List[str]],
        "isA": NotRequired[List[str]],
    },
)
ListingRevisionInputTypeDef = TypedDict(
    "ListingRevisionInputTypeDef",
    {
        "identifier": str,
        "revision": str,
    },
)
ListingRevisionTypeDef = TypedDict(
    "ListingRevisionTypeDef",
    {
        "id": str,
        "revision": str,
    },
)
GroupDetailsTypeDef = TypedDict(
    "GroupDetailsTypeDef",
    {
        "groupId": str,
    },
)
GroupProfileSummaryTypeDef = TypedDict(
    "GroupProfileSummaryTypeDef",
    {
        "domainId": NotRequired[str],
        "groupName": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[GroupProfileStatusType],
    },
)
IamUserProfileDetailsTypeDef = TypedDict(
    "IamUserProfileDetailsTypeDef",
    {
        "arn": NotRequired[str],
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
ListAssetRevisionsInputRequestTypeDef = TypedDict(
    "ListAssetRevisionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListDataSourceRunActivitiesInputRequestTypeDef = TypedDict(
    "ListDataSourceRunActivitiesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataAssetActivityStatusType],
    },
)
ListDataSourceRunsInputRequestTypeDef = TypedDict(
    "ListDataSourceRunsInputRequestTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataSourceRunStatusType],
    },
)
ListDataSourcesInputRequestTypeDef = TypedDict(
    "ListDataSourcesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "environmentIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
    },
)
ListDomainsInputRequestTypeDef = TypedDict(
    "ListDomainsInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "status": NotRequired[DomainStatusType],
    },
)
ListEnvironmentBlueprintConfigurationsInputRequestTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentBlueprintsInputRequestTypeDef = TypedDict(
    "ListEnvironmentBlueprintsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "managed": NotRequired[bool],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)
ListEnvironmentProfilesInputRequestTypeDef = TypedDict(
    "ListEnvironmentProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "projectIdentifier": NotRequired[str],
    },
)
ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "environmentProfileIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "provider": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
    },
)
TimestampTypeDef = Union[datetime, str]
ListProjectMembershipsInputRequestTypeDef = TypedDict(
    "ListProjectMembershipsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[Literal["NAME"]],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListProjectsInputRequestTypeDef = TypedDict(
    "ListProjectsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": NotRequired[str],
        "maxResults": NotRequired[int],
        "name": NotRequired[str],
        "nextToken": NotRequired[str],
        "userIdentifier": NotRequired[str],
    },
)
ListSubscriptionGrantsInputRequestTypeDef = TypedDict(
    "ListSubscriptionGrantsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "subscribedListingId": NotRequired[str],
        "subscriptionId": NotRequired[str],
        "subscriptionTargetId": NotRequired[str],
    },
)
ListSubscriptionRequestsInputRequestTypeDef = TypedDict(
    "ListSubscriptionRequestsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionRequestStatusType],
        "subscribedListingId": NotRequired[str],
    },
)
ListSubscriptionTargetsInputRequestTypeDef = TypedDict(
    "ListSubscriptionTargetsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
    },
)
ListSubscriptionsInputRequestTypeDef = TypedDict(
    "ListSubscriptionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionStatusType],
        "subscribedListingId": NotRequired[str],
        "subscriptionRequestIdentifier": NotRequired[str],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
UserDetailsTypeDef = TypedDict(
    "UserDetailsTypeDef",
    {
        "userId": str,
    },
)
NotificationResourceTypeDef = TypedDict(
    "NotificationResourceTypeDef",
    {
        "id": str,
        "type": Literal["PROJECT"],
        "name": NotRequired[str],
    },
)
PutEnvironmentBlueprintConfigurationInputRequestTypeDef = TypedDict(
    "PutEnvironmentBlueprintConfigurationInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "enabledRegions": Sequence[str],
        "environmentBlueprintIdentifier": str,
        "manageAccessRoleArn": NotRequired[str],
        "provisioningRoleArn": NotRequired[str],
        "regionalParameters": NotRequired[Mapping[str, Mapping[str, str]]],
    },
)
RedshiftClusterStorageTypeDef = TypedDict(
    "RedshiftClusterStorageTypeDef",
    {
        "clusterName": str,
    },
)
RedshiftCredentialConfigurationTypeDef = TypedDict(
    "RedshiftCredentialConfigurationTypeDef",
    {
        "secretManagerArn": str,
    },
)
RedshiftServerlessStorageTypeDef = TypedDict(
    "RedshiftServerlessStorageTypeDef",
    {
        "workgroupName": str,
    },
)
RejectChoiceTypeDef = TypedDict(
    "RejectChoiceTypeDef",
    {
        "predictionChoices": NotRequired[Sequence[int]],
        "predictionTarget": NotRequired[str],
    },
)
RejectRuleTypeDef = TypedDict(
    "RejectRuleTypeDef",
    {
        "rule": NotRequired[RejectRuleBehaviorType],
        "threshold": NotRequired[float],
    },
)
RejectSubscriptionRequestInputRequestTypeDef = TypedDict(
    "RejectSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "decisionComment": NotRequired[str],
    },
)
RevokeSubscriptionInputRequestTypeDef = TypedDict(
    "RevokeSubscriptionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "retainPermissions": NotRequired[bool],
    },
)
SearchGroupProfilesInputRequestTypeDef = TypedDict(
    "SearchGroupProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupType": GroupSearchTypeType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchText": NotRequired[str],
    },
)
SearchInItemTypeDef = TypedDict(
    "SearchInItemTypeDef",
    {
        "attribute": str,
    },
)
SearchSortTypeDef = TypedDict(
    "SearchSortTypeDef",
    {
        "attribute": str,
        "order": NotRequired[SortOrderType],
    },
)
SearchUserProfilesInputRequestTypeDef = TypedDict(
    "SearchUserProfilesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "userType": UserSearchTypeType,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchText": NotRequired[str],
    },
)
SsoUserProfileDetailsTypeDef = TypedDict(
    "SsoUserProfileDetailsTypeDef",
    {
        "firstName": NotRequired[str],
        "lastName": NotRequired[str],
        "username": NotRequired[str],
    },
)
StartDataSourceRunInputRequestTypeDef = TypedDict(
    "StartDataSourceRunInputRequestTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
        "clientToken": NotRequired[str],
    },
)
SubscribedProjectInputTypeDef = TypedDict(
    "SubscribedProjectInputTypeDef",
    {
        "identifier": NotRequired[str],
    },
)
SubscribedProjectTypeDef = TypedDict(
    "SubscribedProjectTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
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
UpdateEnvironmentInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
        "name": NotRequired[str],
    },
)
UpdateGlossaryInputRequestTypeDef = TypedDict(
    "UpdateGlossaryInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[GlossaryStatusType],
    },
)
UpdateGroupProfileInputRequestTypeDef = TypedDict(
    "UpdateGroupProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": str,
        "status": GroupProfileStatusType,
    },
)
UpdateProjectInputRequestTypeDef = TypedDict(
    "UpdateProjectInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
        "name": NotRequired[str],
    },
)
UpdateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "requestReason": str,
    },
)
UpdateUserProfileInputRequestTypeDef = TypedDict(
    "UpdateUserProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "status": UserProfileStatusType,
        "userIdentifier": str,
        "type": NotRequired[UserProfileTypeType],
    },
)
AcceptPredictionsInputRequestTypeDef = TypedDict(
    "AcceptPredictionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "acceptChoices": NotRequired[Sequence[AcceptChoiceTypeDef]],
        "acceptRule": NotRequired[AcceptRuleTypeDef],
        "clientToken": NotRequired[str],
        "revision": NotRequired[str],
    },
)
AcceptPredictionsOutputTypeDef = TypedDict(
    "AcceptPredictionsOutputTypeDef",
    {
        "assetId": str,
        "domainId": str,
        "revision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFormTypeOutputTypeDef = TypedDict(
    "CreateFormTypeOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGlossaryOutputTypeDef = TypedDict(
    "CreateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupProfileOutputTypeDef = TypedDict(
    "CreateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateListingChangeSetOutputTypeDef = TypedDict(
    "CreateListingChangeSetOutputTypeDef",
    {
        "listingId": str,
        "listingRevision": str,
        "status": ListingStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainOutputTypeDef = TypedDict(
    "DeleteDomainOutputTypeDef",
    {
        "status": DomainStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentBlueprintConfigurationOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintConfigurationOutputTypeDef",
    {
        "createdAt": datetime,
        "domainId": str,
        "enabledRegions": List[str],
        "environmentBlueprintId": str,
        "manageAccessRoleArn": str,
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlossaryOutputTypeDef = TypedDict(
    "GetGlossaryOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupProfileOutputTypeDef = TypedDict(
    "GetGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIamPortalLoginUrlOutputTypeDef = TypedDict(
    "GetIamPortalLoginUrlOutputTypeDef",
    {
        "authCodeUrl": str,
        "userProfileId": str,
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
PutEnvironmentBlueprintConfigurationOutputTypeDef = TypedDict(
    "PutEnvironmentBlueprintConfigurationOutputTypeDef",
    {
        "createdAt": datetime,
        "domainId": str,
        "enabledRegions": List[str],
        "environmentBlueprintId": str,
        "manageAccessRoleArn": str,
        "provisioningRoleArn": str,
        "regionalParameters": Dict[str, Dict[str, str]],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectPredictionsOutputTypeDef = TypedDict(
    "RejectPredictionsOutputTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "domainId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGlossaryOutputTypeDef = TypedDict(
    "UpdateGlossaryOutputTypeDef",
    {
        "description": str,
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "status": GlossaryStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGroupProfileOutputTypeDef = TypedDict(
    "UpdateGroupProfileOutputTypeDef",
    {
        "domainId": str,
        "groupName": str,
        "id": str,
        "status": GroupProfileStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetItemAdditionalAttributesTypeDef = TypedDict(
    "AssetItemAdditionalAttributesTypeDef",
    {
        "formsOutput": NotRequired[List[FormOutputTypeDef]],
        "readOnlyFormsOutput": NotRequired[List[FormOutputTypeDef]],
    },
)
GetAssetOutputTypeDef = TypedDict(
    "GetAssetOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetListingItemTypeDef = TypedDict(
    "AssetListingItemTypeDef",
    {
        "additionalAttributes": NotRequired[AssetListingItemAdditionalAttributesTypeDef],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "entityType": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "listingCreatedBy": NotRequired[str],
        "listingId": NotRequired[str],
        "listingRevision": NotRequired[str],
        "listingUpdatedBy": NotRequired[str],
        "name": NotRequired[str],
        "owningProjectId": NotRequired[str],
    },
)
AssetListingTypeDef = TypedDict(
    "AssetListingTypeDef",
    {
        "assetId": NotRequired[str],
        "assetRevision": NotRequired[str],
        "assetType": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "forms": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
        "owningProjectId": NotRequired[str],
    },
)
SubscribedAssetListingTypeDef = TypedDict(
    "SubscribedAssetListingTypeDef",
    {
        "entityId": NotRequired[str],
        "entityRevision": NotRequired[str],
        "entityType": NotRequired[str],
        "forms": NotRequired[str],
        "glossaryTerms": NotRequired[List[DetailedGlossaryTermTypeDef]],
    },
)
ListAssetRevisionsOutputTypeDef = TypedDict(
    "ListAssetRevisionsOutputTypeDef",
    {
        "items": List[AssetRevisionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssetTypeItemTypeDef = TypedDict(
    "AssetTypeItemTypeDef",
    {
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "name": str,
        "owningProjectId": str,
        "revision": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "originDomainId": NotRequired[str],
        "originProjectId": NotRequired[str],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
CreateAssetTypeOutputTypeDef = TypedDict(
    "CreateAssetTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAssetTypeOutputTypeDef = TypedDict(
    "GetAssetTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "formsOutput": Dict[str, FormEntryOutputTypeDef],
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PredictionConfigurationTypeDef = TypedDict(
    "PredictionConfigurationTypeDef",
    {
        "businessNameGeneration": NotRequired[BusinessNameGenerationConfigurationTypeDef],
    },
)
ProvisioningPropertiesTypeDef = TypedDict(
    "ProvisioningPropertiesTypeDef",
    {
        "cloudFormation": NotRequired[CloudFormationPropertiesTypeDef],
    },
)
ConfigurableEnvironmentActionTypeDef = TypedDict(
    "ConfigurableEnvironmentActionTypeDef",
    {
        "parameters": List[ConfigurableActionParameterTypeDef],
        "type": str,
        "auth": NotRequired[ConfigurableActionTypeAuthorizationType],
    },
)
CreateAssetTypeInputRequestTypeDef = TypedDict(
    "CreateAssetTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "formsInput": Mapping[str, FormEntryInputTypeDef],
        "name": str,
        "owningProjectIdentifier": str,
        "description": NotRequired[str],
    },
)
DataSourceRunActivityTypeDef = TypedDict(
    "DataSourceRunActivityTypeDef",
    {
        "createdAt": datetime,
        "dataAssetStatus": DataAssetActivityStatusType,
        "dataSourceRunId": str,
        "database": str,
        "projectId": str,
        "technicalName": str,
        "updatedAt": datetime,
        "dataAssetId": NotRequired[str],
        "errorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "technicalDescription": NotRequired[str],
    },
)
DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "dataSourceId": str,
        "domainId": str,
        "environmentId": str,
        "name": str,
        "status": DataSourceStatusType,
        "type": str,
        "createdAt": NotRequired[datetime],
        "enableSetting": NotRequired[EnableSettingType],
        "lastRunAssetCount": NotRequired[int],
        "lastRunAt": NotRequired[datetime],
        "lastRunErrorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "lastRunStatus": NotRequired[DataSourceRunStatusType],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
        "updatedAt": NotRequired[datetime],
    },
)
CreateDomainInputRequestTypeDef = TypedDict(
    "CreateDomainInputRequestTypeDef",
    {
        "domainExecutionRole": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "kmsKeyIdentifier": NotRequired[str],
        "singleSignOn": NotRequired[SingleSignOnTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateDomainOutputTypeDef = TypedDict(
    "CreateDomainOutputTypeDef",
    {
        "arn": str,
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "kmsKeyIdentifier": str,
        "name": str,
        "portalUrl": str,
        "singleSignOn": SingleSignOnTypeDef,
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainOutputTypeDef = TypedDict(
    "GetDomainOutputTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "kmsKeyIdentifier": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "portalUrl": str,
        "singleSignOn": SingleSignOnTypeDef,
        "status": DomainStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainInputRequestTypeDef = TypedDict(
    "UpdateDomainInputRequestTypeDef",
    {
        "identifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "domainExecutionRole": NotRequired[str],
        "name": NotRequired[str],
        "singleSignOn": NotRequired[SingleSignOnTypeDef],
    },
)
UpdateDomainOutputTypeDef = TypedDict(
    "UpdateDomainOutputTypeDef",
    {
        "description": str,
        "domainExecutionRole": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "singleSignOn": SingleSignOnTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentInputRequestTypeDef = TypedDict(
    "CreateEnvironmentInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentProfileIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[Sequence[str]],
        "userParameters": NotRequired[Sequence[EnvironmentParameterTypeDef]],
    },
)
CreateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "CreateEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentBlueprintIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "description": NotRequired[str],
        "userParameters": NotRequired[Sequence[EnvironmentParameterTypeDef]],
    },
)
UpdateEnvironmentProfileInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentProfileInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "description": NotRequired[str],
        "name": NotRequired[str],
        "userParameters": NotRequired[Sequence[EnvironmentParameterTypeDef]],
    },
)
CreateEnvironmentProfileOutputTypeDef = TypedDict(
    "CreateEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentProfileOutputTypeDef = TypedDict(
    "GetEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentProfileOutputTypeDef = TypedDict(
    "UpdateEnvironmentProfileOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "environmentBlueprintId": str,
        "id": str,
        "name": str,
        "projectId": str,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFormTypeInputRequestTypeDef = TypedDict(
    "CreateFormTypeInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "model": ModelTypeDef,
        "name": str,
        "owningProjectIdentifier": str,
        "description": NotRequired[str],
        "status": NotRequired[FormTypeStatusType],
    },
)
CreateGlossaryTermInputRequestTypeDef = TypedDict(
    "CreateGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "glossaryIdentifier": str,
        "name": str,
        "clientToken": NotRequired[str],
        "longDescription": NotRequired[str],
        "shortDescription": NotRequired[str],
        "status": NotRequired[GlossaryTermStatusType],
        "termRelations": NotRequired[TermRelationsTypeDef],
    },
)
CreateGlossaryTermOutputTypeDef = TypedDict(
    "CreateGlossaryTermOutputTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGlossaryTermOutputTypeDef = TypedDict(
    "GetGlossaryTermOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsTypeDef,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlossaryTermItemTypeDef = TypedDict(
    "GlossaryTermItemTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "name": str,
        "status": GlossaryTermStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "longDescription": NotRequired[str],
        "shortDescription": NotRequired[str],
        "termRelations": NotRequired[TermRelationsTypeDef],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
UpdateGlossaryTermInputRequestTypeDef = TypedDict(
    "UpdateGlossaryTermInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "glossaryIdentifier": NotRequired[str],
        "longDescription": NotRequired[str],
        "name": NotRequired[str],
        "shortDescription": NotRequired[str],
        "status": NotRequired[GlossaryTermStatusType],
        "termRelations": NotRequired[TermRelationsTypeDef],
    },
)
UpdateGlossaryTermOutputTypeDef = TypedDict(
    "UpdateGlossaryTermOutputTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "longDescription": str,
        "name": str,
        "shortDescription": str,
        "status": GlossaryTermStatusType,
        "termRelations": TermRelationsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProjectMembershipInputRequestTypeDef = TypedDict(
    "CreateProjectMembershipInputRequestTypeDef",
    {
        "designation": UserDesignationType,
        "domainIdentifier": str,
        "member": MemberTypeDef,
        "projectIdentifier": str,
    },
)
DeleteProjectMembershipInputRequestTypeDef = TypedDict(
    "DeleteProjectMembershipInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "member": MemberTypeDef,
        "projectIdentifier": str,
    },
)
CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProjectOutputTypeDef = TypedDict(
    "GetProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "createdBy": str,
        "domainId": str,
        "id": str,
        "name": str,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "failureReasons": NotRequired[List[ProjectDeletionErrorTypeDef]],
        "projectStatus": NotRequired[ProjectStatusType],
        "updatedAt": NotRequired[datetime],
    },
)
UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "failureReasons": List[ProjectDeletionErrorTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "projectStatus": ProjectStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "CreateSubscriptionTargetInputRequestTypeDef",
    {
        "applicableAssetTypes": Sequence[str],
        "authorizedPrincipals": Sequence[str],
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "manageAccessRole": str,
        "name": str,
        "subscriptionTargetConfig": Sequence[SubscriptionTargetFormTypeDef],
        "type": str,
        "clientToken": NotRequired[str],
        "provider": NotRequired[str],
    },
)
CreateSubscriptionTargetOutputTypeDef = TypedDict(
    "CreateSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionTargetOutputTypeDef = TypedDict(
    "GetSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionTargetSummaryTypeDef = TypedDict(
    "SubscriptionTargetSummaryTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionTargetInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionTargetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "identifier": str,
        "applicableAssetTypes": NotRequired[Sequence[str]],
        "authorizedPrincipals": NotRequired[Sequence[str]],
        "manageAccessRole": NotRequired[str],
        "name": NotRequired[str],
        "provider": NotRequired[str],
        "subscriptionTargetConfig": NotRequired[Sequence[SubscriptionTargetFormTypeDef]],
    },
)
UpdateSubscriptionTargetOutputTypeDef = TypedDict(
    "UpdateSubscriptionTargetOutputTypeDef",
    {
        "applicableAssetTypes": List[str],
        "authorizedPrincipals": List[str],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "environmentId": str,
        "id": str,
        "manageAccessRole": str,
        "name": str,
        "projectId": str,
        "provider": str,
        "subscriptionTargetConfig": List[SubscriptionTargetFormTypeDef],
        "type": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataProductSummaryTypeDef = TypedDict(
    "DataProductSummaryTypeDef",
    {
        "domainId": str,
        "id": str,
        "name": str,
        "owningProjectId": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "dataProductItems": NotRequired[List[DataProductItemTypeDef]],
        "description": NotRequired[str],
        "glossaryTerms": NotRequired[List[str]],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
DataSourceRunSummaryTypeDef = TypedDict(
    "DataSourceRunSummaryTypeDef",
    {
        "createdAt": datetime,
        "dataSourceId": str,
        "id": str,
        "projectId": str,
        "status": DataSourceRunStatusType,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "errorMessage": NotRequired[DataSourceErrorMessageTypeDef],
        "runStatisticsForAssets": NotRequired[RunStatisticsForAssetsTypeDef],
        "startedAt": NotRequired[datetime],
        "stoppedAt": NotRequired[datetime],
    },
)
GetDataSourceRunOutputTypeDef = TypedDict(
    "GetDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": RunStatisticsForAssetsTypeDef,
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDataSourceRunOutputTypeDef = TypedDict(
    "StartDataSourceRunOutputTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfigurationSnapshot": str,
        "dataSourceId": str,
        "domainId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "projectId": str,
        "runStatisticsForAssets": RunStatisticsForAssetsTypeDef,
        "startedAt": datetime,
        "status": DataSourceRunStatusType,
        "stoppedAt": datetime,
        "type": DataSourceRunTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "deploymentId": NotRequired[str],
        "deploymentStatus": NotRequired[DeploymentStatusType],
        "deploymentType": NotRequired[DeploymentTypeType],
        "failureReason": NotRequired[EnvironmentErrorTypeDef],
        "isDeploymentComplete": NotRequired[bool],
        "messages": NotRequired[List[str]],
    },
)
ListDomainsOutputTypeDef = TypedDict(
    "ListDomainsOutputTypeDef",
    {
        "items": List[DomainSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentBlueprintConfigurationsOutputTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsOutputTypeDef",
    {
        "items": List[EnvironmentBlueprintConfigurationItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentProfilesOutputTypeDef = TypedDict(
    "ListEnvironmentProfilesOutputTypeDef",
    {
        "items": List[EnvironmentProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "items": List[EnvironmentSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribedAssetTypeDef = TypedDict(
    "SubscribedAssetTypeDef",
    {
        "assetId": str,
        "assetRevision": str,
        "status": SubscriptionGrantStatusType,
        "failureCause": NotRequired[FailureCauseTypeDef],
        "failureTimestamp": NotRequired[datetime],
        "grantedTimestamp": NotRequired[datetime],
        "targetName": NotRequired[str],
    },
)
UpdateSubscriptionGrantStatusInputRequestTypeDef = TypedDict(
    "UpdateSubscriptionGrantStatusInputRequestTypeDef",
    {
        "assetIdentifier": str,
        "domainIdentifier": str,
        "identifier": str,
        "status": SubscriptionGrantStatusType,
        "failureCause": NotRequired[FailureCauseTypeDef],
        "targetName": NotRequired[str],
    },
)
FilterClauseTypeDef = TypedDict(
    "FilterClauseTypeDef",
    {
        "and": NotRequired[Sequence[Dict[str, Any]]],
        "filter": NotRequired[FilterTypeDef],
        "or": NotRequired[Sequence[Dict[str, Any]]],
    },
)
RelationalFilterConfigurationTypeDef = TypedDict(
    "RelationalFilterConfigurationTypeDef",
    {
        "databaseName": str,
        "filterExpressions": NotRequired[Sequence[FilterExpressionTypeDef]],
        "schemaName": NotRequired[str],
    },
)
FormTypeDataTypeDef = TypedDict(
    "FormTypeDataTypeDef",
    {
        "domainId": str,
        "name": str,
        "revision": str,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "imports": NotRequired[List[ImportTypeDef]],
        "model": NotRequired[ModelTypeDef],
        "originDomainId": NotRequired[str],
        "originProjectId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "status": NotRequired[FormTypeStatusType],
    },
)
GetFormTypeOutputTypeDef = TypedDict(
    "GetFormTypeOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "imports": List[ImportTypeDef],
        "model": ModelTypeDef,
        "name": str,
        "originDomainId": str,
        "originProjectId": str,
        "owningProjectId": str,
        "revision": str,
        "status": FormTypeStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GlossaryTermItemPaginatorTypeDef = TypedDict(
    "GlossaryTermItemPaginatorTypeDef",
    {
        "domainId": str,
        "glossaryId": str,
        "id": str,
        "name": str,
        "status": GlossaryTermStatusType,
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "longDescription": NotRequired[str],
        "shortDescription": NotRequired[str],
        "termRelations": NotRequired[TermRelationsPaginatorTypeDef],
        "updatedAt": NotRequired[datetime],
        "updatedBy": NotRequired[str],
    },
)
GrantedEntityInputTypeDef = TypedDict(
    "GrantedEntityInputTypeDef",
    {
        "listing": NotRequired[ListingRevisionInputTypeDef],
    },
)
GrantedEntityTypeDef = TypedDict(
    "GrantedEntityTypeDef",
    {
        "listing": NotRequired[ListingRevisionTypeDef],
    },
)
SearchGroupProfilesOutputTypeDef = TypedDict(
    "SearchGroupProfilesOutputTypeDef",
    {
        "items": List[GroupProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef = TypedDict(
    "ListAssetRevisionsInputListAssetRevisionsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef = TypedDict(
    "ListDataSourceRunActivitiesInputListDataSourceRunActivitiesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "status": NotRequired[DataAssetActivityStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef = TypedDict(
    "ListDataSourceRunsInputListDataSourceRunsPaginateTypeDef",
    {
        "dataSourceIdentifier": str,
        "domainIdentifier": str,
        "status": NotRequired[DataSourceRunStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDataSourcesInputListDataSourcesPaginateTypeDef = TypedDict(
    "ListDataSourcesInputListDataSourcesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "environmentIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "status": NotRequired[DataSourceStatusType],
        "type": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDomainsInputListDomainsPaginateTypeDef = TypedDict(
    "ListDomainsInputListDomainsPaginateTypeDef",
    {
        "status": NotRequired[DomainStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef = TypedDict(
    "ListEnvironmentBlueprintConfigurationsInputListEnvironmentBlueprintConfigurationsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef = TypedDict(
    "ListEnvironmentBlueprintsInputListEnvironmentBlueprintsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "managed": NotRequired[bool],
        "name": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef = TypedDict(
    "ListEnvironmentProfilesInputListEnvironmentProfilesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "projectIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEnvironmentsInputListEnvironmentsPaginateTypeDef = TypedDict(
    "ListEnvironmentsInputListEnvironmentsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "awsAccountId": NotRequired[str],
        "awsAccountRegion": NotRequired[str],
        "environmentBlueprintIdentifier": NotRequired[str],
        "environmentProfileIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "provider": NotRequired[str],
        "status": NotRequired[EnvironmentStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef = TypedDict(
    "ListProjectMembershipsInputListProjectMembershipsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "projectIdentifier": str,
        "sortBy": NotRequired[Literal["NAME"]],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProjectsInputListProjectsPaginateTypeDef = TypedDict(
    "ListProjectsInputListProjectsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "groupIdentifier": NotRequired[str],
        "name": NotRequired[str],
        "userIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef = TypedDict(
    "ListSubscriptionGrantsInputListSubscriptionGrantsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "environmentId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "subscribedListingId": NotRequired[str],
        "subscriptionId": NotRequired[str],
        "subscriptionTargetId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef = TypedDict(
    "ListSubscriptionRequestsInputListSubscriptionRequestsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionRequestStatusType],
        "subscribedListingId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef = TypedDict(
    "ListSubscriptionTargetsInputListSubscriptionTargetsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSubscriptionsInputListSubscriptionsPaginateTypeDef = TypedDict(
    "ListSubscriptionsInputListSubscriptionsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "approverProjectId": NotRequired[str],
        "owningProjectId": NotRequired[str],
        "sortBy": NotRequired[SortKeyType],
        "sortOrder": NotRequired[SortOrderType],
        "status": NotRequired[SubscriptionStatusType],
        "subscribedListingId": NotRequired[str],
        "subscriptionRequestIdentifier": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef = TypedDict(
    "SearchGroupProfilesInputSearchGroupProfilesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "groupType": GroupSearchTypeType,
        "searchText": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchUserProfilesInputSearchUserProfilesPaginateTypeDef = TypedDict(
    "SearchUserProfilesInputSearchUserProfilesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "userType": UserSearchTypeType,
        "searchText": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationsInputListNotificationsPaginateTypeDef = TypedDict(
    "ListNotificationsInputListNotificationsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
        "afterTimestamp": NotRequired[TimestampTypeDef],
        "beforeTimestamp": NotRequired[TimestampTypeDef],
        "subjects": NotRequired[Sequence[str]],
        "taskStatus": NotRequired[TaskStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListNotificationsInputRequestTypeDef = TypedDict(
    "ListNotificationsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "type": NotificationTypeType,
        "afterTimestamp": NotRequired[TimestampTypeDef],
        "beforeTimestamp": NotRequired[TimestampTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "subjects": NotRequired[Sequence[str]],
        "taskStatus": NotRequired[TaskStatusType],
    },
)
MemberDetailsTypeDef = TypedDict(
    "MemberDetailsTypeDef",
    {
        "group": NotRequired[GroupDetailsTypeDef],
        "user": NotRequired[UserDetailsTypeDef],
    },
)
TopicTypeDef = TypedDict(
    "TopicTypeDef",
    {
        "resource": NotificationResourceTypeDef,
        "role": NotificationRoleType,
        "subject": str,
    },
)
RedshiftStorageTypeDef = TypedDict(
    "RedshiftStorageTypeDef",
    {
        "redshiftClusterSource": NotRequired[RedshiftClusterStorageTypeDef],
        "redshiftServerlessSource": NotRequired[RedshiftServerlessStorageTypeDef],
    },
)
RejectPredictionsInputRequestTypeDef = TypedDict(
    "RejectPredictionsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "clientToken": NotRequired[str],
        "rejectChoices": NotRequired[Sequence[RejectChoiceTypeDef]],
        "rejectRule": NotRequired[RejectRuleTypeDef],
        "revision": NotRequired[str],
    },
)
SearchInputRequestTypeDef = TypedDict(
    "SearchInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "searchScope": InventorySearchScopeType,
        "additionalAttributes": NotRequired[Sequence[Literal["FORMS"]]],
        "filters": NotRequired["FilterClauseTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "owningProjectIdentifier": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
    },
)
SearchListingsInputRequestTypeDef = TypedDict(
    "SearchListingsInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "additionalAttributes": NotRequired[Sequence[Literal["FORMS"]]],
        "filters": NotRequired["FilterClauseTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
    },
)
SearchTypesInputRequestTypeDef = TypedDict(
    "SearchTypesInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "managed": bool,
        "searchScope": TypesSearchScopeType,
        "filters": NotRequired["FilterClauseTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
    },
)
UserProfileDetailsTypeDef = TypedDict(
    "UserProfileDetailsTypeDef",
    {
        "iam": NotRequired[IamUserProfileDetailsTypeDef],
        "sso": NotRequired[SsoUserProfileDetailsTypeDef],
    },
)
SubscribedPrincipalInputTypeDef = TypedDict(
    "SubscribedPrincipalInputTypeDef",
    {
        "project": NotRequired[SubscribedProjectInputTypeDef],
    },
)
SubscribedPrincipalTypeDef = TypedDict(
    "SubscribedPrincipalTypeDef",
    {
        "project": NotRequired[SubscribedProjectTypeDef],
    },
)
AssetItemTypeDef = TypedDict(
    "AssetItemTypeDef",
    {
        "domainId": str,
        "identifier": str,
        "name": str,
        "owningProjectId": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "additionalAttributes": NotRequired[AssetItemAdditionalAttributesTypeDef],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "description": NotRequired[str],
        "externalIdentifier": NotRequired[str],
        "firstRevisionCreatedAt": NotRequired[datetime],
        "firstRevisionCreatedBy": NotRequired[str],
        "glossaryTerms": NotRequired[List[str]],
    },
)
SearchResultItemTypeDef = TypedDict(
    "SearchResultItemTypeDef",
    {
        "assetListing": NotRequired[AssetListingItemTypeDef],
    },
)
ListingItemTypeDef = TypedDict(
    "ListingItemTypeDef",
    {
        "assetListing": NotRequired[AssetListingTypeDef],
    },
)
SubscribedListingItemTypeDef = TypedDict(
    "SubscribedListingItemTypeDef",
    {
        "assetListing": NotRequired[SubscribedAssetListingTypeDef],
    },
)
CreateAssetInputRequestTypeDef = TypedDict(
    "CreateAssetInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "name": str,
        "owningProjectIdentifier": str,
        "typeIdentifier": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "externalIdentifier": NotRequired[str],
        "formsInput": NotRequired[Sequence[FormInputTypeDef]],
        "glossaryTerms": NotRequired[Sequence[str]],
        "predictionConfiguration": NotRequired[PredictionConfigurationTypeDef],
        "typeRevision": NotRequired[str],
    },
)
CreateAssetOutputTypeDef = TypedDict(
    "CreateAssetOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": PredictionConfigurationTypeDef,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateAssetRevisionInputRequestTypeDef = TypedDict(
    "CreateAssetRevisionInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "formsInput": NotRequired[Sequence[FormInputTypeDef]],
        "glossaryTerms": NotRequired[Sequence[str]],
        "predictionConfiguration": NotRequired[PredictionConfigurationTypeDef],
        "typeRevision": NotRequired[str],
    },
)
CreateAssetRevisionOutputTypeDef = TypedDict(
    "CreateAssetRevisionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "externalIdentifier": str,
        "firstRevisionCreatedAt": datetime,
        "firstRevisionCreatedBy": str,
        "formsOutput": List[FormOutputTypeDef],
        "glossaryTerms": List[str],
        "id": str,
        "listing": AssetListingDetailsTypeDef,
        "name": str,
        "owningProjectId": str,
        "predictionConfiguration": PredictionConfigurationTypeDef,
        "readOnlyFormsOutput": List[FormOutputTypeDef],
        "revision": str,
        "typeIdentifier": str,
        "typeRevision": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnvironmentBlueprintSummaryTypeDef = TypedDict(
    "EnvironmentBlueprintSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "updatedAt": NotRequired[datetime],
    },
)
GetEnvironmentBlueprintOutputTypeDef = TypedDict(
    "GetEnvironmentBlueprintOutputTypeDef",
    {
        "createdAt": datetime,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "glossaryTerms": List[str],
        "id": str,
        "name": str,
        "provider": str,
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourceRunActivitiesOutputTypeDef = TypedDict(
    "ListDataSourceRunActivitiesOutputTypeDef",
    {
        "items": List[DataSourceRunActivityTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourcesOutputTypeDef = TypedDict(
    "ListDataSourcesOutputTypeDef",
    {
        "items": List[DataSourceSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {
        "items": List[ProjectSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionTargetsOutputTypeDef = TypedDict(
    "ListSubscriptionTargetsOutputTypeDef",
    {
        "items": List[SubscriptionTargetSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDataSourceRunsOutputTypeDef = TypedDict(
    "ListDataSourceRunsOutputTypeDef",
    {
        "items": List[DataSourceRunSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "awsAccountId": str,
        "awsAccountRegion": str,
        "createdAt": datetime,
        "createdBy": str,
        "deploymentProperties": DeploymentPropertiesTypeDef,
        "description": str,
        "domainId": str,
        "environmentActions": List[ConfigurableEnvironmentActionTypeDef],
        "environmentBlueprintId": str,
        "environmentProfileId": str,
        "glossaryTerms": List[str],
        "id": str,
        "lastDeployment": DeploymentTypeDef,
        "name": str,
        "projectId": str,
        "provider": str,
        "provisionedResources": List[ResourceTypeDef],
        "provisioningProperties": ProvisioningPropertiesTypeDef,
        "status": EnvironmentStatusType,
        "updatedAt": datetime,
        "userParameters": List[CustomParameterTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchInputSearchPaginateTypeDef = TypedDict(
    "SearchInputSearchPaginateTypeDef",
    {
        "domainIdentifier": str,
        "searchScope": InventorySearchScopeType,
        "additionalAttributes": NotRequired[Sequence[Literal["FORMS"]]],
        "filters": NotRequired[FilterClauseTypeDef],
        "owningProjectIdentifier": NotRequired[str],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchListingsInputSearchListingsPaginateTypeDef = TypedDict(
    "SearchListingsInputSearchListingsPaginateTypeDef",
    {
        "domainIdentifier": str,
        "additionalAttributes": NotRequired[Sequence[Literal["FORMS"]]],
        "filters": NotRequired[FilterClauseTypeDef],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchTypesInputSearchTypesPaginateTypeDef = TypedDict(
    "SearchTypesInputSearchTypesPaginateTypeDef",
    {
        "domainIdentifier": str,
        "managed": bool,
        "searchScope": TypesSearchScopeType,
        "filters": NotRequired[FilterClauseTypeDef],
        "searchIn": NotRequired[Sequence[SearchInItemTypeDef]],
        "searchText": NotRequired[str],
        "sort": NotRequired[SearchSortTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GlueRunConfigurationInputTypeDef = TypedDict(
    "GlueRunConfigurationInputTypeDef",
    {
        "relationalFilterConfigurations": Sequence[RelationalFilterConfigurationTypeDef],
        "dataAccessRole": NotRequired[str],
    },
)
GlueRunConfigurationOutputTypeDef = TypedDict(
    "GlueRunConfigurationOutputTypeDef",
    {
        "relationalFilterConfigurations": List[RelationalFilterConfigurationTypeDef],
        "accountId": NotRequired[str],
        "dataAccessRole": NotRequired[str],
        "region": NotRequired[str],
    },
)
SearchTypesResultItemTypeDef = TypedDict(
    "SearchTypesResultItemTypeDef",
    {
        "assetTypeItem": NotRequired[AssetTypeItemTypeDef],
        "formTypeItem": NotRequired[FormTypeDataTypeDef],
    },
)
CreateSubscriptionGrantInputRequestTypeDef = TypedDict(
    "CreateSubscriptionGrantInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "grantedEntity": GrantedEntityInputTypeDef,
        "subscriptionTargetIdentifier": str,
        "assetTargetNames": NotRequired[Sequence[AssetTargetNameMapTypeDef]],
        "clientToken": NotRequired[str],
    },
)
CreateSubscriptionGrantOutputTypeDef = TypedDict(
    "CreateSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSubscriptionGrantOutputTypeDef = TypedDict(
    "DeleteSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionGrantOutputTypeDef = TypedDict(
    "GetSubscriptionGrantOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionGrantSummaryTypeDef = TypedDict(
    "SubscriptionGrantSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "assets": NotRequired[List[SubscribedAssetTypeDef]],
        "subscriptionId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionGrantStatusOutputTypeDef = TypedDict(
    "UpdateSubscriptionGrantStatusOutputTypeDef",
    {
        "assets": List[SubscribedAssetTypeDef],
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "grantedEntity": GrantedEntityTypeDef,
        "id": str,
        "status": SubscriptionGrantOverallStatusType,
        "subscriptionId": str,
        "subscriptionTargetId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ProjectMemberTypeDef = TypedDict(
    "ProjectMemberTypeDef",
    {
        "designation": UserDesignationType,
        "memberDetails": MemberDetailsTypeDef,
    },
)
NotificationOutputTypeDef = TypedDict(
    "NotificationOutputTypeDef",
    {
        "actionLink": str,
        "creationTimestamp": datetime,
        "domainIdentifier": str,
        "identifier": str,
        "lastUpdatedTimestamp": datetime,
        "message": str,
        "title": str,
        "topic": TopicTypeDef,
        "type": NotificationTypeType,
        "metadata": NotRequired[Dict[str, str]],
        "status": NotRequired[TaskStatusType],
    },
)
RedshiftRunConfigurationInputTypeDef = TypedDict(
    "RedshiftRunConfigurationInputTypeDef",
    {
        "redshiftCredentialConfiguration": RedshiftCredentialConfigurationTypeDef,
        "redshiftStorage": RedshiftStorageTypeDef,
        "relationalFilterConfigurations": Sequence[RelationalFilterConfigurationTypeDef],
        "dataAccessRole": NotRequired[str],
    },
)
RedshiftRunConfigurationOutputTypeDef = TypedDict(
    "RedshiftRunConfigurationOutputTypeDef",
    {
        "redshiftCredentialConfiguration": RedshiftCredentialConfigurationTypeDef,
        "redshiftStorage": RedshiftStorageTypeDef,
        "relationalFilterConfigurations": List[RelationalFilterConfigurationTypeDef],
        "accountId": NotRequired[str],
        "dataAccessRole": NotRequired[str],
        "region": NotRequired[str],
    },
)
CreateUserProfileOutputTypeDef = TypedDict(
    "CreateUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserProfileOutputTypeDef = TypedDict(
    "GetUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateUserProfileOutputTypeDef = TypedDict(
    "UpdateUserProfileOutputTypeDef",
    {
        "details": UserProfileDetailsTypeDef,
        "domainId": str,
        "id": str,
        "status": UserProfileStatusType,
        "type": UserProfileTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "details": NotRequired[UserProfileDetailsTypeDef],
        "domainId": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[UserProfileStatusType],
        "type": NotRequired[UserProfileTypeType],
    },
)
CreateSubscriptionRequestInputRequestTypeDef = TypedDict(
    "CreateSubscriptionRequestInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "requestReason": str,
        "subscribedListings": Sequence[SubscribedListingInputTypeDef],
        "subscribedPrincipals": Sequence[SubscribedPrincipalInputTypeDef],
        "clientToken": NotRequired[str],
    },
)
SearchInventoryResultItemPaginatorTypeDef = TypedDict(
    "SearchInventoryResultItemPaginatorTypeDef",
    {
        "assetItem": NotRequired[AssetItemTypeDef],
        "dataProductItem": NotRequired[DataProductSummaryTypeDef],
        "glossaryItem": NotRequired[GlossaryItemTypeDef],
        "glossaryTermItem": NotRequired[GlossaryTermItemPaginatorTypeDef],
    },
)
SearchInventoryResultItemTypeDef = TypedDict(
    "SearchInventoryResultItemTypeDef",
    {
        "assetItem": NotRequired[AssetItemTypeDef],
        "dataProductItem": NotRequired[DataProductSummaryTypeDef],
        "glossaryItem": NotRequired[GlossaryItemTypeDef],
        "glossaryTermItem": NotRequired[GlossaryTermItemTypeDef],
    },
)
SearchListingsOutputTypeDef = TypedDict(
    "SearchListingsOutputTypeDef",
    {
        "items": List[SearchResultItemTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListingOutputTypeDef = TypedDict(
    "GetListingOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "domainId": str,
        "id": str,
        "item": ListingItemTypeDef,
        "listingRevision": str,
        "name": str,
        "status": ListingStatusType,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribedListingTypeDef = TypedDict(
    "SubscribedListingTypeDef",
    {
        "description": str,
        "id": str,
        "item": SubscribedListingItemTypeDef,
        "name": str,
        "ownerProjectId": str,
        "ownerProjectName": NotRequired[str],
        "revision": NotRequired[str],
    },
)
ListEnvironmentBlueprintsOutputTypeDef = TypedDict(
    "ListEnvironmentBlueprintsOutputTypeDef",
    {
        "items": List[EnvironmentBlueprintSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchTypesOutputTypeDef = TypedDict(
    "SearchTypesOutputTypeDef",
    {
        "items": List[SearchTypesResultItemTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionGrantsOutputTypeDef = TypedDict(
    "ListSubscriptionGrantsOutputTypeDef",
    {
        "items": List[SubscriptionGrantSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProjectMembershipsOutputTypeDef = TypedDict(
    "ListProjectMembershipsOutputTypeDef",
    {
        "members": List[ProjectMemberTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListNotificationsOutputTypeDef = TypedDict(
    "ListNotificationsOutputTypeDef",
    {
        "nextToken": str,
        "notifications": List[NotificationOutputTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DataSourceConfigurationInputTypeDef = TypedDict(
    "DataSourceConfigurationInputTypeDef",
    {
        "glueRunConfiguration": NotRequired[GlueRunConfigurationInputTypeDef],
        "redshiftRunConfiguration": NotRequired[RedshiftRunConfigurationInputTypeDef],
    },
)
DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "glueRunConfiguration": NotRequired[GlueRunConfigurationOutputTypeDef],
        "redshiftRunConfiguration": NotRequired[RedshiftRunConfigurationOutputTypeDef],
    },
)
SearchUserProfilesOutputTypeDef = TypedDict(
    "SearchUserProfilesOutputTypeDef",
    {
        "items": List[UserProfileSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchOutputPaginatorTypeDef = TypedDict(
    "SearchOutputPaginatorTypeDef",
    {
        "items": List[SearchInventoryResultItemPaginatorTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchOutputTypeDef = TypedDict(
    "SearchOutputTypeDef",
    {
        "items": List[SearchInventoryResultItemTypeDef],
        "nextToken": str,
        "totalMatchCount": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AcceptSubscriptionRequestOutputTypeDef = TypedDict(
    "AcceptSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelSubscriptionOutputTypeDef = TypedDict(
    "CancelSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSubscriptionRequestOutputTypeDef = TypedDict(
    "CreateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionOutputTypeDef = TypedDict(
    "GetSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSubscriptionRequestDetailsOutputTypeDef = TypedDict(
    "GetSubscriptionRequestDetailsOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RejectSubscriptionRequestOutputTypeDef = TypedDict(
    "RejectSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RevokeSubscriptionOutputTypeDef = TypedDict(
    "RevokeSubscriptionOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "retainPermissions": bool,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "subscriptionRequestId": str,
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscriptionRequestSummaryTypeDef = TypedDict(
    "SubscriptionRequestSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "decisionComment": NotRequired[str],
        "reviewerId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
SubscriptionSummaryTypeDef = TypedDict(
    "SubscriptionSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "domainId": str,
        "id": str,
        "status": SubscriptionStatusType,
        "subscribedListing": SubscribedListingTypeDef,
        "subscribedPrincipal": SubscribedPrincipalTypeDef,
        "updatedAt": datetime,
        "retainPermissions": NotRequired[bool],
        "subscriptionRequestId": NotRequired[str],
        "updatedBy": NotRequired[str],
    },
)
UpdateSubscriptionRequestOutputTypeDef = TypedDict(
    "UpdateSubscriptionRequestOutputTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "decisionComment": str,
        "domainId": str,
        "id": str,
        "requestReason": str,
        "reviewerId": str,
        "status": SubscriptionRequestStatusType,
        "subscribedListings": List[SubscribedListingTypeDef],
        "subscribedPrincipals": List[SubscribedPrincipalTypeDef],
        "updatedAt": datetime,
        "updatedBy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDataSourceInputRequestTypeDef = TypedDict(
    "CreateDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "environmentIdentifier": str,
        "name": str,
        "projectIdentifier": str,
        "type": str,
        "assetFormsInput": NotRequired[Sequence[FormInputTypeDef]],
        "clientToken": NotRequired[str],
        "configuration": NotRequired[DataSourceConfigurationInputTypeDef],
        "description": NotRequired[str],
        "enableSetting": NotRequired[EnableSettingType],
        "publishOnImport": NotRequired[bool],
        "recommendation": NotRequired[RecommendationConfigurationTypeDef],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
    },
)
UpdateDataSourceInputRequestTypeDef = TypedDict(
    "UpdateDataSourceInputRequestTypeDef",
    {
        "domainIdentifier": str,
        "identifier": str,
        "assetFormsInput": NotRequired[Sequence[FormInputTypeDef]],
        "configuration": NotRequired[DataSourceConfigurationInputTypeDef],
        "description": NotRequired[str],
        "enableSetting": NotRequired[EnableSettingType],
        "name": NotRequired[str],
        "publishOnImport": NotRequired[bool],
        "recommendation": NotRequired[RecommendationConfigurationTypeDef],
        "schedule": NotRequired[ScheduleConfigurationTypeDef],
    },
)
CreateDataSourceOutputTypeDef = TypedDict(
    "CreateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "schedule": ScheduleConfigurationTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAssetCount": int,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "assetFormsOutput": List[FormOutputTypeDef],
        "configuration": DataSourceConfigurationOutputTypeDef,
        "createdAt": datetime,
        "description": str,
        "domainId": str,
        "enableSetting": EnableSettingType,
        "environmentId": str,
        "errorMessage": DataSourceErrorMessageTypeDef,
        "id": str,
        "lastRunAt": datetime,
        "lastRunErrorMessage": DataSourceErrorMessageTypeDef,
        "lastRunStatus": DataSourceRunStatusType,
        "name": str,
        "projectId": str,
        "publishOnImport": bool,
        "recommendation": RecommendationConfigurationTypeDef,
        "schedule": ScheduleConfigurationTypeDef,
        "status": DataSourceStatusType,
        "type": str,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionRequestsOutputTypeDef = TypedDict(
    "ListSubscriptionRequestsOutputTypeDef",
    {
        "items": List[SubscriptionRequestSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSubscriptionsOutputTypeDef = TypedDict(
    "ListSubscriptionsOutputTypeDef",
    {
        "items": List[SubscriptionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
