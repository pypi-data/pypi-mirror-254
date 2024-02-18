"""
Type annotations for customer-profiles service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_customer_profiles.client import CustomerProfilesClient

    session = get_session()
    async with session.create_client("customer-profiles") as client:
        client: CustomerProfilesClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    GenderType,
    MatchTypeType,
    PartyTypeType,
    StatisticType,
    StatusType,
    logicalOperatorType,
)
from .paginator import ListEventStreamsPaginator
from .type_defs import (
    AdditionalSearchKeyTypeDef,
    AddProfileKeyResponseTypeDef,
    AddressTypeDef,
    AttributeDetailsTypeDef,
    ConditionsTypeDef,
    ConflictResolutionTypeDef,
    ConsolidationTypeDef,
    CreateCalculatedAttributeDefinitionResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateEventStreamResponseTypeDef,
    CreateIntegrationWorkflowResponseTypeDef,
    CreateProfileResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteProfileKeyResponseTypeDef,
    DeleteProfileObjectResponseTypeDef,
    DeleteProfileObjectTypeResponseTypeDef,
    DeleteProfileResponseTypeDef,
    DetectProfileObjectTypeResponseTypeDef,
    FieldSourceProfileIdsTypeDef,
    FlowDefinitionTypeDef,
    GetAutoMergingPreviewResponseTypeDef,
    GetCalculatedAttributeDefinitionResponseTypeDef,
    GetCalculatedAttributeForProfileResponseTypeDef,
    GetDomainResponseTypeDef,
    GetEventStreamResponseTypeDef,
    GetIdentityResolutionJobResponseTypeDef,
    GetIntegrationResponseTypeDef,
    GetMatchesResponseTypeDef,
    GetProfileObjectTypeResponseTypeDef,
    GetProfileObjectTypeTemplateResponseTypeDef,
    GetSimilarProfilesResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowStepsResponseTypeDef,
    IntegrationConfigTypeDef,
    ListAccountIntegrationsResponseTypeDef,
    ListCalculatedAttributeDefinitionsResponseTypeDef,
    ListCalculatedAttributesForProfileResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEventStreamsResponseTypeDef,
    ListIdentityResolutionJobsResponseTypeDef,
    ListIntegrationsResponseTypeDef,
    ListProfileObjectsResponseTypeDef,
    ListProfileObjectTypesResponseTypeDef,
    ListProfileObjectTypeTemplatesResponseTypeDef,
    ListRuleBasedMatchesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    MatchingRequestTypeDef,
    MergeProfilesResponseTypeDef,
    ObjectFilterTypeDef,
    ObjectTypeFieldTypeDef,
    ObjectTypeKeyTypeDef,
    PutIntegrationResponseTypeDef,
    PutProfileObjectResponseTypeDef,
    PutProfileObjectTypeResponseTypeDef,
    RuleBasedMatchingRequestTypeDef,
    SearchProfilesResponseTypeDef,
    TimestampTypeDef,
    UpdateAddressTypeDef,
    UpdateCalculatedAttributeDefinitionResponseTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateProfileResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CustomerProfilesClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class CustomerProfilesClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CustomerProfilesClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#exceptions)
        """

    async def add_profile_key(
        self, *, ProfileId: str, KeyName: str, Values: Sequence[str], DomainName: str
    ) -> AddProfileKeyResponseTypeDef:
        """
        Associates a new key value with a specific profile, such as a Contact Record
        ContactId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.add_profile_key)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#add_profile_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#close)
        """

    async def create_calculated_attribute_definition(
        self,
        *,
        DomainName: str,
        CalculatedAttributeName: str,
        AttributeDetails: AttributeDetailsTypeDef,
        Statistic: StatisticType,
        DisplayName: str = ...,
        Description: str = ...,
        Conditions: ConditionsTypeDef = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateCalculatedAttributeDefinitionResponseTypeDef:
        """
        Creates a new calculated attribute definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_calculated_attribute_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#create_calculated_attribute_definition)
        """

    async def create_domain(
        self,
        *,
        DomainName: str,
        DefaultExpirationDays: int,
        DefaultEncryptionKey: str = ...,
        DeadLetterQueueUrl: str = ...,
        Matching: MatchingRequestTypeDef = ...,
        RuleBasedMatching: RuleBasedMatchingRequestTypeDef = ...,
        Tags: Mapping[str, str] = ...,
    ) -> CreateDomainResponseTypeDef:
        """
        Creates a domain, which is a container for all customer data, such as customer
        profile attributes, object types, profile keys, and encryption
        keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#create_domain)
        """

    async def create_event_stream(
        self, *, DomainName: str, Uri: str, EventStreamName: str, Tags: Mapping[str, str] = ...
    ) -> CreateEventStreamResponseTypeDef:
        """
        Creates an event stream, which is a subscription to real-time events, such as
        when profiles are created and updated through Amazon Connect Customer
        Profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_event_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#create_event_stream)
        """

    async def create_integration_workflow(
        self,
        *,
        DomainName: str,
        WorkflowType: Literal["APPFLOW_INTEGRATION"],
        IntegrationConfig: IntegrationConfigTypeDef,
        ObjectTypeName: str,
        RoleArn: str,
        Tags: Mapping[str, str] = ...,
    ) -> CreateIntegrationWorkflowResponseTypeDef:
        """
        Creates an integration workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_integration_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#create_integration_workflow)
        """

    async def create_profile(
        self,
        *,
        DomainName: str,
        AccountNumber: str = ...,
        AdditionalInformation: str = ...,
        PartyType: PartyTypeType = ...,
        BusinessName: str = ...,
        FirstName: str = ...,
        MiddleName: str = ...,
        LastName: str = ...,
        BirthDate: str = ...,
        Gender: GenderType = ...,
        PhoneNumber: str = ...,
        MobilePhoneNumber: str = ...,
        HomePhoneNumber: str = ...,
        BusinessPhoneNumber: str = ...,
        EmailAddress: str = ...,
        PersonalEmailAddress: str = ...,
        BusinessEmailAddress: str = ...,
        Address: AddressTypeDef = ...,
        ShippingAddress: AddressTypeDef = ...,
        MailingAddress: AddressTypeDef = ...,
        BillingAddress: AddressTypeDef = ...,
        Attributes: Mapping[str, str] = ...,
        PartyTypeString: str = ...,
        GenderString: str = ...,
    ) -> CreateProfileResponseTypeDef:
        """
        Creates a standard profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.create_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#create_profile)
        """

    async def delete_calculated_attribute_definition(
        self, *, DomainName: str, CalculatedAttributeName: str
    ) -> Dict[str, Any]:
        """
        Deletes an existing calculated attribute definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_calculated_attribute_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_calculated_attribute_definition)
        """

    async def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        Deletes a specific domain and all of its customer data, such as customer
        profile attributes and their related
        objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_domain)
        """

    async def delete_event_stream(self, *, DomainName: str, EventStreamName: str) -> Dict[str, Any]:
        """
        Disables and deletes the specified event stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_event_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_event_stream)
        """

    async def delete_integration(
        self, *, DomainName: str, Uri: str
    ) -> DeleteIntegrationResponseTypeDef:
        """
        Removes an integration from a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_integration)
        """

    async def delete_profile(
        self, *, ProfileId: str, DomainName: str
    ) -> DeleteProfileResponseTypeDef:
        """
        Deletes the standard customer profile and all data pertaining to the profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_profile)
        """

    async def delete_profile_key(
        self, *, ProfileId: str, KeyName: str, Values: Sequence[str], DomainName: str
    ) -> DeleteProfileKeyResponseTypeDef:
        """
        Removes a searchable key from a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_key)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_profile_key)
        """

    async def delete_profile_object(
        self, *, ProfileId: str, ProfileObjectUniqueKey: str, ObjectTypeName: str, DomainName: str
    ) -> DeleteProfileObjectResponseTypeDef:
        """
        Removes an object associated with a profile of a given ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_profile_object)
        """

    async def delete_profile_object_type(
        self, *, DomainName: str, ObjectTypeName: str
    ) -> DeleteProfileObjectTypeResponseTypeDef:
        """
        Removes a ProfileObjectType from a specific domain as well as removes all the
        ProfileObjects of that
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_profile_object_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_profile_object_type)
        """

    async def delete_workflow(self, *, DomainName: str, WorkflowId: str) -> Dict[str, Any]:
        """
        Deletes the specified workflow and all its corresponding resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.delete_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#delete_workflow)
        """

    async def detect_profile_object_type(
        self, *, Objects: Sequence[str], DomainName: str
    ) -> DetectProfileObjectTypeResponseTypeDef:
        """
        The process of detecting profile object type mapping by using given objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.detect_profile_object_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#detect_profile_object_type)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#generate_presigned_url)
        """

    async def get_auto_merging_preview(
        self,
        *,
        DomainName: str,
        Consolidation: ConsolidationTypeDef,
        ConflictResolution: ConflictResolutionTypeDef,
        MinAllowedConfidenceScoreForMerging: float = ...,
    ) -> GetAutoMergingPreviewResponseTypeDef:
        """
        Tests the auto-merging settings of your Identity Resolution Job without merging
        your
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_auto_merging_preview)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_auto_merging_preview)
        """

    async def get_calculated_attribute_definition(
        self, *, DomainName: str, CalculatedAttributeName: str
    ) -> GetCalculatedAttributeDefinitionResponseTypeDef:
        """
        Provides more information on a calculated attribute definition for Customer
        Profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_calculated_attribute_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_calculated_attribute_definition)
        """

    async def get_calculated_attribute_for_profile(
        self, *, DomainName: str, ProfileId: str, CalculatedAttributeName: str
    ) -> GetCalculatedAttributeForProfileResponseTypeDef:
        """
        Retrieve a calculated attribute for a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_calculated_attribute_for_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_calculated_attribute_for_profile)
        """

    async def get_domain(self, *, DomainName: str) -> GetDomainResponseTypeDef:
        """
        Returns information about a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_domain)
        """

    async def get_event_stream(
        self, *, DomainName: str, EventStreamName: str
    ) -> GetEventStreamResponseTypeDef:
        """
        Returns information about the specified event stream in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_event_stream)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_event_stream)
        """

    async def get_identity_resolution_job(
        self, *, DomainName: str, JobId: str
    ) -> GetIdentityResolutionJobResponseTypeDef:
        """
        Returns information about an Identity Resolution Job in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_identity_resolution_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_identity_resolution_job)
        """

    async def get_integration(self, *, DomainName: str, Uri: str) -> GetIntegrationResponseTypeDef:
        """
        Returns an integration for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_integration)
        """

    async def get_matches(
        self, *, DomainName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> GetMatchesResponseTypeDef:
        """
        Before calling this API, use
        [CreateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html)
        or
        [UpdateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html)
        to enable identity resolution: set `Matching` to
        tr...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_matches)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_matches)
        """

    async def get_profile_object_type(
        self, *, DomainName: str, ObjectTypeName: str
    ) -> GetProfileObjectTypeResponseTypeDef:
        """
        Returns the object types for a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_profile_object_type)
        """

    async def get_profile_object_type_template(
        self, *, TemplateId: str
    ) -> GetProfileObjectTypeTemplateResponseTypeDef:
        """
        Returns the template information for a specific object type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_profile_object_type_template)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_profile_object_type_template)
        """

    async def get_similar_profiles(
        self,
        *,
        DomainName: str,
        MatchType: MatchTypeType,
        SearchKey: str,
        SearchValue: str,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> GetSimilarProfilesResponseTypeDef:
        """
        Returns a set of profiles that belong to the same matching group using the
        `matchId` or
        `profileId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_similar_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_similar_profiles)
        """

    async def get_workflow(self, *, DomainName: str, WorkflowId: str) -> GetWorkflowResponseTypeDef:
        """
        Get details of specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_workflow)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_workflow)
        """

    async def get_workflow_steps(
        self, *, DomainName: str, WorkflowId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> GetWorkflowStepsResponseTypeDef:
        """
        Get granular list of steps in workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_workflow_steps)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_workflow_steps)
        """

    async def list_account_integrations(
        self, *, Uri: str, NextToken: str = ..., MaxResults: int = ..., IncludeHidden: bool = ...
    ) -> ListAccountIntegrationsResponseTypeDef:
        """
        Lists all of the integrations associated to a specific URI in the AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_account_integrations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_account_integrations)
        """

    async def list_calculated_attribute_definitions(
        self, *, DomainName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListCalculatedAttributeDefinitionsResponseTypeDef:
        """
        Lists calculated attribute definitions for Customer Profiles See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/ListCalculatedAttributeDefinitions).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_calculated_attribute_definitions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_calculated_attribute_definitions)
        """

    async def list_calculated_attributes_for_profile(
        self, *, DomainName: str, ProfileId: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListCalculatedAttributesForProfileResponseTypeDef:
        """
        Retrieve a list of calculated attributes for a customer profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_calculated_attributes_for_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_calculated_attributes_for_profile)
        """

    async def list_domains(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListDomainsResponseTypeDef:
        """
        Returns a list of all the domains for an AWS account that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_domains)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_domains)
        """

    async def list_event_streams(
        self, *, DomainName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListEventStreamsResponseTypeDef:
        """
        Returns a list of all the event streams in a specific domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_event_streams)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_event_streams)
        """

    async def list_identity_resolution_jobs(
        self, *, DomainName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListIdentityResolutionJobsResponseTypeDef:
        """
        Lists all of the Identity Resolution Jobs in your domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_identity_resolution_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_identity_resolution_jobs)
        """

    async def list_integrations(
        self,
        *,
        DomainName: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        IncludeHidden: bool = ...,
    ) -> ListIntegrationsResponseTypeDef:
        """
        Lists all of the integrations in your domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_integrations)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_integrations)
        """

    async def list_profile_object_type_templates(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListProfileObjectTypeTemplatesResponseTypeDef:
        """
        Lists all of the template information for object types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_type_templates)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_profile_object_type_templates)
        """

    async def list_profile_object_types(
        self, *, DomainName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListProfileObjectTypesResponseTypeDef:
        """
        Lists all of the templates available within the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_object_types)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_profile_object_types)
        """

    async def list_profile_objects(
        self,
        *,
        DomainName: str,
        ObjectTypeName: str,
        ProfileId: str,
        NextToken: str = ...,
        MaxResults: int = ...,
        ObjectFilter: ObjectFilterTypeDef = ...,
    ) -> ListProfileObjectsResponseTypeDef:
        """
        Returns a list of objects associated with a profile of a given
        ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_profile_objects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_profile_objects)
        """

    async def list_rule_based_matches(
        self, *, DomainName: str, NextToken: str = ..., MaxResults: int = ...
    ) -> ListRuleBasedMatchesResponseTypeDef:
        """
        Returns a set of `MatchIds` that belong to the given domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_rule_based_matches)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_rule_based_matches)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with an Amazon Connect Customer Profiles resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_tags_for_resource)
        """

    async def list_workflows(
        self,
        *,
        DomainName: str,
        WorkflowType: Literal["APPFLOW_INTEGRATION"] = ...,
        Status: StatusType = ...,
        QueryStartDate: TimestampTypeDef = ...,
        QueryEndDate: TimestampTypeDef = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ListWorkflowsResponseTypeDef:
        """
        Query to list all workflows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.list_workflows)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#list_workflows)
        """

    async def merge_profiles(
        self,
        *,
        DomainName: str,
        MainProfileId: str,
        ProfileIdsToBeMerged: Sequence[str],
        FieldSourceProfileIds: FieldSourceProfileIdsTypeDef = ...,
    ) -> MergeProfilesResponseTypeDef:
        """
        Runs an AWS Lambda job that does the following: * All the profileKeys in the
        `ProfileToBeMerged` will be moved to the main
        profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.merge_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#merge_profiles)
        """

    async def put_integration(
        self,
        *,
        DomainName: str,
        Uri: str = ...,
        ObjectTypeName: str = ...,
        Tags: Mapping[str, str] = ...,
        FlowDefinition: FlowDefinitionTypeDef = ...,
        ObjectTypeNames: Mapping[str, str] = ...,
    ) -> PutIntegrationResponseTypeDef:
        """
        Adds an integration between the service and a third-party service, which
        includes Amazon AppFlow and Amazon
        Connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.put_integration)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#put_integration)
        """

    async def put_profile_object(
        self, *, ObjectTypeName: str, Object: str, DomainName: str
    ) -> PutProfileObjectResponseTypeDef:
        """
        Adds additional objects to customer profiles of a given ObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#put_profile_object)
        """

    async def put_profile_object_type(
        self,
        *,
        DomainName: str,
        ObjectTypeName: str,
        Description: str,
        TemplateId: str = ...,
        ExpirationDays: int = ...,
        EncryptionKey: str = ...,
        AllowProfileCreation: bool = ...,
        SourceLastUpdatedTimestampFormat: str = ...,
        Fields: Mapping[str, ObjectTypeFieldTypeDef] = ...,
        Keys: Mapping[str, Sequence[ObjectTypeKeyTypeDef]] = ...,
        Tags: Mapping[str, str] = ...,
    ) -> PutProfileObjectTypeResponseTypeDef:
        """
        Defines a ProfileObjectType.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.put_profile_object_type)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#put_profile_object_type)
        """

    async def search_profiles(
        self,
        *,
        DomainName: str,
        KeyName: str,
        Values: Sequence[str],
        NextToken: str = ...,
        MaxResults: int = ...,
        AdditionalSearchKeys: Sequence[AdditionalSearchKeyTypeDef] = ...,
        LogicalOperator: logicalOperatorType = ...,
    ) -> SearchProfilesResponseTypeDef:
        """
        Searches for profiles within a specific domain using one or more predefined
        search keys (e.g., _fullName, _phone, _email, _account, etc.) and/or
        custom-defined search
        keys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.search_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#search_profiles)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Mapping[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified Amazon Connect
        Customer Profiles
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified Amazon Connect Customer Profiles
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#untag_resource)
        """

    async def update_calculated_attribute_definition(
        self,
        *,
        DomainName: str,
        CalculatedAttributeName: str,
        DisplayName: str = ...,
        Description: str = ...,
        Conditions: ConditionsTypeDef = ...,
    ) -> UpdateCalculatedAttributeDefinitionResponseTypeDef:
        """
        Updates an existing calculated attribute definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.update_calculated_attribute_definition)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#update_calculated_attribute_definition)
        """

    async def update_domain(
        self,
        *,
        DomainName: str,
        DefaultExpirationDays: int = ...,
        DefaultEncryptionKey: str = ...,
        DeadLetterQueueUrl: str = ...,
        Matching: MatchingRequestTypeDef = ...,
        RuleBasedMatching: RuleBasedMatchingRequestTypeDef = ...,
        Tags: Mapping[str, str] = ...,
    ) -> UpdateDomainResponseTypeDef:
        """
        Updates the properties of a domain, including creating or selecting a dead
        letter queue or an encryption
        key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.update_domain)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#update_domain)
        """

    async def update_profile(
        self,
        *,
        DomainName: str,
        ProfileId: str,
        AdditionalInformation: str = ...,
        AccountNumber: str = ...,
        PartyType: PartyTypeType = ...,
        BusinessName: str = ...,
        FirstName: str = ...,
        MiddleName: str = ...,
        LastName: str = ...,
        BirthDate: str = ...,
        Gender: GenderType = ...,
        PhoneNumber: str = ...,
        MobilePhoneNumber: str = ...,
        HomePhoneNumber: str = ...,
        BusinessPhoneNumber: str = ...,
        EmailAddress: str = ...,
        PersonalEmailAddress: str = ...,
        BusinessEmailAddress: str = ...,
        Address: UpdateAddressTypeDef = ...,
        ShippingAddress: UpdateAddressTypeDef = ...,
        MailingAddress: UpdateAddressTypeDef = ...,
        BillingAddress: UpdateAddressTypeDef = ...,
        Attributes: Mapping[str, str] = ...,
        PartyTypeString: str = ...,
        GenderString: str = ...,
    ) -> UpdateProfileResponseTypeDef:
        """
        Updates the properties of a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.update_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#update_profile)
        """

    def get_paginator(
        self, operation_name: Literal["list_event_streams"]
    ) -> ListEventStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/#get_paginator)
        """

    async def __aenter__(self) -> "CustomerProfilesClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/customer-profiles.html#CustomerProfiles.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/client/)
        """
