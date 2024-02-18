"""
Type annotations for iotevents service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_iotevents/type_defs/)

Usage::

    ```python
    from types_aiobotocore_iotevents.type_defs import AcknowledgeFlowTypeDef

    data: AcknowledgeFlowTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from .literals import (
    AlarmModelVersionStatusType,
    AnalysisResultLevelType,
    AnalysisStatusType,
    ComparisonOperatorType,
    DetectorModelVersionStatusType,
    EvaluationMethodType,
    InputStatusType,
    LoggingLevelType,
    PayloadTypeType,
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
    "AcknowledgeFlowTypeDef",
    "ClearTimerActionTypeDef",
    "ResetTimerActionTypeDef",
    "SetTimerActionTypeDef",
    "SetVariableActionTypeDef",
    "InitializationConfigurationTypeDef",
    "AlarmModelSummaryTypeDef",
    "AlarmModelVersionSummaryTypeDef",
    "SimpleRuleTypeDef",
    "AnalysisResultLocationTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyVariantTypeDef",
    "AttributeTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DetectorModelConfigurationTypeDef",
    "InputConfigurationTypeDef",
    "DeleteAlarmModelRequestRequestTypeDef",
    "DeleteDetectorModelRequestRequestTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DescribeAlarmModelRequestRequestTypeDef",
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    "DescribeDetectorModelRequestRequestTypeDef",
    "DescribeInputRequestRequestTypeDef",
    "DetectorDebugOptionTypeDef",
    "DetectorModelSummaryTypeDef",
    "DetectorModelVersionSummaryTypeDef",
    "PayloadTypeDef",
    "EmailContentTypeDef",
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    "IotEventsInputIdentifierTypeDef",
    "InputSummaryTypeDef",
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    "ListAlarmModelVersionsRequestRequestTypeDef",
    "ListAlarmModelsRequestRequestTypeDef",
    "ListDetectorModelVersionsRequestRequestTypeDef",
    "ListDetectorModelsRequestRequestTypeDef",
    "RoutedResourceTypeDef",
    "ListInputsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "SSOIdentityTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AlarmCapabilitiesTypeDef",
    "AlarmRuleTypeDef",
    "AnalysisResultTypeDef",
    "AssetPropertyValueTypeDef",
    "InputDefinitionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateAlarmModelResponseTypeDef",
    "DescribeDetectorModelAnalysisResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListAlarmModelVersionsResponseTypeDef",
    "ListAlarmModelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartDetectorModelAnalysisResponseTypeDef",
    "UpdateAlarmModelResponseTypeDef",
    "CreateDetectorModelResponseTypeDef",
    "UpdateDetectorModelResponseTypeDef",
    "CreateInputResponseTypeDef",
    "UpdateInputResponseTypeDef",
    "LoggingOptionsTypeDef",
    "ListDetectorModelsResponseTypeDef",
    "ListDetectorModelVersionsResponseTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "FirehoseActionTypeDef",
    "IotEventsActionTypeDef",
    "IotTopicPublishActionTypeDef",
    "LambdaActionTypeDef",
    "SNSTopicPublishActionTypeDef",
    "SqsActionTypeDef",
    "ListInputsResponseTypeDef",
    "IotSiteWiseInputIdentifierTypeDef",
    "ListInputRoutingsResponseTypeDef",
    "RecipientDetailTypeDef",
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    "IotSiteWiseActionTypeDef",
    "CreateInputRequestRequestTypeDef",
    "InputTypeDef",
    "UpdateInputRequestRequestTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "NotificationTargetActionsTypeDef",
    "InputIdentifierTypeDef",
    "EmailRecipientsTypeDef",
    "SMSConfigurationTypeDef",
    "ActionTypeDef",
    "AlarmActionTypeDef",
    "DescribeInputResponseTypeDef",
    "ListInputRoutingsRequestRequestTypeDef",
    "EmailConfigurationTypeDef",
    "EventTypeDef",
    "TransitionEventTypeDef",
    "AlarmEventActionsTypeDef",
    "NotificationActionTypeDef",
    "OnEnterLifecycleTypeDef",
    "OnExitLifecycleTypeDef",
    "OnInputLifecycleTypeDef",
    "AlarmNotificationTypeDef",
    "StateTypeDef",
    "CreateAlarmModelRequestRequestTypeDef",
    "DescribeAlarmModelResponseTypeDef",
    "UpdateAlarmModelRequestRequestTypeDef",
    "DetectorModelDefinitionTypeDef",
    "CreateDetectorModelRequestRequestTypeDef",
    "DetectorModelTypeDef",
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    "UpdateDetectorModelRequestRequestTypeDef",
    "DescribeDetectorModelResponseTypeDef",
)

AcknowledgeFlowTypeDef = TypedDict(
    "AcknowledgeFlowTypeDef",
    {
        "enabled": bool,
    },
)
ClearTimerActionTypeDef = TypedDict(
    "ClearTimerActionTypeDef",
    {
        "timerName": str,
    },
)
ResetTimerActionTypeDef = TypedDict(
    "ResetTimerActionTypeDef",
    {
        "timerName": str,
    },
)
SetTimerActionTypeDef = TypedDict(
    "SetTimerActionTypeDef",
    {
        "timerName": str,
        "seconds": NotRequired[int],
        "durationExpression": NotRequired[str],
    },
)
SetVariableActionTypeDef = TypedDict(
    "SetVariableActionTypeDef",
    {
        "variableName": str,
        "value": str,
    },
)
InitializationConfigurationTypeDef = TypedDict(
    "InitializationConfigurationTypeDef",
    {
        "disabledOnInitialization": bool,
    },
)
AlarmModelSummaryTypeDef = TypedDict(
    "AlarmModelSummaryTypeDef",
    {
        "creationTime": NotRequired[datetime],
        "alarmModelDescription": NotRequired[str],
        "alarmModelName": NotRequired[str],
    },
)
AlarmModelVersionSummaryTypeDef = TypedDict(
    "AlarmModelVersionSummaryTypeDef",
    {
        "alarmModelName": NotRequired[str],
        "alarmModelArn": NotRequired[str],
        "alarmModelVersion": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[AlarmModelVersionStatusType],
        "statusMessage": NotRequired[str],
    },
)
SimpleRuleTypeDef = TypedDict(
    "SimpleRuleTypeDef",
    {
        "inputProperty": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": str,
    },
)
AnalysisResultLocationTypeDef = TypedDict(
    "AnalysisResultLocationTypeDef",
    {
        "path": NotRequired[str],
    },
)
AssetPropertyTimestampTypeDef = TypedDict(
    "AssetPropertyTimestampTypeDef",
    {
        "timeInSeconds": str,
        "offsetInNanos": NotRequired[str],
    },
)
AssetPropertyVariantTypeDef = TypedDict(
    "AssetPropertyVariantTypeDef",
    {
        "stringValue": NotRequired[str],
        "integerValue": NotRequired[str],
        "doubleValue": NotRequired[str],
        "booleanValue": NotRequired[str],
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "jsonPath": str,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
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
DetectorModelConfigurationTypeDef = TypedDict(
    "DetectorModelConfigurationTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "detectorModelDescription": NotRequired[str],
        "detectorModelArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[DetectorModelVersionStatusType],
        "key": NotRequired[str],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "inputName": str,
        "inputArn": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "status": InputStatusType,
        "inputDescription": NotRequired[str],
    },
)
DeleteAlarmModelRequestRequestTypeDef = TypedDict(
    "DeleteAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
    },
)
DeleteDetectorModelRequestRequestTypeDef = TypedDict(
    "DeleteDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
    },
)
DeleteInputRequestRequestTypeDef = TypedDict(
    "DeleteInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)
DescribeAlarmModelRequestRequestTypeDef = TypedDict(
    "DescribeAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "alarmModelVersion": NotRequired[str],
    },
)
DescribeDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisRequestRequestTypeDef",
    {
        "analysisId": str,
    },
)
DescribeDetectorModelRequestRequestTypeDef = TypedDict(
    "DescribeDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelVersion": NotRequired[str],
    },
)
DescribeInputRequestRequestTypeDef = TypedDict(
    "DescribeInputRequestRequestTypeDef",
    {
        "inputName": str,
    },
)
DetectorDebugOptionTypeDef = TypedDict(
    "DetectorDebugOptionTypeDef",
    {
        "detectorModelName": str,
        "keyValue": NotRequired[str],
    },
)
DetectorModelSummaryTypeDef = TypedDict(
    "DetectorModelSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelDescription": NotRequired[str],
        "creationTime": NotRequired[datetime],
    },
)
DetectorModelVersionSummaryTypeDef = TypedDict(
    "DetectorModelVersionSummaryTypeDef",
    {
        "detectorModelName": NotRequired[str],
        "detectorModelVersion": NotRequired[str],
        "detectorModelArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[DetectorModelVersionStatusType],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
PayloadTypeDef = TypedDict(
    "PayloadTypeDef",
    {
        "contentExpression": str,
        "type": PayloadTypeType,
    },
)
EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "subject": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)
GetDetectorModelAnalysisResultsRequestRequestTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsRequestRequestTypeDef",
    {
        "analysisId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
IotEventsInputIdentifierTypeDef = TypedDict(
    "IotEventsInputIdentifierTypeDef",
    {
        "inputName": str,
    },
)
InputSummaryTypeDef = TypedDict(
    "InputSummaryTypeDef",
    {
        "inputName": NotRequired[str],
        "inputDescription": NotRequired[str],
        "inputArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "status": NotRequired[InputStatusType],
    },
)
IotSiteWiseAssetModelPropertyIdentifierTypeDef = TypedDict(
    "IotSiteWiseAssetModelPropertyIdentifierTypeDef",
    {
        "assetModelId": str,
        "propertyId": str,
    },
)
ListAlarmModelVersionsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelVersionsRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListAlarmModelsRequestRequestTypeDef = TypedDict(
    "ListAlarmModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDetectorModelVersionsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelVersionsRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListDetectorModelsRequestRequestTypeDef = TypedDict(
    "ListDetectorModelsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
RoutedResourceTypeDef = TypedDict(
    "RoutedResourceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)
ListInputsRequestRequestTypeDef = TypedDict(
    "ListInputsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
SSOIdentityTypeDef = TypedDict(
    "SSOIdentityTypeDef",
    {
        "identityStoreId": str,
        "userId": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AlarmCapabilitiesTypeDef = TypedDict(
    "AlarmCapabilitiesTypeDef",
    {
        "initializationConfiguration": NotRequired[InitializationConfigurationTypeDef],
        "acknowledgeFlow": NotRequired[AcknowledgeFlowTypeDef],
    },
)
AlarmRuleTypeDef = TypedDict(
    "AlarmRuleTypeDef",
    {
        "simpleRule": NotRequired[SimpleRuleTypeDef],
    },
)
AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "type": NotRequired[str],
        "level": NotRequired[AnalysisResultLevelType],
        "message": NotRequired[str],
        "locations": NotRequired[List[AnalysisResultLocationTypeDef]],
    },
)
AssetPropertyValueTypeDef = TypedDict(
    "AssetPropertyValueTypeDef",
    {
        "value": NotRequired[AssetPropertyVariantTypeDef],
        "timestamp": NotRequired[AssetPropertyTimestampTypeDef],
        "quality": NotRequired[str],
    },
)
InputDefinitionTypeDef = TypedDict(
    "InputDefinitionTypeDef",
    {
        "attributes": Sequence[AttributeTypeDef],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateAlarmModelResponseTypeDef = TypedDict(
    "CreateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDetectorModelAnalysisResponseTypeDef = TypedDict(
    "DescribeDetectorModelAnalysisResponseTypeDef",
    {
        "status": AnalysisStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlarmModelVersionsResponseTypeDef = TypedDict(
    "ListAlarmModelVersionsResponseTypeDef",
    {
        "alarmModelVersionSummaries": List[AlarmModelVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAlarmModelsResponseTypeDef = TypedDict(
    "ListAlarmModelsResponseTypeDef",
    {
        "alarmModelSummaries": List[AlarmModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDetectorModelAnalysisResponseTypeDef = TypedDict(
    "StartDetectorModelAnalysisResponseTypeDef",
    {
        "analysisId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAlarmModelResponseTypeDef = TypedDict(
    "UpdateAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDetectorModelResponseTypeDef = TypedDict(
    "CreateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDetectorModelResponseTypeDef = TypedDict(
    "UpdateDetectorModelResponseTypeDef",
    {
        "detectorModelConfiguration": DetectorModelConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef",
    {
        "inputConfiguration": InputConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingOptionsTypeDef = TypedDict(
    "LoggingOptionsTypeDef",
    {
        "roleArn": str,
        "level": LoggingLevelType,
        "enabled": bool,
        "detectorDebugOptions": NotRequired[List[DetectorDebugOptionTypeDef]],
    },
)
ListDetectorModelsResponseTypeDef = TypedDict(
    "ListDetectorModelsResponseTypeDef",
    {
        "detectorModelSummaries": List[DetectorModelSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDetectorModelVersionsResponseTypeDef = TypedDict(
    "ListDetectorModelVersionsResponseTypeDef",
    {
        "detectorModelVersionSummaries": List[DetectorModelVersionSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DynamoDBActionTypeDef = TypedDict(
    "DynamoDBActionTypeDef",
    {
        "hashKeyField": str,
        "hashKeyValue": str,
        "tableName": str,
        "hashKeyType": NotRequired[str],
        "rangeKeyType": NotRequired[str],
        "rangeKeyField": NotRequired[str],
        "rangeKeyValue": NotRequired[str],
        "operation": NotRequired[str],
        "payloadField": NotRequired[str],
        "payload": NotRequired[PayloadTypeDef],
    },
)
DynamoDBv2ActionTypeDef = TypedDict(
    "DynamoDBv2ActionTypeDef",
    {
        "tableName": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
FirehoseActionTypeDef = TypedDict(
    "FirehoseActionTypeDef",
    {
        "deliveryStreamName": str,
        "separator": NotRequired[str],
        "payload": NotRequired[PayloadTypeDef],
    },
)
IotEventsActionTypeDef = TypedDict(
    "IotEventsActionTypeDef",
    {
        "inputName": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
IotTopicPublishActionTypeDef = TypedDict(
    "IotTopicPublishActionTypeDef",
    {
        "mqttTopic": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
LambdaActionTypeDef = TypedDict(
    "LambdaActionTypeDef",
    {
        "functionArn": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
SNSTopicPublishActionTypeDef = TypedDict(
    "SNSTopicPublishActionTypeDef",
    {
        "targetArn": str,
        "payload": NotRequired[PayloadTypeDef],
    },
)
SqsActionTypeDef = TypedDict(
    "SqsActionTypeDef",
    {
        "queueUrl": str,
        "useBase64": NotRequired[bool],
        "payload": NotRequired[PayloadTypeDef],
    },
)
ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef",
    {
        "inputSummaries": List[InputSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IotSiteWiseInputIdentifierTypeDef = TypedDict(
    "IotSiteWiseInputIdentifierTypeDef",
    {
        "iotSiteWiseAssetModelPropertyIdentifier": NotRequired[
            IotSiteWiseAssetModelPropertyIdentifierTypeDef
        ],
    },
)
ListInputRoutingsResponseTypeDef = TypedDict(
    "ListInputRoutingsResponseTypeDef",
    {
        "routedResources": List[RoutedResourceTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RecipientDetailTypeDef = TypedDict(
    "RecipientDetailTypeDef",
    {
        "ssoIdentity": NotRequired[SSOIdentityTypeDef],
    },
)
GetDetectorModelAnalysisResultsResponseTypeDef = TypedDict(
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    {
        "analysisResults": List[AnalysisResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IotSiteWiseActionTypeDef = TypedDict(
    "IotSiteWiseActionTypeDef",
    {
        "entryId": NotRequired[str],
        "assetId": NotRequired[str],
        "propertyId": NotRequired[str],
        "propertyAlias": NotRequired[str],
        "propertyValue": NotRequired[AssetPropertyValueTypeDef],
    },
)
CreateInputRequestRequestTypeDef = TypedDict(
    "CreateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": InputDefinitionTypeDef,
        "inputDescription": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)
InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "inputConfiguration": NotRequired[InputConfigurationTypeDef],
        "inputDefinition": NotRequired[InputDefinitionTypeDef],
    },
)
UpdateInputRequestRequestTypeDef = TypedDict(
    "UpdateInputRequestRequestTypeDef",
    {
        "inputName": str,
        "inputDefinition": InputDefinitionTypeDef,
        "inputDescription": NotRequired[str],
    },
)
DescribeLoggingOptionsResponseTypeDef = TypedDict(
    "DescribeLoggingOptionsResponseTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "loggingOptions": LoggingOptionsTypeDef,
    },
)
NotificationTargetActionsTypeDef = TypedDict(
    "NotificationTargetActionsTypeDef",
    {
        "lambdaAction": NotRequired[LambdaActionTypeDef],
    },
)
InputIdentifierTypeDef = TypedDict(
    "InputIdentifierTypeDef",
    {
        "iotEventsInputIdentifier": NotRequired[IotEventsInputIdentifierTypeDef],
        "iotSiteWiseInputIdentifier": NotRequired[IotSiteWiseInputIdentifierTypeDef],
    },
)
EmailRecipientsTypeDef = TypedDict(
    "EmailRecipientsTypeDef",
    {
        "to": NotRequired[Sequence[RecipientDetailTypeDef]],
    },
)
SMSConfigurationTypeDef = TypedDict(
    "SMSConfigurationTypeDef",
    {
        "recipients": Sequence[RecipientDetailTypeDef],
        "senderId": NotRequired[str],
        "additionalMessage": NotRequired[str],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "setVariable": NotRequired[SetVariableActionTypeDef],
        "sns": NotRequired[SNSTopicPublishActionTypeDef],
        "iotTopicPublish": NotRequired[IotTopicPublishActionTypeDef],
        "setTimer": NotRequired[SetTimerActionTypeDef],
        "clearTimer": NotRequired[ClearTimerActionTypeDef],
        "resetTimer": NotRequired[ResetTimerActionTypeDef],
        "lambda": NotRequired[LambdaActionTypeDef],
        "iotEvents": NotRequired[IotEventsActionTypeDef],
        "sqs": NotRequired[SqsActionTypeDef],
        "firehose": NotRequired[FirehoseActionTypeDef],
        "dynamoDB": NotRequired[DynamoDBActionTypeDef],
        "dynamoDBv2": NotRequired[DynamoDBv2ActionTypeDef],
        "iotSiteWise": NotRequired[IotSiteWiseActionTypeDef],
    },
)
AlarmActionTypeDef = TypedDict(
    "AlarmActionTypeDef",
    {
        "sns": NotRequired[SNSTopicPublishActionTypeDef],
        "iotTopicPublish": NotRequired[IotTopicPublishActionTypeDef],
        "lambda": NotRequired[LambdaActionTypeDef],
        "iotEvents": NotRequired[IotEventsActionTypeDef],
        "sqs": NotRequired[SqsActionTypeDef],
        "firehose": NotRequired[FirehoseActionTypeDef],
        "dynamoDB": NotRequired[DynamoDBActionTypeDef],
        "dynamoDBv2": NotRequired[DynamoDBv2ActionTypeDef],
        "iotSiteWise": NotRequired[IotSiteWiseActionTypeDef],
    },
)
DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "input": InputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInputRoutingsRequestRequestTypeDef = TypedDict(
    "ListInputRoutingsRequestRequestTypeDef",
    {
        "inputIdentifier": InputIdentifierTypeDef,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
EmailConfigurationTypeDef = TypedDict(
    "EmailConfigurationTypeDef",
    {
        "from": str,
        "recipients": EmailRecipientsTypeDef,
        "content": NotRequired[EmailContentTypeDef],
    },
)
EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventName": str,
        "condition": NotRequired[str],
        "actions": NotRequired[Sequence[ActionTypeDef]],
    },
)
TransitionEventTypeDef = TypedDict(
    "TransitionEventTypeDef",
    {
        "eventName": str,
        "condition": str,
        "nextState": str,
        "actions": NotRequired[Sequence[ActionTypeDef]],
    },
)
AlarmEventActionsTypeDef = TypedDict(
    "AlarmEventActionsTypeDef",
    {
        "alarmActions": NotRequired[Sequence[AlarmActionTypeDef]],
    },
)
NotificationActionTypeDef = TypedDict(
    "NotificationActionTypeDef",
    {
        "action": NotificationTargetActionsTypeDef,
        "smsConfigurations": NotRequired[Sequence[SMSConfigurationTypeDef]],
        "emailConfigurations": NotRequired[Sequence[EmailConfigurationTypeDef]],
    },
)
OnEnterLifecycleTypeDef = TypedDict(
    "OnEnterLifecycleTypeDef",
    {
        "events": NotRequired[Sequence[EventTypeDef]],
    },
)
OnExitLifecycleTypeDef = TypedDict(
    "OnExitLifecycleTypeDef",
    {
        "events": NotRequired[Sequence[EventTypeDef]],
    },
)
OnInputLifecycleTypeDef = TypedDict(
    "OnInputLifecycleTypeDef",
    {
        "events": NotRequired[Sequence[EventTypeDef]],
        "transitionEvents": NotRequired[Sequence[TransitionEventTypeDef]],
    },
)
AlarmNotificationTypeDef = TypedDict(
    "AlarmNotificationTypeDef",
    {
        "notificationActions": NotRequired[Sequence[NotificationActionTypeDef]],
    },
)
StateTypeDef = TypedDict(
    "StateTypeDef",
    {
        "stateName": str,
        "onInput": NotRequired[OnInputLifecycleTypeDef],
        "onEnter": NotRequired[OnEnterLifecycleTypeDef],
        "onExit": NotRequired[OnExitLifecycleTypeDef],
    },
)
CreateAlarmModelRequestRequestTypeDef = TypedDict(
    "CreateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": AlarmRuleTypeDef,
        "alarmModelDescription": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "key": NotRequired[str],
        "severity": NotRequired[int],
        "alarmNotification": NotRequired[AlarmNotificationTypeDef],
        "alarmEventActions": NotRequired[AlarmEventActionsTypeDef],
        "alarmCapabilities": NotRequired[AlarmCapabilitiesTypeDef],
    },
)
DescribeAlarmModelResponseTypeDef = TypedDict(
    "DescribeAlarmModelResponseTypeDef",
    {
        "creationTime": datetime,
        "alarmModelArn": str,
        "alarmModelVersion": str,
        "lastUpdateTime": datetime,
        "status": AlarmModelVersionStatusType,
        "statusMessage": str,
        "alarmModelName": str,
        "alarmModelDescription": str,
        "roleArn": str,
        "key": str,
        "severity": int,
        "alarmRule": AlarmRuleTypeDef,
        "alarmNotification": AlarmNotificationTypeDef,
        "alarmEventActions": AlarmEventActionsTypeDef,
        "alarmCapabilities": AlarmCapabilitiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAlarmModelRequestRequestTypeDef = TypedDict(
    "UpdateAlarmModelRequestRequestTypeDef",
    {
        "alarmModelName": str,
        "roleArn": str,
        "alarmRule": AlarmRuleTypeDef,
        "alarmModelDescription": NotRequired[str],
        "severity": NotRequired[int],
        "alarmNotification": NotRequired[AlarmNotificationTypeDef],
        "alarmEventActions": NotRequired[AlarmEventActionsTypeDef],
        "alarmCapabilities": NotRequired[AlarmCapabilitiesTypeDef],
    },
)
DetectorModelDefinitionTypeDef = TypedDict(
    "DetectorModelDefinitionTypeDef",
    {
        "states": Sequence[StateTypeDef],
        "initialStateName": str,
    },
)
CreateDetectorModelRequestRequestTypeDef = TypedDict(
    "CreateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
        "roleArn": str,
        "detectorModelDescription": NotRequired[str],
        "key": NotRequired[str],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
DetectorModelTypeDef = TypedDict(
    "DetectorModelTypeDef",
    {
        "detectorModelDefinition": NotRequired[DetectorModelDefinitionTypeDef],
        "detectorModelConfiguration": NotRequired[DetectorModelConfigurationTypeDef],
    },
)
StartDetectorModelAnalysisRequestRequestTypeDef = TypedDict(
    "StartDetectorModelAnalysisRequestRequestTypeDef",
    {
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
    },
)
UpdateDetectorModelRequestRequestTypeDef = TypedDict(
    "UpdateDetectorModelRequestRequestTypeDef",
    {
        "detectorModelName": str,
        "detectorModelDefinition": DetectorModelDefinitionTypeDef,
        "roleArn": str,
        "detectorModelDescription": NotRequired[str],
        "evaluationMethod": NotRequired[EvaluationMethodType],
    },
)
DescribeDetectorModelResponseTypeDef = TypedDict(
    "DescribeDetectorModelResponseTypeDef",
    {
        "detectorModel": DetectorModelTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
