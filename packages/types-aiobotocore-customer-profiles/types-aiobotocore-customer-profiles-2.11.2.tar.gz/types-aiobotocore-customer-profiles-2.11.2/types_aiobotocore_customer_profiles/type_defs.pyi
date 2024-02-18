"""
Type annotations for customer-profiles service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_customer_profiles/type_defs/)

Usage::

    ```python
    from types_aiobotocore_customer_profiles.type_defs import AddProfileKeyRequestRequestTypeDef

    data: AddProfileKeyRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AttributeMatchingModelType,
    ConflictResolvingModelType,
    DataPullModeType,
    EventStreamDestinationStatusType,
    EventStreamStateType,
    FieldContentTypeType,
    GenderType,
    IdentityResolutionJobStatusType,
    JobScheduleDayOfTheWeekType,
    MarketoConnectorOperatorType,
    MatchTypeType,
    OperatorPropertiesKeysType,
    OperatorType,
    PartyTypeType,
    RuleBasedMatchingStatusType,
    S3ConnectorOperatorType,
    SalesforceConnectorOperatorType,
    ServiceNowConnectorOperatorType,
    SourceConnectorTypeType,
    StandardIdentifierType,
    StatisticType,
    StatusType,
    TaskTypeType,
    TriggerTypeType,
    ZendeskConnectorOperatorType,
    logicalOperatorType,
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
    "AddProfileKeyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "AdditionalSearchKeyTypeDef",
    "AddressTypeDef",
    "AppflowIntegrationWorkflowAttributesTypeDef",
    "AppflowIntegrationWorkflowMetricsTypeDef",
    "AppflowIntegrationWorkflowStepTypeDef",
    "AttributeItemTypeDef",
    "AttributeTypesSelectorTypeDef",
    "ConflictResolutionTypeDef",
    "ConsolidationTypeDef",
    "TimestampTypeDef",
    "RangeTypeDef",
    "ThresholdTypeDef",
    "ConnectorOperatorTypeDef",
    "CreateEventStreamRequestRequestTypeDef",
    "DeleteCalculatedAttributeDefinitionRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteEventStreamRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteProfileKeyRequestRequestTypeDef",
    "DeleteProfileObjectRequestRequestTypeDef",
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DestinationSummaryTypeDef",
    "DetectProfileObjectTypeRequestRequestTypeDef",
    "ObjectTypeFieldTypeDef",
    "ObjectTypeKeyTypeDef",
    "DomainStatsTypeDef",
    "EventStreamDestinationDetailsTypeDef",
    "S3ExportingConfigTypeDef",
    "S3ExportingLocationTypeDef",
    "FieldSourceProfileIdsTypeDef",
    "FoundByKeyValueTypeDef",
    "GetCalculatedAttributeDefinitionRequestRequestTypeDef",
    "GetCalculatedAttributeForProfileRequestRequestTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetEventStreamRequestRequestTypeDef",
    "GetIdentityResolutionJobRequestRequestTypeDef",
    "JobStatsTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetMatchesRequestRequestTypeDef",
    "MatchItemTypeDef",
    "GetProfileObjectTypeRequestRequestTypeDef",
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    "GetSimilarProfilesRequestRequestTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowStepsRequestRequestTypeDef",
    "IncrementalPullConfigTypeDef",
    "JobScheduleTypeDef",
    "ListAccountIntegrationsRequestRequestTypeDef",
    "ListIntegrationItemTypeDef",
    "ListCalculatedAttributeDefinitionItemTypeDef",
    "ListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    "ListCalculatedAttributeForProfileItemTypeDef",
    "ListCalculatedAttributesForProfileRequestRequestTypeDef",
    "ListDomainItemTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListEventStreamsRequestRequestTypeDef",
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    "ListIntegrationsRequestRequestTypeDef",
    "ListProfileObjectTypeItemTypeDef",
    "ListProfileObjectTypeTemplateItemTypeDef",
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    "ListProfileObjectTypesRequestRequestTypeDef",
    "ListProfileObjectsItemTypeDef",
    "ObjectFilterTypeDef",
    "ListRuleBasedMatchesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListWorkflowsItemTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "MatchingRuleTypeDef",
    "PutProfileObjectRequestRequestTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "ZendeskSourcePropertiesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddressTypeDef",
    "AddProfileKeyResponseTypeDef",
    "CreateEventStreamResponseTypeDef",
    "CreateIntegrationWorkflowResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteProfileKeyResponseTypeDef",
    "DeleteProfileObjectResponseTypeDef",
    "DeleteProfileObjectTypeResponseTypeDef",
    "DeleteProfileResponseTypeDef",
    "GetAutoMergingPreviewResponseTypeDef",
    "GetCalculatedAttributeForProfileResponseTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetSimilarProfilesResponseTypeDef",
    "ListRuleBasedMatchesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MergeProfilesResponseTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutProfileObjectResponseTypeDef",
    "UpdateProfileResponseTypeDef",
    "SearchProfilesRequestRequestTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "WorkflowAttributesTypeDef",
    "WorkflowMetricsTypeDef",
    "WorkflowStepItemTypeDef",
    "AttributeDetailsTypeDef",
    "AutoMergingTypeDef",
    "GetAutoMergingPreviewRequestRequestTypeDef",
    "BatchTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "ConditionsTypeDef",
    "TaskTypeDef",
    "EventStreamSummaryTypeDef",
    "DetectedProfileObjectTypeTypeDef",
    "GetProfileObjectTypeResponseTypeDef",
    "GetProfileObjectTypeTemplateResponseTypeDef",
    "PutProfileObjectTypeRequestRequestTypeDef",
    "PutProfileObjectTypeResponseTypeDef",
    "GetEventStreamResponseTypeDef",
    "ExportingConfigTypeDef",
    "ExportingLocationTypeDef",
    "MergeProfilesRequestRequestTypeDef",
    "ProfileTypeDef",
    "GetMatchesResponseTypeDef",
    "ListAccountIntegrationsResponseTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    "ListCalculatedAttributesForProfileResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEventStreamsRequestListEventStreamsPaginateTypeDef",
    "ListProfileObjectTypesResponseTypeDef",
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    "ListProfileObjectsResponseTypeDef",
    "ListProfileObjectsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowStepsResponseTypeDef",
    "TriggerPropertiesTypeDef",
    "CreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    "UpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    "ListEventStreamsResponseTypeDef",
    "DetectProfileObjectTypeResponseTypeDef",
    "MatchingRequestTypeDef",
    "MatchingResponseTypeDef",
    "RuleBasedMatchingRequestTypeDef",
    "RuleBasedMatchingResponseTypeDef",
    "GetIdentityResolutionJobResponseTypeDef",
    "IdentityResolutionJobTypeDef",
    "SearchProfilesResponseTypeDef",
    "SourceFlowConfigTypeDef",
    "TriggerConfigTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "UpdateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "GetDomainResponseTypeDef",
    "UpdateDomainResponseTypeDef",
    "ListIdentityResolutionJobsResponseTypeDef",
    "FlowDefinitionTypeDef",
    "AppflowIntegrationTypeDef",
    "PutIntegrationRequestRequestTypeDef",
    "IntegrationConfigTypeDef",
    "CreateIntegrationWorkflowRequestRequestTypeDef",
)

AddProfileKeyRequestRequestTypeDef = TypedDict(
    "AddProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": Sequence[str],
        "DomainName": str,
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
AdditionalSearchKeyTypeDef = TypedDict(
    "AdditionalSearchKeyTypeDef",
    {
        "KeyName": str,
        "Values": Sequence[str],
    },
)
AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "Address1": NotRequired[str],
        "Address2": NotRequired[str],
        "Address3": NotRequired[str],
        "Address4": NotRequired[str],
        "City": NotRequired[str],
        "County": NotRequired[str],
        "State": NotRequired[str],
        "Province": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
    },
)
AppflowIntegrationWorkflowAttributesTypeDef = TypedDict(
    "AppflowIntegrationWorkflowAttributesTypeDef",
    {
        "SourceConnectorType": SourceConnectorTypeType,
        "ConnectorProfileName": str,
        "RoleArn": NotRequired[str],
    },
)
AppflowIntegrationWorkflowMetricsTypeDef = TypedDict(
    "AppflowIntegrationWorkflowMetricsTypeDef",
    {
        "RecordsProcessed": int,
        "StepsCompleted": int,
        "TotalSteps": int,
    },
)
AppflowIntegrationWorkflowStepTypeDef = TypedDict(
    "AppflowIntegrationWorkflowStepTypeDef",
    {
        "FlowName": str,
        "Status": StatusType,
        "ExecutionMessage": str,
        "RecordsProcessed": int,
        "BatchRecordsStartTime": str,
        "BatchRecordsEndTime": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
AttributeItemTypeDef = TypedDict(
    "AttributeItemTypeDef",
    {
        "Name": str,
    },
)
AttributeTypesSelectorTypeDef = TypedDict(
    "AttributeTypesSelectorTypeDef",
    {
        "AttributeMatchingModel": AttributeMatchingModelType,
        "Address": NotRequired[Sequence[str]],
        "PhoneNumber": NotRequired[Sequence[str]],
        "EmailAddress": NotRequired[Sequence[str]],
    },
)
ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "ConflictResolvingModel": ConflictResolvingModelType,
        "SourceName": NotRequired[str],
    },
)
ConsolidationTypeDef = TypedDict(
    "ConsolidationTypeDef",
    {
        "MatchingAttributesList": Sequence[Sequence[str]],
    },
)
TimestampTypeDef = Union[datetime, str]
RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "Value": int,
        "Unit": Literal["DAYS"],
    },
)
ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": str,
        "Operator": OperatorType,
    },
)
ConnectorOperatorTypeDef = TypedDict(
    "ConnectorOperatorTypeDef",
    {
        "Marketo": NotRequired[MarketoConnectorOperatorType],
        "S3": NotRequired[S3ConnectorOperatorType],
        "Salesforce": NotRequired[SalesforceConnectorOperatorType],
        "ServiceNow": NotRequired[ServiceNowConnectorOperatorType],
        "Zendesk": NotRequired[ZendeskConnectorOperatorType],
    },
)
CreateEventStreamRequestRequestTypeDef = TypedDict(
    "CreateEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "EventStreamName": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)
DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
DeleteEventStreamRequestRequestTypeDef = TypedDict(
    "DeleteEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
    },
)
DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)
DeleteProfileKeyRequestRequestTypeDef = TypedDict(
    "DeleteProfileKeyRequestRequestTypeDef",
    {
        "ProfileId": str,
        "KeyName": str,
        "Values": Sequence[str],
        "DomainName": str,
    },
)
DeleteProfileObjectRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ProfileObjectUniqueKey": str,
        "ObjectTypeName": str,
        "DomainName": str,
    },
)
DeleteProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DeleteProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)
DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "DomainName": str,
    },
)
DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)
DestinationSummaryTypeDef = TypedDict(
    "DestinationSummaryTypeDef",
    {
        "Uri": str,
        "Status": EventStreamDestinationStatusType,
        "UnhealthySince": NotRequired[datetime],
    },
)
DetectProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "DetectProfileObjectTypeRequestRequestTypeDef",
    {
        "Objects": Sequence[str],
        "DomainName": str,
    },
)
ObjectTypeFieldTypeDef = TypedDict(
    "ObjectTypeFieldTypeDef",
    {
        "Source": NotRequired[str],
        "Target": NotRequired[str],
        "ContentType": NotRequired[FieldContentTypeType],
    },
)
ObjectTypeKeyTypeDef = TypedDict(
    "ObjectTypeKeyTypeDef",
    {
        "StandardIdentifiers": NotRequired[List[StandardIdentifierType]],
        "FieldNames": NotRequired[List[str]],
    },
)
DomainStatsTypeDef = TypedDict(
    "DomainStatsTypeDef",
    {
        "ProfileCount": NotRequired[int],
        "MeteringProfileCount": NotRequired[int],
        "ObjectCount": NotRequired[int],
        "TotalSize": NotRequired[int],
    },
)
EventStreamDestinationDetailsTypeDef = TypedDict(
    "EventStreamDestinationDetailsTypeDef",
    {
        "Uri": str,
        "Status": EventStreamDestinationStatusType,
        "UnhealthySince": NotRequired[datetime],
        "Message": NotRequired[str],
    },
)
S3ExportingConfigTypeDef = TypedDict(
    "S3ExportingConfigTypeDef",
    {
        "S3BucketName": str,
        "S3KeyName": NotRequired[str],
    },
)
S3ExportingLocationTypeDef = TypedDict(
    "S3ExportingLocationTypeDef",
    {
        "S3BucketName": NotRequired[str],
        "S3KeyName": NotRequired[str],
    },
)
FieldSourceProfileIdsTypeDef = TypedDict(
    "FieldSourceProfileIdsTypeDef",
    {
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[str],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[str],
        "ShippingAddress": NotRequired[str],
        "MailingAddress": NotRequired[str],
        "BillingAddress": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
FoundByKeyValueTypeDef = TypedDict(
    "FoundByKeyValueTypeDef",
    {
        "KeyName": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)
GetCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "GetCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
    },
)
GetCalculatedAttributeForProfileRequestRequestTypeDef = TypedDict(
    "GetCalculatedAttributeForProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "CalculatedAttributeName": str,
    },
)
GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
GetEventStreamRequestRequestTypeDef = TypedDict(
    "GetEventStreamRequestRequestTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
    },
)
GetIdentityResolutionJobRequestRequestTypeDef = TypedDict(
    "GetIdentityResolutionJobRequestRequestTypeDef",
    {
        "DomainName": str,
        "JobId": str,
    },
)
JobStatsTypeDef = TypedDict(
    "JobStatsTypeDef",
    {
        "NumberOfProfilesReviewed": NotRequired[int],
        "NumberOfMatchesFound": NotRequired[int],
        "NumberOfMergesDone": NotRequired[int],
    },
)
GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": str,
    },
)
GetMatchesRequestRequestTypeDef = TypedDict(
    "GetMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
MatchItemTypeDef = TypedDict(
    "MatchItemTypeDef",
    {
        "MatchId": NotRequired[str],
        "ProfileIds": NotRequired[List[str]],
        "ConfidenceScore": NotRequired[float],
    },
)
GetProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
    },
)
GetProfileObjectTypeTemplateRequestRequestTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateRequestRequestTypeDef",
    {
        "TemplateId": str,
    },
)
GetSimilarProfilesRequestRequestTypeDef = TypedDict(
    "GetSimilarProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MatchType": MatchTypeType,
        "SearchKey": str,
        "SearchValue": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
    },
)
GetWorkflowStepsRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
IncrementalPullConfigTypeDef = TypedDict(
    "IncrementalPullConfigTypeDef",
    {
        "DatetimeTypeFieldName": NotRequired[str],
    },
)
JobScheduleTypeDef = TypedDict(
    "JobScheduleTypeDef",
    {
        "DayOfTheWeek": JobScheduleDayOfTheWeekType,
        "Time": str,
    },
)
ListAccountIntegrationsRequestRequestTypeDef = TypedDict(
    "ListAccountIntegrationsRequestRequestTypeDef",
    {
        "Uri": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeHidden": NotRequired[bool],
    },
)
ListIntegrationItemTypeDef = TypedDict(
    "ListIntegrationItemTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ObjectTypeName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "ObjectTypeNames": NotRequired[Dict[str, str]],
        "WorkflowId": NotRequired[str],
        "IsUnstructured": NotRequired[bool],
    },
)
ListCalculatedAttributeDefinitionItemTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionItemTypeDef",
    {
        "CalculatedAttributeName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListCalculatedAttributeDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListCalculatedAttributeForProfileItemTypeDef = TypedDict(
    "ListCalculatedAttributeForProfileItemTypeDef",
    {
        "CalculatedAttributeName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "IsDataPartial": NotRequired[str],
        "Value": NotRequired[str],
    },
)
ListCalculatedAttributesForProfileRequestRequestTypeDef = TypedDict(
    "ListCalculatedAttributesForProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDomainItemTypeDef = TypedDict(
    "ListDomainItemTypeDef",
    {
        "DomainName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
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
ListEventStreamsRequestRequestTypeDef = TypedDict(
    "ListEventStreamsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIdentityResolutionJobsRequestRequestTypeDef = TypedDict(
    "ListIdentityResolutionJobsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListIntegrationsRequestRequestTypeDef = TypedDict(
    "ListIntegrationsRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeHidden": NotRequired[bool],
    },
)
ListProfileObjectTypeItemTypeDef = TypedDict(
    "ListProfileObjectTypeItemTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListProfileObjectTypeTemplateItemTypeDef = TypedDict(
    "ListProfileObjectTypeTemplateItemTypeDef",
    {
        "TemplateId": NotRequired[str],
        "SourceName": NotRequired[str],
        "SourceObject": NotRequired[str],
    },
)
ListProfileObjectTypeTemplatesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProfileObjectTypesRequestRequestTypeDef = TypedDict(
    "ListProfileObjectTypesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListProfileObjectsItemTypeDef = TypedDict(
    "ListProfileObjectsItemTypeDef",
    {
        "ObjectTypeName": NotRequired[str],
        "ProfileObjectUniqueKey": NotRequired[str],
        "Object": NotRequired[str],
    },
)
ObjectFilterTypeDef = TypedDict(
    "ObjectFilterTypeDef",
    {
        "KeyName": str,
        "Values": Sequence[str],
    },
)
ListRuleBasedMatchesRequestRequestTypeDef = TypedDict(
    "ListRuleBasedMatchesRequestRequestTypeDef",
    {
        "DomainName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
ListWorkflowsItemTypeDef = TypedDict(
    "ListWorkflowsItemTypeDef",
    {
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "WorkflowId": str,
        "Status": StatusType,
        "StatusDescription": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
)
MarketoSourcePropertiesTypeDef = TypedDict(
    "MarketoSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
MatchingRuleTypeDef = TypedDict(
    "MatchingRuleTypeDef",
    {
        "Rule": Sequence[str],
    },
)
PutProfileObjectRequestRequestTypeDef = TypedDict(
    "PutProfileObjectRequestRequestTypeDef",
    {
        "ObjectTypeName": str,
        "Object": str,
        "DomainName": str,
    },
)
S3SourcePropertiesTypeDef = TypedDict(
    "S3SourcePropertiesTypeDef",
    {
        "BucketName": str,
        "BucketPrefix": NotRequired[str],
    },
)
SalesforceSourcePropertiesTypeDef = TypedDict(
    "SalesforceSourcePropertiesTypeDef",
    {
        "Object": str,
        "EnableDynamicFieldUpdate": NotRequired[bool],
        "IncludeDeletedRecords": NotRequired[bool],
    },
)
ServiceNowSourcePropertiesTypeDef = TypedDict(
    "ServiceNowSourcePropertiesTypeDef",
    {
        "Object": str,
    },
)
ZendeskSourcePropertiesTypeDef = TypedDict(
    "ZendeskSourcePropertiesTypeDef",
    {
        "Object": str,
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
UpdateAddressTypeDef = TypedDict(
    "UpdateAddressTypeDef",
    {
        "Address1": NotRequired[str],
        "Address2": NotRequired[str],
        "Address3": NotRequired[str],
        "Address4": NotRequired[str],
        "City": NotRequired[str],
        "County": NotRequired[str],
        "State": NotRequired[str],
        "Province": NotRequired[str],
        "Country": NotRequired[str],
        "PostalCode": NotRequired[str],
    },
)
AddProfileKeyResponseTypeDef = TypedDict(
    "AddProfileKeyResponseTypeDef",
    {
        "KeyName": str,
        "Values": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEventStreamResponseTypeDef = TypedDict(
    "CreateEventStreamResponseTypeDef",
    {
        "EventStreamArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateIntegrationWorkflowResponseTypeDef = TypedDict(
    "CreateIntegrationWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteIntegrationResponseTypeDef = TypedDict(
    "DeleteIntegrationResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileKeyResponseTypeDef = TypedDict(
    "DeleteProfileKeyResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileObjectResponseTypeDef = TypedDict(
    "DeleteProfileObjectResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileObjectTypeResponseTypeDef = TypedDict(
    "DeleteProfileObjectTypeResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAutoMergingPreviewResponseTypeDef = TypedDict(
    "GetAutoMergingPreviewResponseTypeDef",
    {
        "DomainName": str,
        "NumberOfMatchesInSample": int,
        "NumberOfProfilesInSample": int,
        "NumberOfProfilesWillBeMerged": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalculatedAttributeForProfileResponseTypeDef = TypedDict(
    "GetCalculatedAttributeForProfileResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "IsDataPartial": str,
        "Value": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIntegrationResponseTypeDef = TypedDict(
    "GetIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSimilarProfilesResponseTypeDef = TypedDict(
    "GetSimilarProfilesResponseTypeDef",
    {
        "ProfileIds": List[str],
        "MatchId": str,
        "MatchType": MatchTypeType,
        "RuleLevel": int,
        "ConfidenceScore": float,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRuleBasedMatchesResponseTypeDef = TypedDict(
    "ListRuleBasedMatchesResponseTypeDef",
    {
        "MatchIds": List[str],
        "NextToken": str,
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
MergeProfilesResponseTypeDef = TypedDict(
    "MergeProfilesResponseTypeDef",
    {
        "Message": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutIntegrationResponseTypeDef = TypedDict(
    "PutIntegrationResponseTypeDef",
    {
        "DomainName": str,
        "Uri": str,
        "ObjectTypeName": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ObjectTypeNames": Dict[str, str],
        "WorkflowId": str,
        "IsUnstructured": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProfileObjectResponseTypeDef = TypedDict(
    "PutProfileObjectResponseTypeDef",
    {
        "ProfileObjectUniqueKey": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateProfileResponseTypeDef = TypedDict(
    "UpdateProfileResponseTypeDef",
    {
        "ProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchProfilesRequestRequestTypeDef = TypedDict(
    "SearchProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "KeyName": str,
        "Values": Sequence[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AdditionalSearchKeys": NotRequired[Sequence[AdditionalSearchKeyTypeDef]],
        "LogicalOperator": NotRequired[logicalOperatorType],
    },
)
CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[AddressTypeDef],
        "ShippingAddress": NotRequired[AddressTypeDef],
        "MailingAddress": NotRequired[AddressTypeDef],
        "BillingAddress": NotRequired[AddressTypeDef],
        "Attributes": NotRequired[Mapping[str, str]],
        "PartyTypeString": NotRequired[str],
        "GenderString": NotRequired[str],
    },
)
WorkflowAttributesTypeDef = TypedDict(
    "WorkflowAttributesTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationWorkflowAttributesTypeDef],
    },
)
WorkflowMetricsTypeDef = TypedDict(
    "WorkflowMetricsTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationWorkflowMetricsTypeDef],
    },
)
WorkflowStepItemTypeDef = TypedDict(
    "WorkflowStepItemTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationWorkflowStepTypeDef],
    },
)
AttributeDetailsTypeDef = TypedDict(
    "AttributeDetailsTypeDef",
    {
        "Attributes": Sequence[AttributeItemTypeDef],
        "Expression": str,
    },
)
AutoMergingTypeDef = TypedDict(
    "AutoMergingTypeDef",
    {
        "Enabled": bool,
        "Consolidation": NotRequired[ConsolidationTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "MinAllowedConfidenceScoreForMerging": NotRequired[float],
    },
)
GetAutoMergingPreviewRequestRequestTypeDef = TypedDict(
    "GetAutoMergingPreviewRequestRequestTypeDef",
    {
        "DomainName": str,
        "Consolidation": ConsolidationTypeDef,
        "ConflictResolution": ConflictResolutionTypeDef,
        "MinAllowedConfidenceScoreForMerging": NotRequired[float],
    },
)
BatchTypeDef = TypedDict(
    "BatchTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
    },
)
ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": NotRequired[Literal["APPFLOW_INTEGRATION"]],
        "Status": NotRequired[StatusType],
        "QueryStartDate": NotRequired[TimestampTypeDef],
        "QueryEndDate": NotRequired[TimestampTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ScheduledTriggerPropertiesTypeDef = TypedDict(
    "ScheduledTriggerPropertiesTypeDef",
    {
        "ScheduleExpression": str,
        "DataPullMode": NotRequired[DataPullModeType],
        "ScheduleStartTime": NotRequired[TimestampTypeDef],
        "ScheduleEndTime": NotRequired[TimestampTypeDef],
        "Timezone": NotRequired[str],
        "ScheduleOffset": NotRequired[int],
        "FirstExecutionFrom": NotRequired[TimestampTypeDef],
    },
)
ConditionsTypeDef = TypedDict(
    "ConditionsTypeDef",
    {
        "Range": NotRequired[RangeTypeDef],
        "ObjectCount": NotRequired[int],
        "Threshold": NotRequired[ThresholdTypeDef],
    },
)
TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "SourceFields": Sequence[str],
        "TaskType": TaskTypeType,
        "ConnectorOperator": NotRequired[ConnectorOperatorTypeDef],
        "DestinationField": NotRequired[str],
        "TaskProperties": NotRequired[Mapping[OperatorPropertiesKeysType, str]],
    },
)
EventStreamSummaryTypeDef = TypedDict(
    "EventStreamSummaryTypeDef",
    {
        "DomainName": str,
        "EventStreamName": str,
        "EventStreamArn": str,
        "State": EventStreamStateType,
        "StoppedSince": NotRequired[datetime],
        "DestinationSummary": NotRequired[DestinationSummaryTypeDef],
        "Tags": NotRequired[Dict[str, str]],
    },
)
DetectedProfileObjectTypeTypeDef = TypedDict(
    "DetectedProfileObjectTypeTypeDef",
    {
        "SourceLastUpdatedTimestampFormat": NotRequired[str],
        "Fields": NotRequired[Dict[str, ObjectTypeFieldTypeDef]],
        "Keys": NotRequired[Dict[str, List[ObjectTypeKeyTypeDef]]],
    },
)
GetProfileObjectTypeResponseTypeDef = TypedDict(
    "GetProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, ObjectTypeFieldTypeDef],
        "Keys": Dict[str, List[ObjectTypeKeyTypeDef]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetProfileObjectTypeTemplateResponseTypeDef = TypedDict(
    "GetProfileObjectTypeTemplateResponseTypeDef",
    {
        "TemplateId": str,
        "SourceName": str,
        "SourceObject": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, ObjectTypeFieldTypeDef],
        "Keys": Dict[str, List[ObjectTypeKeyTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutProfileObjectTypeRequestRequestTypeDef = TypedDict(
    "PutProfileObjectTypeRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": NotRequired[str],
        "ExpirationDays": NotRequired[int],
        "EncryptionKey": NotRequired[str],
        "AllowProfileCreation": NotRequired[bool],
        "SourceLastUpdatedTimestampFormat": NotRequired[str],
        "Fields": NotRequired[Mapping[str, ObjectTypeFieldTypeDef]],
        "Keys": NotRequired[Mapping[str, Sequence[ObjectTypeKeyTypeDef]]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
PutProfileObjectTypeResponseTypeDef = TypedDict(
    "PutProfileObjectTypeResponseTypeDef",
    {
        "ObjectTypeName": str,
        "Description": str,
        "TemplateId": str,
        "ExpirationDays": int,
        "EncryptionKey": str,
        "AllowProfileCreation": bool,
        "SourceLastUpdatedTimestampFormat": str,
        "Fields": Dict[str, ObjectTypeFieldTypeDef],
        "Keys": Dict[str, List[ObjectTypeKeyTypeDef]],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetEventStreamResponseTypeDef = TypedDict(
    "GetEventStreamResponseTypeDef",
    {
        "DomainName": str,
        "EventStreamArn": str,
        "CreatedAt": datetime,
        "State": EventStreamStateType,
        "StoppedSince": datetime,
        "DestinationDetails": EventStreamDestinationDetailsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportingConfigTypeDef = TypedDict(
    "ExportingConfigTypeDef",
    {
        "S3Exporting": NotRequired[S3ExportingConfigTypeDef],
    },
)
ExportingLocationTypeDef = TypedDict(
    "ExportingLocationTypeDef",
    {
        "S3Exporting": NotRequired[S3ExportingLocationTypeDef],
    },
)
MergeProfilesRequestRequestTypeDef = TypedDict(
    "MergeProfilesRequestRequestTypeDef",
    {
        "DomainName": str,
        "MainProfileId": str,
        "ProfileIdsToBeMerged": Sequence[str],
        "FieldSourceProfileIds": NotRequired[FieldSourceProfileIdsTypeDef],
    },
)
ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileId": NotRequired[str],
        "AccountNumber": NotRequired[str],
        "AdditionalInformation": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[AddressTypeDef],
        "ShippingAddress": NotRequired[AddressTypeDef],
        "MailingAddress": NotRequired[AddressTypeDef],
        "BillingAddress": NotRequired[AddressTypeDef],
        "Attributes": NotRequired[Dict[str, str]],
        "FoundByItems": NotRequired[List[FoundByKeyValueTypeDef]],
        "PartyTypeString": NotRequired[str],
        "GenderString": NotRequired[str],
    },
)
GetMatchesResponseTypeDef = TypedDict(
    "GetMatchesResponseTypeDef",
    {
        "NextToken": str,
        "MatchGenerationDate": datetime,
        "PotentialMatches": int,
        "Matches": List[MatchItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountIntegrationsResponseTypeDef = TypedDict(
    "ListAccountIntegrationsResponseTypeDef",
    {
        "Items": List[ListIntegrationItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIntegrationsResponseTypeDef = TypedDict(
    "ListIntegrationsResponseTypeDef",
    {
        "Items": List[ListIntegrationItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCalculatedAttributeDefinitionsResponseTypeDef = TypedDict(
    "ListCalculatedAttributeDefinitionsResponseTypeDef",
    {
        "Items": List[ListCalculatedAttributeDefinitionItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListCalculatedAttributesForProfileResponseTypeDef = TypedDict(
    "ListCalculatedAttributesForProfileResponseTypeDef",
    {
        "Items": List[ListCalculatedAttributeForProfileItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Items": List[ListDomainItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventStreamsRequestListEventStreamsPaginateTypeDef = TypedDict(
    "ListEventStreamsRequestListEventStreamsPaginateTypeDef",
    {
        "DomainName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListProfileObjectTypesResponseTypeDef = TypedDict(
    "ListProfileObjectTypesResponseTypeDef",
    {
        "Items": List[ListProfileObjectTypeItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileObjectTypeTemplatesResponseTypeDef = TypedDict(
    "ListProfileObjectTypeTemplatesResponseTypeDef",
    {
        "Items": List[ListProfileObjectTypeTemplateItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileObjectsResponseTypeDef = TypedDict(
    "ListProfileObjectsResponseTypeDef",
    {
        "Items": List[ListProfileObjectsItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListProfileObjectsRequestRequestTypeDef = TypedDict(
    "ListProfileObjectsRequestRequestTypeDef",
    {
        "DomainName": str,
        "ObjectTypeName": str,
        "ProfileId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ObjectFilter": NotRequired[ObjectFilterTypeDef],
    },
)
ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Items": List[ListWorkflowsItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceConnectorPropertiesTypeDef = TypedDict(
    "SourceConnectorPropertiesTypeDef",
    {
        "Marketo": NotRequired[MarketoSourcePropertiesTypeDef],
        "S3": NotRequired[S3SourcePropertiesTypeDef],
        "Salesforce": NotRequired[SalesforceSourcePropertiesTypeDef],
        "ServiceNow": NotRequired[ServiceNowSourcePropertiesTypeDef],
        "Zendesk": NotRequired[ZendeskSourcePropertiesTypeDef],
    },
)
UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "DomainName": str,
        "ProfileId": str,
        "AdditionalInformation": NotRequired[str],
        "AccountNumber": NotRequired[str],
        "PartyType": NotRequired[PartyTypeType],
        "BusinessName": NotRequired[str],
        "FirstName": NotRequired[str],
        "MiddleName": NotRequired[str],
        "LastName": NotRequired[str],
        "BirthDate": NotRequired[str],
        "Gender": NotRequired[GenderType],
        "PhoneNumber": NotRequired[str],
        "MobilePhoneNumber": NotRequired[str],
        "HomePhoneNumber": NotRequired[str],
        "BusinessPhoneNumber": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "PersonalEmailAddress": NotRequired[str],
        "BusinessEmailAddress": NotRequired[str],
        "Address": NotRequired[UpdateAddressTypeDef],
        "ShippingAddress": NotRequired[UpdateAddressTypeDef],
        "MailingAddress": NotRequired[UpdateAddressTypeDef],
        "BillingAddress": NotRequired[UpdateAddressTypeDef],
        "Attributes": NotRequired[Mapping[str, str]],
        "PartyTypeString": NotRequired[str],
        "GenderString": NotRequired[str],
    },
)
GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Status": StatusType,
        "ErrorDescription": str,
        "StartDate": datetime,
        "LastUpdatedAt": datetime,
        "Attributes": WorkflowAttributesTypeDef,
        "Metrics": WorkflowMetricsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowStepsResponseTypeDef = TypedDict(
    "GetWorkflowStepsResponseTypeDef",
    {
        "WorkflowId": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "Items": List[WorkflowStepItemTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TriggerPropertiesTypeDef = TypedDict(
    "TriggerPropertiesTypeDef",
    {
        "Scheduled": NotRequired[ScheduledTriggerPropertiesTypeDef],
    },
)
CreateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
        "AttributeDetails": AttributeDetailsTypeDef,
        "Statistic": StatisticType,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "Conditions": NotRequired[ConditionsTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "CreateCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "AttributeDetails": AttributeDetailsTypeDef,
        "Conditions": ConditionsTypeDef,
        "Statistic": StatisticType,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "GetCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Statistic": StatisticType,
        "Conditions": ConditionsTypeDef,
        "AttributeDetails": AttributeDetailsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateCalculatedAttributeDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateCalculatedAttributeDefinitionRequestRequestTypeDef",
    {
        "DomainName": str,
        "CalculatedAttributeName": str,
        "DisplayName": NotRequired[str],
        "Description": NotRequired[str],
        "Conditions": NotRequired[ConditionsTypeDef],
    },
)
UpdateCalculatedAttributeDefinitionResponseTypeDef = TypedDict(
    "UpdateCalculatedAttributeDefinitionResponseTypeDef",
    {
        "CalculatedAttributeName": str,
        "DisplayName": str,
        "Description": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Statistic": StatisticType,
        "Conditions": ConditionsTypeDef,
        "AttributeDetails": AttributeDetailsTypeDef,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventStreamsResponseTypeDef = TypedDict(
    "ListEventStreamsResponseTypeDef",
    {
        "Items": List[EventStreamSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectProfileObjectTypeResponseTypeDef = TypedDict(
    "DetectProfileObjectTypeResponseTypeDef",
    {
        "DetectedProfileObjectTypes": List[DetectedProfileObjectTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MatchingRequestTypeDef = TypedDict(
    "MatchingRequestTypeDef",
    {
        "Enabled": bool,
        "JobSchedule": NotRequired[JobScheduleTypeDef],
        "AutoMerging": NotRequired[AutoMergingTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
MatchingResponseTypeDef = TypedDict(
    "MatchingResponseTypeDef",
    {
        "Enabled": NotRequired[bool],
        "JobSchedule": NotRequired[JobScheduleTypeDef],
        "AutoMerging": NotRequired[AutoMergingTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
RuleBasedMatchingRequestTypeDef = TypedDict(
    "RuleBasedMatchingRequestTypeDef",
    {
        "Enabled": bool,
        "MatchingRules": NotRequired[Sequence[MatchingRuleTypeDef]],
        "MaxAllowedRuleLevelForMerging": NotRequired[int],
        "MaxAllowedRuleLevelForMatching": NotRequired[int],
        "AttributeTypesSelector": NotRequired[AttributeTypesSelectorTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
RuleBasedMatchingResponseTypeDef = TypedDict(
    "RuleBasedMatchingResponseTypeDef",
    {
        "Enabled": NotRequired[bool],
        "MatchingRules": NotRequired[List[MatchingRuleTypeDef]],
        "Status": NotRequired[RuleBasedMatchingStatusType],
        "MaxAllowedRuleLevelForMerging": NotRequired[int],
        "MaxAllowedRuleLevelForMatching": NotRequired[int],
        "AttributeTypesSelector": NotRequired[AttributeTypesSelectorTypeDef],
        "ConflictResolution": NotRequired[ConflictResolutionTypeDef],
        "ExportingConfig": NotRequired[ExportingConfigTypeDef],
    },
)
GetIdentityResolutionJobResponseTypeDef = TypedDict(
    "GetIdentityResolutionJobResponseTypeDef",
    {
        "DomainName": str,
        "JobId": str,
        "Status": IdentityResolutionJobStatusType,
        "Message": str,
        "JobStartTime": datetime,
        "JobEndTime": datetime,
        "LastUpdatedAt": datetime,
        "JobExpirationTime": datetime,
        "AutoMerging": AutoMergingTypeDef,
        "ExportingLocation": ExportingLocationTypeDef,
        "JobStats": JobStatsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IdentityResolutionJobTypeDef = TypedDict(
    "IdentityResolutionJobTypeDef",
    {
        "DomainName": NotRequired[str],
        "JobId": NotRequired[str],
        "Status": NotRequired[IdentityResolutionJobStatusType],
        "JobStartTime": NotRequired[datetime],
        "JobEndTime": NotRequired[datetime],
        "JobStats": NotRequired[JobStatsTypeDef],
        "ExportingLocation": NotRequired[ExportingLocationTypeDef],
        "Message": NotRequired[str],
    },
)
SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Items": List[ProfileTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SourceFlowConfigTypeDef = TypedDict(
    "SourceFlowConfigTypeDef",
    {
        "ConnectorType": SourceConnectorTypeType,
        "SourceConnectorProperties": SourceConnectorPropertiesTypeDef,
        "ConnectorProfileName": NotRequired[str],
        "IncrementalPullConfig": NotRequired[IncrementalPullConfigTypeDef],
    },
)
TriggerConfigTypeDef = TypedDict(
    "TriggerConfigTypeDef",
    {
        "TriggerType": TriggerTypeType,
        "TriggerProperties": NotRequired[TriggerPropertiesTypeDef],
    },
)
CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": NotRequired[str],
        "DeadLetterQueueUrl": NotRequired[str],
        "Matching": NotRequired[MatchingRequestTypeDef],
        "RuleBasedMatching": NotRequired[RuleBasedMatchingRequestTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
UpdateDomainRequestRequestTypeDef = TypedDict(
    "UpdateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": NotRequired[int],
        "DefaultEncryptionKey": NotRequired[str],
        "DeadLetterQueueUrl": NotRequired[str],
        "Matching": NotRequired[MatchingRequestTypeDef],
        "RuleBasedMatching": NotRequired[RuleBasedMatchingRequestTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": MatchingResponseTypeDef,
        "RuleBasedMatching": RuleBasedMatchingResponseTypeDef,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Stats": DomainStatsTypeDef,
        "Matching": MatchingResponseTypeDef,
        "RuleBasedMatching": RuleBasedMatchingResponseTypeDef,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDomainResponseTypeDef = TypedDict(
    "UpdateDomainResponseTypeDef",
    {
        "DomainName": str,
        "DefaultExpirationDays": int,
        "DefaultEncryptionKey": str,
        "DeadLetterQueueUrl": str,
        "Matching": MatchingResponseTypeDef,
        "RuleBasedMatching": RuleBasedMatchingResponseTypeDef,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListIdentityResolutionJobsResponseTypeDef = TypedDict(
    "ListIdentityResolutionJobsResponseTypeDef",
    {
        "IdentityResolutionJobsList": List[IdentityResolutionJobTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FlowDefinitionTypeDef = TypedDict(
    "FlowDefinitionTypeDef",
    {
        "FlowName": str,
        "KmsArn": str,
        "SourceFlowConfig": SourceFlowConfigTypeDef,
        "Tasks": Sequence[TaskTypeDef],
        "TriggerConfig": TriggerConfigTypeDef,
        "Description": NotRequired[str],
    },
)
AppflowIntegrationTypeDef = TypedDict(
    "AppflowIntegrationTypeDef",
    {
        "FlowDefinition": FlowDefinitionTypeDef,
        "Batches": NotRequired[Sequence[BatchTypeDef]],
    },
)
PutIntegrationRequestRequestTypeDef = TypedDict(
    "PutIntegrationRequestRequestTypeDef",
    {
        "DomainName": str,
        "Uri": NotRequired[str],
        "ObjectTypeName": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "FlowDefinition": NotRequired[FlowDefinitionTypeDef],
        "ObjectTypeNames": NotRequired[Mapping[str, str]],
    },
)
IntegrationConfigTypeDef = TypedDict(
    "IntegrationConfigTypeDef",
    {
        "AppflowIntegration": NotRequired[AppflowIntegrationTypeDef],
    },
)
CreateIntegrationWorkflowRequestRequestTypeDef = TypedDict(
    "CreateIntegrationWorkflowRequestRequestTypeDef",
    {
        "DomainName": str,
        "WorkflowType": Literal["APPFLOW_INTEGRATION"],
        "IntegrationConfig": IntegrationConfigTypeDef,
        "ObjectTypeName": str,
        "RoleArn": str,
        "Tags": NotRequired[Mapping[str, str]],
    },
)
