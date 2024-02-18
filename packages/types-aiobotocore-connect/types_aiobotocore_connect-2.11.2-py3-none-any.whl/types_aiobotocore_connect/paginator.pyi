"""
Type annotations for connect service client paginators.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/)

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_connect.client import ConnectClient
    from types_aiobotocore_connect.paginator import (
        GetMetricDataPaginator,
        ListAgentStatusesPaginator,
        ListApprovedOriginsPaginator,
        ListBotsPaginator,
        ListContactEvaluationsPaginator,
        ListContactFlowModulesPaginator,
        ListContactFlowsPaginator,
        ListContactReferencesPaginator,
        ListDefaultVocabulariesPaginator,
        ListEvaluationFormVersionsPaginator,
        ListEvaluationFormsPaginator,
        ListFlowAssociationsPaginator,
        ListHoursOfOperationsPaginator,
        ListInstanceAttributesPaginator,
        ListInstanceStorageConfigsPaginator,
        ListInstancesPaginator,
        ListIntegrationAssociationsPaginator,
        ListLambdaFunctionsPaginator,
        ListLexBotsPaginator,
        ListPhoneNumbersPaginator,
        ListPhoneNumbersV2Paginator,
        ListPredefinedAttributesPaginator,
        ListPromptsPaginator,
        ListQueueQuickConnectsPaginator,
        ListQueuesPaginator,
        ListQuickConnectsPaginator,
        ListRoutingProfileQueuesPaginator,
        ListRoutingProfilesPaginator,
        ListRulesPaginator,
        ListSecurityKeysPaginator,
        ListSecurityProfileApplicationsPaginator,
        ListSecurityProfilePermissionsPaginator,
        ListSecurityProfilesPaginator,
        ListTaskTemplatesPaginator,
        ListTrafficDistributionGroupUsersPaginator,
        ListTrafficDistributionGroupsPaginator,
        ListUseCasesPaginator,
        ListUserHierarchyGroupsPaginator,
        ListUserProficienciesPaginator,
        ListUsersPaginator,
        ListViewVersionsPaginator,
        ListViewsPaginator,
        SearchAvailablePhoneNumbersPaginator,
        SearchContactsPaginator,
        SearchHoursOfOperationsPaginator,
        SearchPredefinedAttributesPaginator,
        SearchPromptsPaginator,
        SearchQueuesPaginator,
        SearchQuickConnectsPaginator,
        SearchResourceTagsPaginator,
        SearchRoutingProfilesPaginator,
        SearchSecurityProfilesPaginator,
        SearchUsersPaginator,
        SearchVocabulariesPaginator,
    )

    session = get_session()
    with session.create_client("connect") as client:
        client: ConnectClient

        get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
        list_agent_statuses_paginator: ListAgentStatusesPaginator = client.get_paginator("list_agent_statuses")
        list_approved_origins_paginator: ListApprovedOriginsPaginator = client.get_paginator("list_approved_origins")
        list_bots_paginator: ListBotsPaginator = client.get_paginator("list_bots")
        list_contact_evaluations_paginator: ListContactEvaluationsPaginator = client.get_paginator("list_contact_evaluations")
        list_contact_flow_modules_paginator: ListContactFlowModulesPaginator = client.get_paginator("list_contact_flow_modules")
        list_contact_flows_paginator: ListContactFlowsPaginator = client.get_paginator("list_contact_flows")
        list_contact_references_paginator: ListContactReferencesPaginator = client.get_paginator("list_contact_references")
        list_default_vocabularies_paginator: ListDefaultVocabulariesPaginator = client.get_paginator("list_default_vocabularies")
        list_evaluation_form_versions_paginator: ListEvaluationFormVersionsPaginator = client.get_paginator("list_evaluation_form_versions")
        list_evaluation_forms_paginator: ListEvaluationFormsPaginator = client.get_paginator("list_evaluation_forms")
        list_flow_associations_paginator: ListFlowAssociationsPaginator = client.get_paginator("list_flow_associations")
        list_hours_of_operations_paginator: ListHoursOfOperationsPaginator = client.get_paginator("list_hours_of_operations")
        list_instance_attributes_paginator: ListInstanceAttributesPaginator = client.get_paginator("list_instance_attributes")
        list_instance_storage_configs_paginator: ListInstanceStorageConfigsPaginator = client.get_paginator("list_instance_storage_configs")
        list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
        list_integration_associations_paginator: ListIntegrationAssociationsPaginator = client.get_paginator("list_integration_associations")
        list_lambda_functions_paginator: ListLambdaFunctionsPaginator = client.get_paginator("list_lambda_functions")
        list_lex_bots_paginator: ListLexBotsPaginator = client.get_paginator("list_lex_bots")
        list_phone_numbers_paginator: ListPhoneNumbersPaginator = client.get_paginator("list_phone_numbers")
        list_phone_numbers_v2_paginator: ListPhoneNumbersV2Paginator = client.get_paginator("list_phone_numbers_v2")
        list_predefined_attributes_paginator: ListPredefinedAttributesPaginator = client.get_paginator("list_predefined_attributes")
        list_prompts_paginator: ListPromptsPaginator = client.get_paginator("list_prompts")
        list_queue_quick_connects_paginator: ListQueueQuickConnectsPaginator = client.get_paginator("list_queue_quick_connects")
        list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
        list_quick_connects_paginator: ListQuickConnectsPaginator = client.get_paginator("list_quick_connects")
        list_routing_profile_queues_paginator: ListRoutingProfileQueuesPaginator = client.get_paginator("list_routing_profile_queues")
        list_routing_profiles_paginator: ListRoutingProfilesPaginator = client.get_paginator("list_routing_profiles")
        list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
        list_security_keys_paginator: ListSecurityKeysPaginator = client.get_paginator("list_security_keys")
        list_security_profile_applications_paginator: ListSecurityProfileApplicationsPaginator = client.get_paginator("list_security_profile_applications")
        list_security_profile_permissions_paginator: ListSecurityProfilePermissionsPaginator = client.get_paginator("list_security_profile_permissions")
        list_security_profiles_paginator: ListSecurityProfilesPaginator = client.get_paginator("list_security_profiles")
        list_task_templates_paginator: ListTaskTemplatesPaginator = client.get_paginator("list_task_templates")
        list_traffic_distribution_group_users_paginator: ListTrafficDistributionGroupUsersPaginator = client.get_paginator("list_traffic_distribution_group_users")
        list_traffic_distribution_groups_paginator: ListTrafficDistributionGroupsPaginator = client.get_paginator("list_traffic_distribution_groups")
        list_use_cases_paginator: ListUseCasesPaginator = client.get_paginator("list_use_cases")
        list_user_hierarchy_groups_paginator: ListUserHierarchyGroupsPaginator = client.get_paginator("list_user_hierarchy_groups")
        list_user_proficiencies_paginator: ListUserProficienciesPaginator = client.get_paginator("list_user_proficiencies")
        list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
        list_view_versions_paginator: ListViewVersionsPaginator = client.get_paginator("list_view_versions")
        list_views_paginator: ListViewsPaginator = client.get_paginator("list_views")
        search_available_phone_numbers_paginator: SearchAvailablePhoneNumbersPaginator = client.get_paginator("search_available_phone_numbers")
        search_contacts_paginator: SearchContactsPaginator = client.get_paginator("search_contacts")
        search_hours_of_operations_paginator: SearchHoursOfOperationsPaginator = client.get_paginator("search_hours_of_operations")
        search_predefined_attributes_paginator: SearchPredefinedAttributesPaginator = client.get_paginator("search_predefined_attributes")
        search_prompts_paginator: SearchPromptsPaginator = client.get_paginator("search_prompts")
        search_queues_paginator: SearchQueuesPaginator = client.get_paginator("search_queues")
        search_quick_connects_paginator: SearchQuickConnectsPaginator = client.get_paginator("search_quick_connects")
        search_resource_tags_paginator: SearchResourceTagsPaginator = client.get_paginator("search_resource_tags")
        search_routing_profiles_paginator: SearchRoutingProfilesPaginator = client.get_paginator("search_routing_profiles")
        search_security_profiles_paginator: SearchSecurityProfilesPaginator = client.get_paginator("search_security_profiles")
        search_users_paginator: SearchUsersPaginator = client.get_paginator("search_users")
        search_vocabularies_paginator: SearchVocabulariesPaginator = client.get_paginator("search_vocabularies")
    ```
"""

import sys
from typing import AsyncIterator, Generic, Iterator, Sequence, TypeVar

from aiobotocore.paginate import AioPaginator
from botocore.paginate import PageIterator

from .literals import (
    AgentStatusTypeType,
    ContactFlowModuleStateType,
    ContactFlowTypeType,
    EventSourceNameType,
    GroupingType,
    InstanceStorageResourceTypeType,
    IntegrationTypeType,
    LexVersionType,
    PhoneNumberCountryCodeType,
    PhoneNumberTypeType,
    QueueTypeType,
    QuickConnectTypeType,
    ReferenceTypeType,
    RulePublishStatusType,
    TaskTemplateStatusType,
    ViewTypeType,
    VocabularyLanguageCodeType,
    VocabularyStateType,
)
from .type_defs import (
    FiltersTypeDef,
    GetMetricDataResponseTypeDef,
    HistoricalMetricTypeDef,
    HoursOfOperationSearchCriteriaTypeDef,
    HoursOfOperationSearchFilterTypeDef,
    ListAgentStatusResponseTypeDef,
    ListApprovedOriginsResponseTypeDef,
    ListBotsResponseTypeDef,
    ListContactEvaluationsResponseTypeDef,
    ListContactFlowModulesResponseTypeDef,
    ListContactFlowsResponseTypeDef,
    ListContactReferencesResponseTypeDef,
    ListDefaultVocabulariesResponseTypeDef,
    ListEvaluationFormsResponseTypeDef,
    ListEvaluationFormVersionsResponseTypeDef,
    ListFlowAssociationsResponseTypeDef,
    ListHoursOfOperationsResponseTypeDef,
    ListInstanceAttributesResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListInstanceStorageConfigsResponseTypeDef,
    ListIntegrationAssociationsResponseTypeDef,
    ListLambdaFunctionsResponseTypeDef,
    ListLexBotsResponseTypeDef,
    ListPhoneNumbersResponseTypeDef,
    ListPhoneNumbersV2ResponseTypeDef,
    ListPredefinedAttributesResponseTypeDef,
    ListPromptsResponseTypeDef,
    ListQueueQuickConnectsResponseTypeDef,
    ListQueuesResponseTypeDef,
    ListQuickConnectsResponseTypeDef,
    ListRoutingProfileQueuesResponseTypeDef,
    ListRoutingProfilesResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSecurityKeysResponseTypeDef,
    ListSecurityProfileApplicationsResponsePaginatorTypeDef,
    ListSecurityProfilePermissionsResponseTypeDef,
    ListSecurityProfilesResponseTypeDef,
    ListTaskTemplatesResponseTypeDef,
    ListTrafficDistributionGroupsResponseTypeDef,
    ListTrafficDistributionGroupUsersResponseTypeDef,
    ListUseCasesResponseTypeDef,
    ListUserHierarchyGroupsResponseTypeDef,
    ListUserProficienciesResponseTypeDef,
    ListUsersResponseTypeDef,
    ListViewsResponseTypeDef,
    ListViewVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
    PredefinedAttributeSearchCriteriaTypeDef,
    PromptSearchCriteriaTypeDef,
    PromptSearchFilterTypeDef,
    QueueSearchCriteriaTypeDef,
    QueueSearchFilterTypeDef,
    QuickConnectSearchCriteriaTypeDef,
    QuickConnectSearchFilterTypeDef,
    ResourceTagsSearchCriteriaTypeDef,
    RoutingProfileSearchCriteriaTypeDef,
    RoutingProfileSearchFilterTypeDef,
    SearchAvailablePhoneNumbersResponseTypeDef,
    SearchContactsResponseTypeDef,
    SearchContactsTimeRangeTypeDef,
    SearchCriteriaTypeDef,
    SearchHoursOfOperationsResponseTypeDef,
    SearchPredefinedAttributesResponsePaginatorTypeDef,
    SearchPromptsResponseTypeDef,
    SearchQueuesResponseTypeDef,
    SearchQuickConnectsResponseTypeDef,
    SearchResourceTagsResponseTypeDef,
    SearchRoutingProfilesResponseTypeDef,
    SearchSecurityProfilesResponseTypeDef,
    SearchUsersResponseTypeDef,
    SearchVocabulariesResponseTypeDef,
    SecurityProfileSearchCriteriaTypeDef,
    SecurityProfilesSearchFilterTypeDef,
    SortTypeDef,
    TimestampTypeDef,
    UserSearchCriteriaTypeDef,
    UserSearchFilterTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "GetMetricDataPaginator",
    "ListAgentStatusesPaginator",
    "ListApprovedOriginsPaginator",
    "ListBotsPaginator",
    "ListContactEvaluationsPaginator",
    "ListContactFlowModulesPaginator",
    "ListContactFlowsPaginator",
    "ListContactReferencesPaginator",
    "ListDefaultVocabulariesPaginator",
    "ListEvaluationFormVersionsPaginator",
    "ListEvaluationFormsPaginator",
    "ListFlowAssociationsPaginator",
    "ListHoursOfOperationsPaginator",
    "ListInstanceAttributesPaginator",
    "ListInstanceStorageConfigsPaginator",
    "ListInstancesPaginator",
    "ListIntegrationAssociationsPaginator",
    "ListLambdaFunctionsPaginator",
    "ListLexBotsPaginator",
    "ListPhoneNumbersPaginator",
    "ListPhoneNumbersV2Paginator",
    "ListPredefinedAttributesPaginator",
    "ListPromptsPaginator",
    "ListQueueQuickConnectsPaginator",
    "ListQueuesPaginator",
    "ListQuickConnectsPaginator",
    "ListRoutingProfileQueuesPaginator",
    "ListRoutingProfilesPaginator",
    "ListRulesPaginator",
    "ListSecurityKeysPaginator",
    "ListSecurityProfileApplicationsPaginator",
    "ListSecurityProfilePermissionsPaginator",
    "ListSecurityProfilesPaginator",
    "ListTaskTemplatesPaginator",
    "ListTrafficDistributionGroupUsersPaginator",
    "ListTrafficDistributionGroupsPaginator",
    "ListUseCasesPaginator",
    "ListUserHierarchyGroupsPaginator",
    "ListUserProficienciesPaginator",
    "ListUsersPaginator",
    "ListViewVersionsPaginator",
    "ListViewsPaginator",
    "SearchAvailablePhoneNumbersPaginator",
    "SearchContactsPaginator",
    "SearchHoursOfOperationsPaginator",
    "SearchPredefinedAttributesPaginator",
    "SearchPromptsPaginator",
    "SearchQueuesPaginator",
    "SearchQuickConnectsPaginator",
    "SearchResourceTagsPaginator",
    "SearchRoutingProfilesPaginator",
    "SearchSecurityProfilesPaginator",
    "SearchUsersPaginator",
    "SearchVocabulariesPaginator",
)

_ItemTypeDef = TypeVar("_ItemTypeDef")

class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """

class GetMetricDataPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.GetMetricData)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#getmetricdatapaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        Filters: FiltersTypeDef,
        HistoricalMetrics: Sequence[HistoricalMetricTypeDef],
        Groupings: Sequence[GroupingType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[GetMetricDataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.GetMetricData.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#getmetricdatapaginator)
        """

class ListAgentStatusesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListAgentStatuses)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listagentstatusespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        AgentStatusTypes: Sequence[AgentStatusTypeType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListAgentStatusResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListAgentStatuses.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listagentstatusespaginator)
        """

class ListApprovedOriginsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listapprovedoriginspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListApprovedOriginsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListApprovedOrigins.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listapprovedoriginspaginator)
        """

class ListBotsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListBots)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listbotspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        LexVersion: LexVersionType,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListBotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListBots.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listbotspaginator)
        """

class ListContactEvaluationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactEvaluations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactevaluationspaginator)
    """

    def paginate(
        self, *, InstanceId: str, ContactId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListContactEvaluationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactEvaluations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactevaluationspaginator)
        """

class ListContactFlowModulesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactFlowModules)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactflowmodulespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        ContactFlowModuleState: ContactFlowModuleStateType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListContactFlowModulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactFlowModules.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactflowmodulespaginator)
        """

class ListContactFlowsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactFlows)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactflowspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        ContactFlowTypes: Sequence[ContactFlowTypeType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListContactFlowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactFlows.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactflowspaginator)
        """

class ListContactReferencesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactReferences)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactreferencespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        ContactId: str,
        ReferenceTypes: Sequence[ReferenceTypeType],
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListContactReferencesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListContactReferences.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listcontactreferencespaginator)
        """

class ListDefaultVocabulariesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListDefaultVocabularies)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listdefaultvocabulariespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        LanguageCode: VocabularyLanguageCodeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListDefaultVocabulariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListDefaultVocabularies.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listdefaultvocabulariespaginator)
        """

class ListEvaluationFormVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListEvaluationFormVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listevaluationformversionspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        EvaluationFormId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListEvaluationFormVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListEvaluationFormVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listevaluationformversionspaginator)
        """

class ListEvaluationFormsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListEvaluationForms)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listevaluationformspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListEvaluationFormsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListEvaluationForms.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listevaluationformspaginator)
        """

class ListFlowAssociationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListFlowAssociations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listflowassociationspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        ResourceType: Literal["VOICE_PHONE_NUMBER"] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListFlowAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListFlowAssociations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listflowassociationspaginator)
        """

class ListHoursOfOperationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listhoursofoperationspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListHoursOfOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListHoursOfOperations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listhoursofoperationspaginator)
        """

class ListInstanceAttributesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listinstanceattributespaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListInstanceAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceAttributes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listinstanceattributespaginator)
        """

class ListInstanceStorageConfigsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listinstancestorageconfigspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        ResourceType: InstanceStorageResourceTypeType,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListInstanceStorageConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstanceStorageConfigs.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listinstancestorageconfigspaginator)
        """

class ListInstancesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstances)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listinstancespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListInstances.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listinstancespaginator)
        """

class ListIntegrationAssociationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listintegrationassociationspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        IntegrationType: IntegrationTypeType = ...,
        IntegrationArn: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListIntegrationAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListIntegrationAssociations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listintegrationassociationspaginator)
        """

class ListLambdaFunctionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listlambdafunctionspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListLambdaFunctionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLambdaFunctions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listlambdafunctionspaginator)
        """

class ListLexBotsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLexBots)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listlexbotspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListLexBotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListLexBots.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listlexbotspaginator)
        """

class ListPhoneNumbersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listphonenumberspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        PhoneNumberTypes: Sequence[PhoneNumberTypeType] = ...,
        PhoneNumberCountryCodes: Sequence[PhoneNumberCountryCodeType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPhoneNumbersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPhoneNumbers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listphonenumberspaginator)
        """

class ListPhoneNumbersV2Paginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPhoneNumbersV2)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listphonenumbersv2paginator)
    """

    def paginate(
        self,
        *,
        TargetArn: str = ...,
        InstanceId: str = ...,
        PhoneNumberCountryCodes: Sequence[PhoneNumberCountryCodeType] = ...,
        PhoneNumberTypes: Sequence[PhoneNumberTypeType] = ...,
        PhoneNumberPrefix: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListPhoneNumbersV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPhoneNumbersV2.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listphonenumbersv2paginator)
        """

class ListPredefinedAttributesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPredefinedAttributes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listpredefinedattributespaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPredefinedAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPredefinedAttributes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listpredefinedattributespaginator)
        """

class ListPromptsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPrompts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listpromptspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListPrompts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listpromptspaginator)
        """

class ListQueueQuickConnectsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listqueuequickconnectspaginator)
    """

    def paginate(
        self, *, InstanceId: str, QueueId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListQueueQuickConnectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueueQuickConnects.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listqueuequickconnectspaginator)
        """

class ListQueuesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueues)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listqueuespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        QueueTypes: Sequence[QueueTypeType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQueues.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listqueuespaginator)
        """

class ListQuickConnectsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQuickConnects)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listquickconnectspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        QuickConnectTypes: Sequence[QuickConnectTypeType] = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListQuickConnectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListQuickConnects.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listquickconnectspaginator)
        """

class ListRoutingProfileQueuesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listroutingprofilequeuespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        RoutingProfileId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRoutingProfileQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfileQueues.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listroutingprofilequeuespaginator)
        """

class ListRoutingProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listroutingprofilespaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListRoutingProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRoutingProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listroutingprofilespaginator)
        """

class ListRulesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRules)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listrulespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        PublishStatus: RulePublishStatusType = ...,
        EventSourceName: EventSourceNameType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListRules.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listrulespaginator)
        """

class ListSecurityKeysPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityKeys)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecuritykeyspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListSecurityKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityKeys.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecuritykeyspaginator)
        """

class ListSecurityProfileApplicationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfileApplications)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecurityprofileapplicationspaginator)
    """

    def paginate(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSecurityProfileApplicationsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfileApplications.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecurityprofileapplicationspaginator)
        """

class ListSecurityProfilePermissionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfilePermissions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecurityprofilepermissionspaginator)
    """

    def paginate(
        self,
        *,
        SecurityProfileId: str,
        InstanceId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListSecurityProfilePermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfilePermissions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecurityprofilepermissionspaginator)
        """

class ListSecurityProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecurityprofilespaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListSecurityProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListSecurityProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listsecurityprofilespaginator)
        """

class ListTaskTemplatesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListTaskTemplates)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listtasktemplatespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        Status: TaskTemplateStatusType = ...,
        Name: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListTaskTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListTaskTemplates.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listtasktemplatespaginator)
        """

class ListTrafficDistributionGroupUsersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListTrafficDistributionGroupUsers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listtrafficdistributiongroupuserspaginator)
    """

    def paginate(
        self, *, TrafficDistributionGroupId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListTrafficDistributionGroupUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListTrafficDistributionGroupUsers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listtrafficdistributiongroupuserspaginator)
        """

class ListTrafficDistributionGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListTrafficDistributionGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listtrafficdistributiongroupspaginator)
    """

    def paginate(
        self, *, InstanceId: str = ..., PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListTrafficDistributionGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListTrafficDistributionGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listtrafficdistributiongroupspaginator)
        """

class ListUseCasesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUseCases)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listusecasespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        IntegrationAssociationId: str,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListUseCasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUseCases.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listusecasespaginator)
        """

class ListUserHierarchyGroupsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listuserhierarchygroupspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListUserHierarchyGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUserHierarchyGroups.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listuserhierarchygroupspaginator)
        """

class ListUserProficienciesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUserProficiencies)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listuserproficienciespaginator)
    """

    def paginate(
        self, *, InstanceId: str, UserId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListUserProficienciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUserProficiencies.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listuserproficienciespaginator)
        """

class ListUsersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUsers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listuserspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListUsers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listuserspaginator)
        """

class ListViewVersionsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListViewVersions)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listviewversionspaginator)
    """

    def paginate(
        self, *, InstanceId: str, ViewId: str, PaginationConfig: PaginatorConfigTypeDef = ...
    ) -> AsyncIterator[ListViewVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListViewVersions.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listviewversionspaginator)
        """

class ListViewsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListViews)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listviewspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        Type: ViewTypeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[ListViewsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.ListViews.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#listviewspaginator)
        """

class SearchAvailablePhoneNumbersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchAvailablePhoneNumbers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchavailablephonenumberspaginator)
    """

    def paginate(
        self,
        *,
        PhoneNumberCountryCode: PhoneNumberCountryCodeType,
        PhoneNumberType: PhoneNumberTypeType,
        TargetArn: str = ...,
        InstanceId: str = ...,
        PhoneNumberPrefix: str = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchAvailablePhoneNumbersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchAvailablePhoneNumbers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchavailablephonenumberspaginator)
        """

class SearchContactsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchContacts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchcontactspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        TimeRange: SearchContactsTimeRangeTypeDef,
        SearchCriteria: SearchCriteriaTypeDef = ...,
        Sort: SortTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchContactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchContacts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchcontactspaginator)
        """

class SearchHoursOfOperationsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchHoursOfOperations)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchhoursofoperationspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchFilter: HoursOfOperationSearchFilterTypeDef = ...,
        SearchCriteria: HoursOfOperationSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchHoursOfOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchHoursOfOperations.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchhoursofoperationspaginator)
        """

class SearchPredefinedAttributesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchPredefinedAttributes)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchpredefinedattributespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchCriteria: PredefinedAttributeSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchPredefinedAttributesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchPredefinedAttributes.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchpredefinedattributespaginator)
        """

class SearchPromptsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchPrompts)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchpromptspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchFilter: PromptSearchFilterTypeDef = ...,
        SearchCriteria: PromptSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchPrompts.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchpromptspaginator)
        """

class SearchQueuesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchQueues)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchqueuespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchFilter: QueueSearchFilterTypeDef = ...,
        SearchCriteria: QueueSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchQueues.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchqueuespaginator)
        """

class SearchQuickConnectsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchQuickConnects)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchquickconnectspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchFilter: QuickConnectSearchFilterTypeDef = ...,
        SearchCriteria: QuickConnectSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchQuickConnectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchQuickConnects.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchquickconnectspaginator)
        """

class SearchResourceTagsPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchResourceTags)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchresourcetagspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        ResourceTypes: Sequence[str] = ...,
        SearchCriteria: ResourceTagsSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchResourceTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchResourceTags.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchresourcetagspaginator)
        """

class SearchRoutingProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchRoutingProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchroutingprofilespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchFilter: RoutingProfileSearchFilterTypeDef = ...,
        SearchCriteria: RoutingProfileSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchRoutingProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchRoutingProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchroutingprofilespaginator)
        """

class SearchSecurityProfilesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchSecurityProfiles)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchsecurityprofilespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchCriteria: SecurityProfileSearchCriteriaTypeDef = ...,
        SearchFilter: SecurityProfilesSearchFilterTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchSecurityProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchSecurityProfiles.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchsecurityprofilespaginator)
        """

class SearchUsersPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchUsers)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchuserspaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        SearchFilter: UserSearchFilterTypeDef = ...,
        SearchCriteria: UserSearchCriteriaTypeDef = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchUsers.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchuserspaginator)
        """

class SearchVocabulariesPaginator(AioPaginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchVocabularies)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchvocabulariespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        State: VocabularyStateType = ...,
        NameStartsWith: str = ...,
        LanguageCode: VocabularyLanguageCodeType = ...,
        PaginationConfig: PaginatorConfigTypeDef = ...,
    ) -> AsyncIterator[SearchVocabulariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/connect.html#Connect.Paginator.SearchVocabularies.paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect/paginators/#searchvocabulariespaginator)
        """
