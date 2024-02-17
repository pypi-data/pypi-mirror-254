"""
Type annotations for datazone service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datazone.client import DataZoneClient

    session = Session()
    client: DataZoneClient = session.client("datazone")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ChangeActionType,
    DataAssetActivityStatusType,
    DataSourceRunStatusType,
    DataSourceStatusType,
    DomainStatusType,
    EnableSettingType,
    EnvironmentStatusType,
    FormTypeStatusType,
    GlossaryStatusType,
    GlossaryTermStatusType,
    GroupProfileStatusType,
    GroupSearchTypeType,
    InventorySearchScopeType,
    NotificationTypeType,
    SortKeyType,
    SortOrderType,
    SubscriptionGrantStatusType,
    SubscriptionRequestStatusType,
    SubscriptionStatusType,
    TaskStatusType,
    TypesSearchScopeType,
    UserDesignationType,
    UserProfileStatusType,
    UserProfileTypeType,
    UserSearchTypeType,
    UserTypeType,
)
from .paginator import (
    ListAssetRevisionsPaginator,
    ListDataSourceRunActivitiesPaginator,
    ListDataSourceRunsPaginator,
    ListDataSourcesPaginator,
    ListDomainsPaginator,
    ListEnvironmentBlueprintConfigurationsPaginator,
    ListEnvironmentBlueprintsPaginator,
    ListEnvironmentProfilesPaginator,
    ListEnvironmentsPaginator,
    ListNotificationsPaginator,
    ListProjectMembershipsPaginator,
    ListProjectsPaginator,
    ListSubscriptionGrantsPaginator,
    ListSubscriptionRequestsPaginator,
    ListSubscriptionsPaginator,
    ListSubscriptionTargetsPaginator,
    SearchGroupProfilesPaginator,
    SearchListingsPaginator,
    SearchPaginator,
    SearchTypesPaginator,
    SearchUserProfilesPaginator,
)
from .type_defs import (
    AcceptChoiceTypeDef,
    AcceptPredictionsOutputTypeDef,
    AcceptRuleTypeDef,
    AcceptSubscriptionRequestOutputTypeDef,
    AssetTargetNameMapTypeDef,
    CancelSubscriptionOutputTypeDef,
    CreateAssetOutputTypeDef,
    CreateAssetRevisionOutputTypeDef,
    CreateAssetTypeOutputTypeDef,
    CreateDataSourceOutputTypeDef,
    CreateDomainOutputTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateEnvironmentProfileOutputTypeDef,
    CreateFormTypeOutputTypeDef,
    CreateGlossaryOutputTypeDef,
    CreateGlossaryTermOutputTypeDef,
    CreateGroupProfileOutputTypeDef,
    CreateListingChangeSetOutputTypeDef,
    CreateProjectOutputTypeDef,
    CreateSubscriptionGrantOutputTypeDef,
    CreateSubscriptionRequestOutputTypeDef,
    CreateSubscriptionTargetOutputTypeDef,
    CreateUserProfileOutputTypeDef,
    DataSourceConfigurationInputTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteDomainOutputTypeDef,
    DeleteSubscriptionGrantOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    EnvironmentParameterTypeDef,
    FailureCauseTypeDef,
    FilterClauseTypeDef,
    FormEntryInputTypeDef,
    FormInputTypeDef,
    GetAssetOutputTypeDef,
    GetAssetTypeOutputTypeDef,
    GetDataSourceOutputTypeDef,
    GetDataSourceRunOutputTypeDef,
    GetDomainOutputTypeDef,
    GetEnvironmentBlueprintConfigurationOutputTypeDef,
    GetEnvironmentBlueprintOutputTypeDef,
    GetEnvironmentOutputTypeDef,
    GetEnvironmentProfileOutputTypeDef,
    GetFormTypeOutputTypeDef,
    GetGlossaryOutputTypeDef,
    GetGlossaryTermOutputTypeDef,
    GetGroupProfileOutputTypeDef,
    GetIamPortalLoginUrlOutputTypeDef,
    GetListingOutputTypeDef,
    GetProjectOutputTypeDef,
    GetSubscriptionGrantOutputTypeDef,
    GetSubscriptionOutputTypeDef,
    GetSubscriptionRequestDetailsOutputTypeDef,
    GetSubscriptionTargetOutputTypeDef,
    GetUserProfileOutputTypeDef,
    GrantedEntityInputTypeDef,
    ListAssetRevisionsOutputTypeDef,
    ListDataSourceRunActivitiesOutputTypeDef,
    ListDataSourceRunsOutputTypeDef,
    ListDataSourcesOutputTypeDef,
    ListDomainsOutputTypeDef,
    ListEnvironmentBlueprintConfigurationsOutputTypeDef,
    ListEnvironmentBlueprintsOutputTypeDef,
    ListEnvironmentProfilesOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListNotificationsOutputTypeDef,
    ListProjectMembershipsOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListSubscriptionGrantsOutputTypeDef,
    ListSubscriptionRequestsOutputTypeDef,
    ListSubscriptionsOutputTypeDef,
    ListSubscriptionTargetsOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    MemberTypeDef,
    ModelTypeDef,
    PredictionConfigurationTypeDef,
    PutEnvironmentBlueprintConfigurationOutputTypeDef,
    RecommendationConfigurationTypeDef,
    RejectChoiceTypeDef,
    RejectPredictionsOutputTypeDef,
    RejectRuleTypeDef,
    RejectSubscriptionRequestOutputTypeDef,
    RevokeSubscriptionOutputTypeDef,
    ScheduleConfigurationTypeDef,
    SearchGroupProfilesOutputTypeDef,
    SearchInItemTypeDef,
    SearchListingsOutputTypeDef,
    SearchOutputTypeDef,
    SearchSortTypeDef,
    SearchTypesOutputTypeDef,
    SearchUserProfilesOutputTypeDef,
    SingleSignOnTypeDef,
    StartDataSourceRunOutputTypeDef,
    SubscribedListingInputTypeDef,
    SubscribedPrincipalInputTypeDef,
    SubscriptionTargetFormTypeDef,
    TermRelationsTypeDef,
    TimestampTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateDomainOutputTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateEnvironmentProfileOutputTypeDef,
    UpdateGlossaryOutputTypeDef,
    UpdateGlossaryTermOutputTypeDef,
    UpdateGroupProfileOutputTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateSubscriptionGrantStatusOutputTypeDef,
    UpdateSubscriptionRequestOutputTypeDef,
    UpdateSubscriptionTargetOutputTypeDef,
    UpdateUserProfileOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DataZoneClient",)


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
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class DataZoneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataZoneClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#exceptions)
        """

    def accept_predictions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        acceptChoices: Sequence[AcceptChoiceTypeDef] = ...,
        acceptRule: AcceptRuleTypeDef = ...,
        clientToken: str = ...,
        revision: str = ...,
    ) -> AcceptPredictionsOutputTypeDef:
        """
        Accepts automatically generated business-friendly metadata for your Amazon
        DataZone
        assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.accept_predictions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#accept_predictions)
        """

    def accept_subscription_request(
        self, *, domainIdentifier: str, identifier: str, decisionComment: str = ...
    ) -> AcceptSubscriptionRequestOutputTypeDef:
        """
        Accepts a subscription request to a specific asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.accept_subscription_request)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#accept_subscription_request)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#can_paginate)
        """

    def cancel_subscription(
        self, *, domainIdentifier: str, identifier: str
    ) -> CancelSubscriptionOutputTypeDef:
        """
        Cancels the subscription to the specified asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.cancel_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#cancel_subscription)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#close)
        """

    def create_asset(
        self,
        *,
        domainIdentifier: str,
        name: str,
        owningProjectIdentifier: str,
        typeIdentifier: str,
        clientToken: str = ...,
        description: str = ...,
        externalIdentifier: str = ...,
        formsInput: Sequence[FormInputTypeDef] = ...,
        glossaryTerms: Sequence[str] = ...,
        predictionConfiguration: PredictionConfigurationTypeDef = ...,
        typeRevision: str = ...,
    ) -> CreateAssetOutputTypeDef:
        """
        Creates an asset in Amazon DataZone catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset)
        """

    def create_asset_revision(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        formsInput: Sequence[FormInputTypeDef] = ...,
        glossaryTerms: Sequence[str] = ...,
        predictionConfiguration: PredictionConfigurationTypeDef = ...,
        typeRevision: str = ...,
    ) -> CreateAssetRevisionOutputTypeDef:
        """
        Creates a revision of the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset_revision)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_revision)
        """

    def create_asset_type(
        self,
        *,
        domainIdentifier: str,
        formsInput: Mapping[str, FormEntryInputTypeDef],
        name: str,
        owningProjectIdentifier: str,
        description: str = ...,
    ) -> CreateAssetTypeOutputTypeDef:
        """
        Creates a custom asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_asset_type)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_asset_type)
        """

    def create_data_source(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        name: str,
        projectIdentifier: str,
        type: str,
        assetFormsInput: Sequence[FormInputTypeDef] = ...,
        clientToken: str = ...,
        configuration: DataSourceConfigurationInputTypeDef = ...,
        description: str = ...,
        enableSetting: EnableSettingType = ...,
        publishOnImport: bool = ...,
        recommendation: RecommendationConfigurationTypeDef = ...,
        schedule: ScheduleConfigurationTypeDef = ...,
    ) -> CreateDataSourceOutputTypeDef:
        """
        Creates an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_data_source)
        """

    def create_domain(
        self,
        *,
        domainExecutionRole: str,
        name: str,
        clientToken: str = ...,
        description: str = ...,
        kmsKeyIdentifier: str = ...,
        singleSignOn: SingleSignOnTypeDef = ...,
        tags: Mapping[str, str] = ...,
    ) -> CreateDomainOutputTypeDef:
        """
        Creates an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_domain)
        """

    def create_environment(
        self,
        *,
        domainIdentifier: str,
        environmentProfileIdentifier: str,
        name: str,
        projectIdentifier: str,
        description: str = ...,
        glossaryTerms: Sequence[str] = ...,
        userParameters: Sequence[EnvironmentParameterTypeDef] = ...,
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Create an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_environment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment)
        """

    def create_environment_profile(
        self,
        *,
        domainIdentifier: str,
        environmentBlueprintIdentifier: str,
        name: str,
        projectIdentifier: str,
        awsAccountId: str = ...,
        awsAccountRegion: str = ...,
        description: str = ...,
        userParameters: Sequence[EnvironmentParameterTypeDef] = ...,
    ) -> CreateEnvironmentProfileOutputTypeDef:
        """
        Creates an Amazon DataZone environment profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_environment_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_environment_profile)
        """

    def create_form_type(
        self,
        *,
        domainIdentifier: str,
        model: ModelTypeDef,
        name: str,
        owningProjectIdentifier: str,
        description: str = ...,
        status: FormTypeStatusType = ...,
    ) -> CreateFormTypeOutputTypeDef:
        """
        Creates a metadata form type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_form_type)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_form_type)
        """

    def create_glossary(
        self,
        *,
        domainIdentifier: str,
        name: str,
        owningProjectIdentifier: str,
        clientToken: str = ...,
        description: str = ...,
        status: GlossaryStatusType = ...,
    ) -> CreateGlossaryOutputTypeDef:
        """
        Creates an Amazon DataZone business glossary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_glossary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_glossary)
        """

    def create_glossary_term(
        self,
        *,
        domainIdentifier: str,
        glossaryIdentifier: str,
        name: str,
        clientToken: str = ...,
        longDescription: str = ...,
        shortDescription: str = ...,
        status: GlossaryTermStatusType = ...,
        termRelations: TermRelationsTypeDef = ...,
    ) -> CreateGlossaryTermOutputTypeDef:
        """
        Creates a business glossary term.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_glossary_term)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_glossary_term)
        """

    def create_group_profile(
        self, *, domainIdentifier: str, groupIdentifier: str, clientToken: str = ...
    ) -> CreateGroupProfileOutputTypeDef:
        """
        Creates a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_group_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_group_profile)
        """

    def create_listing_change_set(
        self,
        *,
        action: ChangeActionType,
        domainIdentifier: str,
        entityIdentifier: str,
        entityType: Literal["ASSET"],
        clientToken: str = ...,
        entityRevision: str = ...,
    ) -> CreateListingChangeSetOutputTypeDef:
        """
        See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/CreateListingChangeSet).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_listing_change_set)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_listing_change_set)
        """

    def create_project(
        self,
        *,
        domainIdentifier: str,
        name: str,
        description: str = ...,
        glossaryTerms: Sequence[str] = ...,
    ) -> CreateProjectOutputTypeDef:
        """
        Creates an Amazon DataZone project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project)
        """

    def create_project_membership(
        self,
        *,
        designation: UserDesignationType,
        domainIdentifier: str,
        member: MemberTypeDef,
        projectIdentifier: str,
    ) -> Dict[str, Any]:
        """
        Creates a project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_project_membership)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_project_membership)
        """

    def create_subscription_grant(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        grantedEntity: GrantedEntityInputTypeDef,
        subscriptionTargetIdentifier: str,
        assetTargetNames: Sequence[AssetTargetNameMapTypeDef] = ...,
        clientToken: str = ...,
    ) -> CreateSubscriptionGrantOutputTypeDef:
        """
        Creates a subsscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_subscription_grant)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_grant)
        """

    def create_subscription_request(
        self,
        *,
        domainIdentifier: str,
        requestReason: str,
        subscribedListings: Sequence[SubscribedListingInputTypeDef],
        subscribedPrincipals: Sequence[SubscribedPrincipalInputTypeDef],
        clientToken: str = ...,
    ) -> CreateSubscriptionRequestOutputTypeDef:
        """
        Creates a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_subscription_request)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_request)
        """

    def create_subscription_target(
        self,
        *,
        applicableAssetTypes: Sequence[str],
        authorizedPrincipals: Sequence[str],
        domainIdentifier: str,
        environmentIdentifier: str,
        manageAccessRole: str,
        name: str,
        subscriptionTargetConfig: Sequence[SubscriptionTargetFormTypeDef],
        type: str,
        clientToken: str = ...,
        provider: str = ...,
    ) -> CreateSubscriptionTargetOutputTypeDef:
        """
        Creates a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_subscription_target)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_subscription_target)
        """

    def create_user_profile(
        self,
        *,
        domainIdentifier: str,
        userIdentifier: str,
        clientToken: str = ...,
        userType: UserTypeType = ...,
    ) -> CreateUserProfileOutputTypeDef:
        """
        Creates a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.create_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#create_user_profile)
        """

    def delete_asset(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Delets an asset in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_asset)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset)
        """

    def delete_asset_type(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes an asset type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_asset_type)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_asset_type)
        """

    def delete_data_source(
        self, *, domainIdentifier: str, identifier: str, clientToken: str = ...
    ) -> DeleteDataSourceOutputTypeDef:
        """
        Deletes a data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_data_source)
        """

    def delete_domain(
        self, *, identifier: str, clientToken: str = ..., skipDeletionCheck: bool = ...
    ) -> DeleteDomainOutputTypeDef:
        """
        Deletes a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_domain)
        """

    def delete_environment(
        self, *, domainIdentifier: str, identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment)
        """

    def delete_environment_blueprint_configuration(
        self, *, domainIdentifier: str, environmentBlueprintIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment_blueprint_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_blueprint_configuration)
        """

    def delete_environment_profile(
        self, *, domainIdentifier: str, identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_environment_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_environment_profile)
        """

    def delete_form_type(self, *, domainIdentifier: str, formTypeIdentifier: str) -> Dict[str, Any]:
        """
        Delets and metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_form_type)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_form_type)
        """

    def delete_glossary(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_glossary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_glossary)
        """

    def delete_glossary_term(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        Deletes a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_glossary_term)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_glossary_term)
        """

    def delete_listing(self, *, domainIdentifier: str, identifier: str) -> Dict[str, Any]:
        """
        See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/DeleteListing).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_listing)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_listing)
        """

    def delete_project(
        self, *, domainIdentifier: str, identifier: str, skipDeletionCheck: bool = ...
    ) -> Dict[str, Any]:
        """
        Deletes a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project)
        """

    def delete_project_membership(
        self, *, domainIdentifier: str, member: MemberTypeDef, projectIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes project membership in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_project_membership)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_project_membership)
        """

    def delete_subscription_grant(
        self, *, domainIdentifier: str, identifier: str
    ) -> DeleteSubscriptionGrantOutputTypeDef:
        """
        Deletes and subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_subscription_grant)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_grant)
        """

    def delete_subscription_request(
        self, *, domainIdentifier: str, identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_subscription_request)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_request)
        """

    def delete_subscription_target(
        self, *, domainIdentifier: str, environmentIdentifier: str, identifier: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.delete_subscription_target)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#delete_subscription_target)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#generate_presigned_url)
        """

    def get_asset(
        self, *, domainIdentifier: str, identifier: str, revision: str = ...
    ) -> GetAssetOutputTypeDef:
        """
        Gets an Amazon DataZone asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_asset)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset)
        """

    def get_asset_type(
        self, *, domainIdentifier: str, identifier: str, revision: str = ...
    ) -> GetAssetTypeOutputTypeDef:
        """
        Gets an Amazon DataZone asset type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_asset_type)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_asset_type)
        """

    def get_data_source(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetDataSourceOutputTypeDef:
        """
        Gets an Amazon DataZone data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_source)
        """

    def get_data_source_run(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetDataSourceRunOutputTypeDef:
        """
        Gets an Amazon DataZone data source run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_data_source_run)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_data_source_run)
        """

    def get_domain(self, *, identifier: str) -> GetDomainOutputTypeDef:
        """
        Gets an Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_domain)
        """

    def get_environment(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetEnvironmentOutputTypeDef:
        """
        Gets an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment)
        """

    def get_environment_blueprint(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetEnvironmentBlueprintOutputTypeDef:
        """
        Gets an Amazon DataZone blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_blueprint)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_blueprint)
        """

    def get_environment_blueprint_configuration(
        self, *, domainIdentifier: str, environmentBlueprintIdentifier: str
    ) -> GetEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Gets the blueprint configuration in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_blueprint_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_blueprint_configuration)
        """

    def get_environment_profile(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetEnvironmentProfileOutputTypeDef:
        """
        Gets an evinronment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_environment_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_environment_profile)
        """

    def get_form_type(
        self, *, domainIdentifier: str, formTypeIdentifier: str, revision: str = ...
    ) -> GetFormTypeOutputTypeDef:
        """
        Gets a metadata form type in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_form_type)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_form_type)
        """

    def get_glossary(self, *, domainIdentifier: str, identifier: str) -> GetGlossaryOutputTypeDef:
        """
        Gets a business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_glossary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_glossary)
        """

    def get_glossary_term(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetGlossaryTermOutputTypeDef:
        """
        Gets a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_glossary_term)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_glossary_term)
        """

    def get_group_profile(
        self, *, domainIdentifier: str, groupIdentifier: str
    ) -> GetGroupProfileOutputTypeDef:
        """
        Gets a group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_group_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_group_profile)
        """

    def get_iam_portal_login_url(
        self, *, domainIdentifier: str
    ) -> GetIamPortalLoginUrlOutputTypeDef:
        """
        Gets the data portal URL for the specified Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_iam_portal_login_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_iam_portal_login_url)
        """

    def get_listing(
        self, *, domainIdentifier: str, identifier: str, listingRevision: str = ...
    ) -> GetListingOutputTypeDef:
        """
        See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/GetListing).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_listing)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_listing)
        """

    def get_project(self, *, domainIdentifier: str, identifier: str) -> GetProjectOutputTypeDef:
        """
        Gets a project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_project)
        """

    def get_subscription(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetSubscriptionOutputTypeDef:
        """
        Gets a subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription)
        """

    def get_subscription_grant(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetSubscriptionGrantOutputTypeDef:
        """
        Gets the subscription grant in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription_grant)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_grant)
        """

    def get_subscription_request_details(
        self, *, domainIdentifier: str, identifier: str
    ) -> GetSubscriptionRequestDetailsOutputTypeDef:
        """
        Gets the details of the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription_request_details)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_request_details)
        """

    def get_subscription_target(
        self, *, domainIdentifier: str, environmentIdentifier: str, identifier: str
    ) -> GetSubscriptionTargetOutputTypeDef:
        """
        Gets the subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_subscription_target)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_subscription_target)
        """

    def get_user_profile(
        self, *, domainIdentifier: str, userIdentifier: str, type: UserProfileTypeType = ...
    ) -> GetUserProfileOutputTypeDef:
        """
        Gets a user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_user_profile)
        """

    def list_asset_revisions(
        self, *, domainIdentifier: str, identifier: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListAssetRevisionsOutputTypeDef:
        """
        Lists the revisions for the asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_asset_revisions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_asset_revisions)
        """

    def list_data_source_run_activities(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
        status: DataAssetActivityStatusType = ...,
    ) -> ListDataSourceRunActivitiesOutputTypeDef:
        """
        Lists data source run activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_source_run_activities)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_source_run_activities)
        """

    def list_data_source_runs(
        self,
        *,
        dataSourceIdentifier: str,
        domainIdentifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
        status: DataSourceRunStatusType = ...,
    ) -> ListDataSourceRunsOutputTypeDef:
        """
        Lists data source runs in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_source_runs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_source_runs)
        """

    def list_data_sources(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        environmentIdentifier: str = ...,
        maxResults: int = ...,
        name: str = ...,
        nextToken: str = ...,
        status: DataSourceStatusType = ...,
        type: str = ...,
    ) -> ListDataSourcesOutputTypeDef:
        """
        Lists data sources in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_data_sources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_data_sources)
        """

    def list_domains(
        self, *, maxResults: int = ..., nextToken: str = ..., status: DomainStatusType = ...
    ) -> ListDomainsOutputTypeDef:
        """
        Lists Amazon DataZone domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_domains)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_domains)
        """

    def list_environment_blueprint_configurations(
        self, *, domainIdentifier: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListEnvironmentBlueprintConfigurationsOutputTypeDef:
        """
        Lists blueprint configurations for a Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_blueprint_configurations)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_blueprint_configurations)
        """

    def list_environment_blueprints(
        self,
        *,
        domainIdentifier: str,
        managed: bool = ...,
        maxResults: int = ...,
        name: str = ...,
        nextToken: str = ...,
    ) -> ListEnvironmentBlueprintsOutputTypeDef:
        """
        Lists blueprints in an Amazon DataZone environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_blueprints)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_blueprints)
        """

    def list_environment_profiles(
        self,
        *,
        domainIdentifier: str,
        awsAccountId: str = ...,
        awsAccountRegion: str = ...,
        environmentBlueprintIdentifier: str = ...,
        maxResults: int = ...,
        name: str = ...,
        nextToken: str = ...,
        projectIdentifier: str = ...,
    ) -> ListEnvironmentProfilesOutputTypeDef:
        """
        Lists Amazon DataZone environment profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environment_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environment_profiles)
        """

    def list_environments(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        awsAccountId: str = ...,
        awsAccountRegion: str = ...,
        environmentBlueprintIdentifier: str = ...,
        environmentProfileIdentifier: str = ...,
        maxResults: int = ...,
        name: str = ...,
        nextToken: str = ...,
        provider: str = ...,
        status: EnvironmentStatusType = ...,
    ) -> ListEnvironmentsOutputTypeDef:
        """
        Lists Amazon DataZone environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_environments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_environments)
        """

    def list_notifications(
        self,
        *,
        domainIdentifier: str,
        type: NotificationTypeType,
        afterTimestamp: TimestampTypeDef = ...,
        beforeTimestamp: TimestampTypeDef = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        subjects: Sequence[str] = ...,
        taskStatus: TaskStatusType = ...,
    ) -> ListNotificationsOutputTypeDef:
        """
        Lists all Amazon DataZone notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_notifications)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_notifications)
        """

    def list_project_memberships(
        self,
        *,
        domainIdentifier: str,
        projectIdentifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: Literal["NAME"] = ...,
        sortOrder: SortOrderType = ...,
    ) -> ListProjectMembershipsOutputTypeDef:
        """
        Lists all members of the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_project_memberships)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_project_memberships)
        """

    def list_projects(
        self,
        *,
        domainIdentifier: str,
        groupIdentifier: str = ...,
        maxResults: int = ...,
        name: str = ...,
        nextToken: str = ...,
        userIdentifier: str = ...,
    ) -> ListProjectsOutputTypeDef:
        """
        Lists Amazon DataZone projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_projects)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_projects)
        """

    def list_subscription_grants(
        self,
        *,
        domainIdentifier: str,
        environmentId: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        subscribedListingId: str = ...,
        subscriptionId: str = ...,
        subscriptionTargetId: str = ...,
    ) -> ListSubscriptionGrantsOutputTypeDef:
        """
        Lists subscription grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscription_grants)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_grants)
        """

    def list_subscription_requests(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        owningProjectId: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        status: SubscriptionRequestStatusType = ...,
        subscribedListingId: str = ...,
    ) -> ListSubscriptionRequestsOutputTypeDef:
        """
        Lists Amazon DataZone subscription requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscription_requests)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_requests)
        """

    def list_subscription_targets(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        maxResults: int = ...,
        nextToken: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
    ) -> ListSubscriptionTargetsOutputTypeDef:
        """
        Lists subscription targets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscription_targets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscription_targets)
        """

    def list_subscriptions(
        self,
        *,
        domainIdentifier: str,
        approverProjectId: str = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        owningProjectId: str = ...,
        sortBy: SortKeyType = ...,
        sortOrder: SortOrderType = ...,
        status: SubscriptionStatusType = ...,
        subscribedListingId: str = ...,
        subscriptionRequestIdentifier: str = ...,
    ) -> ListSubscriptionsOutputTypeDef:
        """
        Lists subscriptions in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_subscriptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_subscriptions)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for the specified resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#list_tags_for_resource)
        """

    def put_environment_blueprint_configuration(
        self,
        *,
        domainIdentifier: str,
        enabledRegions: Sequence[str],
        environmentBlueprintIdentifier: str,
        manageAccessRoleArn: str = ...,
        provisioningRoleArn: str = ...,
        regionalParameters: Mapping[str, Mapping[str, str]] = ...,
    ) -> PutEnvironmentBlueprintConfigurationOutputTypeDef:
        """
        Writes the configuration for the specified environment blueprint in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.put_environment_blueprint_configuration)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#put_environment_blueprint_configuration)
        """

    def reject_predictions(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        clientToken: str = ...,
        rejectChoices: Sequence[RejectChoiceTypeDef] = ...,
        rejectRule: RejectRuleTypeDef = ...,
        revision: str = ...,
    ) -> RejectPredictionsOutputTypeDef:
        """
        Rejects automatically generated business-friendly metadata for your Amazon
        DataZone
        assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.reject_predictions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#reject_predictions)
        """

    def reject_subscription_request(
        self, *, domainIdentifier: str, identifier: str, decisionComment: str = ...
    ) -> RejectSubscriptionRequestOutputTypeDef:
        """
        Rejects the specified subscription request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.reject_subscription_request)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#reject_subscription_request)
        """

    def revoke_subscription(
        self, *, domainIdentifier: str, identifier: str, retainPermissions: bool = ...
    ) -> RevokeSubscriptionOutputTypeDef:
        """
        Revokes a specified subscription in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.revoke_subscription)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#revoke_subscription)
        """

    def search(
        self,
        *,
        domainIdentifier: str,
        searchScope: InventorySearchScopeType,
        additionalAttributes: Sequence[Literal["FORMS"]] = ...,
        filters: "FilterClauseTypeDef" = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        owningProjectIdentifier: str = ...,
        searchIn: Sequence[SearchInItemTypeDef] = ...,
        searchText: str = ...,
        sort: SearchSortTypeDef = ...,
    ) -> SearchOutputTypeDef:
        """
        Searches for assets in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search)
        """

    def search_group_profiles(
        self,
        *,
        domainIdentifier: str,
        groupType: GroupSearchTypeType,
        maxResults: int = ...,
        nextToken: str = ...,
        searchText: str = ...,
    ) -> SearchGroupProfilesOutputTypeDef:
        """
        Searches group profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_group_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_group_profiles)
        """

    def search_listings(
        self,
        *,
        domainIdentifier: str,
        additionalAttributes: Sequence[Literal["FORMS"]] = ...,
        filters: "FilterClauseTypeDef" = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        searchIn: Sequence[SearchInItemTypeDef] = ...,
        searchText: str = ...,
        sort: SearchSortTypeDef = ...,
    ) -> SearchListingsOutputTypeDef:
        """
        Searches listings in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_listings)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_listings)
        """

    def search_types(
        self,
        *,
        domainIdentifier: str,
        managed: bool,
        searchScope: TypesSearchScopeType,
        filters: "FilterClauseTypeDef" = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        searchIn: Sequence[SearchInItemTypeDef] = ...,
        searchText: str = ...,
        sort: SearchSortTypeDef = ...,
    ) -> SearchTypesOutputTypeDef:
        """
        Searches for types in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_types)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_types)
        """

    def search_user_profiles(
        self,
        *,
        domainIdentifier: str,
        userType: UserSearchTypeType,
        maxResults: int = ...,
        nextToken: str = ...,
        searchText: str = ...,
    ) -> SearchUserProfilesOutputTypeDef:
        """
        Searches user profiles in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.search_user_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#search_user_profiles)
        """

    def start_data_source_run(
        self, *, dataSourceIdentifier: str, domainIdentifier: str, clientToken: str = ...
    ) -> StartDataSourceRunOutputTypeDef:
        """
        Start the run of the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.start_data_source_run)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#start_data_source_run)
        """

    def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Tags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Untags a resource in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#untag_resource)
        """

    def update_data_source(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        assetFormsInput: Sequence[FormInputTypeDef] = ...,
        configuration: DataSourceConfigurationInputTypeDef = ...,
        description: str = ...,
        enableSetting: EnableSettingType = ...,
        name: str = ...,
        publishOnImport: bool = ...,
        recommendation: RecommendationConfigurationTypeDef = ...,
        schedule: ScheduleConfigurationTypeDef = ...,
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the specified data source in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_data_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_data_source)
        """

    def update_domain(
        self,
        *,
        identifier: str,
        clientToken: str = ...,
        description: str = ...,
        domainExecutionRole: str = ...,
        name: str = ...,
        singleSignOn: SingleSignOnTypeDef = ...,
    ) -> UpdateDomainOutputTypeDef:
        """
        Updates a Amazon DataZone domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_domain)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_domain)
        """

    def update_environment(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str = ...,
        glossaryTerms: Sequence[str] = ...,
        name: str = ...,
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Updates the specified environment in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_environment)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment)
        """

    def update_environment_profile(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        awsAccountId: str = ...,
        awsAccountRegion: str = ...,
        description: str = ...,
        name: str = ...,
        userParameters: Sequence[EnvironmentParameterTypeDef] = ...,
    ) -> UpdateEnvironmentProfileOutputTypeDef:
        """
        Updates the specified environment profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_environment_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_environment_profile)
        """

    def update_glossary(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        clientToken: str = ...,
        description: str = ...,
        name: str = ...,
        status: GlossaryStatusType = ...,
    ) -> UpdateGlossaryOutputTypeDef:
        """
        Updates the business glossary in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_glossary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_glossary)
        """

    def update_glossary_term(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        glossaryIdentifier: str = ...,
        longDescription: str = ...,
        name: str = ...,
        shortDescription: str = ...,
        status: GlossaryTermStatusType = ...,
        termRelations: TermRelationsTypeDef = ...,
    ) -> UpdateGlossaryTermOutputTypeDef:
        """
        Updates a business glossary term in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_glossary_term)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_glossary_term)
        """

    def update_group_profile(
        self, *, domainIdentifier: str, groupIdentifier: str, status: GroupProfileStatusType
    ) -> UpdateGroupProfileOutputTypeDef:
        """
        Updates the specified group profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_group_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_group_profile)
        """

    def update_project(
        self,
        *,
        domainIdentifier: str,
        identifier: str,
        description: str = ...,
        glossaryTerms: Sequence[str] = ...,
        name: str = ...,
    ) -> UpdateProjectOutputTypeDef:
        """
        Updates the specified project in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_project)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_project)
        """

    def update_subscription_grant_status(
        self,
        *,
        assetIdentifier: str,
        domainIdentifier: str,
        identifier: str,
        status: SubscriptionGrantStatusType,
        failureCause: FailureCauseTypeDef = ...,
        targetName: str = ...,
    ) -> UpdateSubscriptionGrantStatusOutputTypeDef:
        """
        Updates the status of the specified subscription grant status in Amazon
        DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_subscription_grant_status)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_grant_status)
        """

    def update_subscription_request(
        self, *, domainIdentifier: str, identifier: str, requestReason: str
    ) -> UpdateSubscriptionRequestOutputTypeDef:
        """
        Updates a specified subscription request in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_subscription_request)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_request)
        """

    def update_subscription_target(
        self,
        *,
        domainIdentifier: str,
        environmentIdentifier: str,
        identifier: str,
        applicableAssetTypes: Sequence[str] = ...,
        authorizedPrincipals: Sequence[str] = ...,
        manageAccessRole: str = ...,
        name: str = ...,
        provider: str = ...,
        subscriptionTargetConfig: Sequence[SubscriptionTargetFormTypeDef] = ...,
    ) -> UpdateSubscriptionTargetOutputTypeDef:
        """
        Updates the specified subscription target in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_subscription_target)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_subscription_target)
        """

    def update_user_profile(
        self,
        *,
        domainIdentifier: str,
        status: UserProfileStatusType,
        userIdentifier: str,
        type: UserProfileTypeType = ...,
    ) -> UpdateUserProfileOutputTypeDef:
        """
        Updates the specified user profile in Amazon DataZone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.update_user_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#update_user_profile)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_revisions"]
    ) -> ListAssetRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_run_activities"]
    ) -> ListDataSourceRunActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_source_runs"]
    ) -> ListDataSourceRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_blueprint_configurations"]
    ) -> ListEnvironmentBlueprintConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_blueprints"]
    ) -> ListEnvironmentBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environment_profiles"]
    ) -> ListEnvironmentProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notifications"]
    ) -> ListNotificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_memberships"]
    ) -> ListProjectMembershipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_grants"]
    ) -> ListSubscriptionGrantsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_requests"]
    ) -> ListSubscriptionRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscription_targets"]
    ) -> ListSubscriptionTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_group_profiles"]
    ) -> SearchGroupProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_listings"]) -> SearchListingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_types"]) -> SearchTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_user_profiles"]
    ) -> SearchUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datazone.html#DataZone.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datazone/client/#get_paginator)
        """
