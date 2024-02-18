"""
Type annotations for bedrock-agent-runtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_bedrock_agent_runtime.type_defs import AccessDeniedExceptionTypeDef

    data: AccessDeniedExceptionTypeDef = ...
    ```
"""

import sys
from typing import Dict, List, Mapping

from aiobotocore.eventstream import AioEventStream

from .literals import CreationModeType, InvocationTypeType, PromptTypeType, SourceType, TypeType

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
    "AccessDeniedExceptionTypeDef",
    "ParameterTypeDef",
    "ActionGroupInvocationOutputTypeDef",
    "BadGatewayExceptionTypeDef",
    "ConflictExceptionTypeDef",
    "DependencyFailedExceptionTypeDef",
    "FailureTraceTypeDef",
    "FinalResponseTypeDef",
    "InferenceConfigurationTypeDef",
    "InternalServerExceptionTypeDef",
    "KnowledgeBaseLookupInputTypeDef",
    "SessionStateTypeDef",
    "ResponseMetadataTypeDef",
    "KnowledgeBaseQueryTypeDef",
    "KnowledgeBaseVectorSearchConfigurationTypeDef",
    "RetrievalResultContentTypeDef",
    "KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef",
    "RepromptResponseTypeDef",
    "RationaleTypeDef",
    "PaginatorConfigTypeDef",
    "PostProcessingParsedResponseTypeDef",
    "PreProcessingParsedResponseTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ServiceQuotaExceededExceptionTypeDef",
    "ThrottlingExceptionTypeDef",
    "ValidationExceptionTypeDef",
    "RetrievalResultS3LocationTypeDef",
    "RetrieveAndGenerateInputTypeDef",
    "RetrieveAndGenerateOutputTypeDef",
    "RetrieveAndGenerateSessionConfigurationTypeDef",
    "SpanTypeDef",
    "RequestBodyTypeDef",
    "ModelInvocationInputTypeDef",
    "InvokeAgentRequestRequestTypeDef",
    "KnowledgeBaseRetrievalConfigurationTypeDef",
    "RetrieveAndGenerateConfigurationTypeDef",
    "PostProcessingModelInvocationOutputTypeDef",
    "PreProcessingModelInvocationOutputTypeDef",
    "RetrievalResultLocationTypeDef",
    "TextResponsePartTypeDef",
    "ActionGroupInvocationInputTypeDef",
    "RetrieveRequestRequestTypeDef",
    "RetrieveRequestRetrievePaginateTypeDef",
    "RetrieveAndGenerateRequestRequestTypeDef",
    "PostProcessingTraceTypeDef",
    "PreProcessingTraceTypeDef",
    "KnowledgeBaseRetrievalResultTypeDef",
    "RetrievedReferenceTypeDef",
    "GeneratedResponsePartTypeDef",
    "InvocationInputTypeDef",
    "RetrieveResponseTypeDef",
    "KnowledgeBaseLookupOutputTypeDef",
    "CitationTypeDef",
    "ObservationTypeDef",
    "AttributionTypeDef",
    "RetrieveAndGenerateResponseTypeDef",
    "OrchestrationTraceTypeDef",
    "PayloadPartTypeDef",
    "TraceTypeDef",
    "TracePartTypeDef",
    "ResponseStreamTypeDef",
    "InvokeAgentResponseTypeDef",
)

AccessDeniedExceptionTypeDef = TypedDict(
    "AccessDeniedExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "name": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
    },
)
ActionGroupInvocationOutputTypeDef = TypedDict(
    "ActionGroupInvocationOutputTypeDef",
    {
        "text": NotRequired[str],
    },
)
BadGatewayExceptionTypeDef = TypedDict(
    "BadGatewayExceptionTypeDef",
    {
        "message": NotRequired[str],
        "resourceName": NotRequired[str],
    },
)
ConflictExceptionTypeDef = TypedDict(
    "ConflictExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
DependencyFailedExceptionTypeDef = TypedDict(
    "DependencyFailedExceptionTypeDef",
    {
        "message": NotRequired[str],
        "resourceName": NotRequired[str],
    },
)
FailureTraceTypeDef = TypedDict(
    "FailureTraceTypeDef",
    {
        "traceId": NotRequired[str],
        "failureReason": NotRequired[str],
    },
)
FinalResponseTypeDef = TypedDict(
    "FinalResponseTypeDef",
    {
        "text": NotRequired[str],
    },
)
InferenceConfigurationTypeDef = TypedDict(
    "InferenceConfigurationTypeDef",
    {
        "temperature": NotRequired[float],
        "topP": NotRequired[float],
        "topK": NotRequired[int],
        "maximumLength": NotRequired[int],
        "stopSequences": NotRequired[List[str]],
    },
)
InternalServerExceptionTypeDef = TypedDict(
    "InternalServerExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
KnowledgeBaseLookupInputTypeDef = TypedDict(
    "KnowledgeBaseLookupInputTypeDef",
    {
        "text": NotRequired[str],
        "knowledgeBaseId": NotRequired[str],
    },
)
SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "promptSessionAttributes": NotRequired[Mapping[str, str]],
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
KnowledgeBaseQueryTypeDef = TypedDict(
    "KnowledgeBaseQueryTypeDef",
    {
        "text": str,
    },
)
KnowledgeBaseVectorSearchConfigurationTypeDef = TypedDict(
    "KnowledgeBaseVectorSearchConfigurationTypeDef",
    {
        "numberOfResults": int,
    },
)
RetrievalResultContentTypeDef = TypedDict(
    "RetrievalResultContentTypeDef",
    {
        "text": str,
    },
)
KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef",
    {
        "knowledgeBaseId": str,
        "modelArn": str,
    },
)
RepromptResponseTypeDef = TypedDict(
    "RepromptResponseTypeDef",
    {
        "text": NotRequired[str],
        "source": NotRequired[SourceType],
    },
)
RationaleTypeDef = TypedDict(
    "RationaleTypeDef",
    {
        "traceId": NotRequired[str],
        "text": NotRequired[str],
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
PostProcessingParsedResponseTypeDef = TypedDict(
    "PostProcessingParsedResponseTypeDef",
    {
        "text": NotRequired[str],
    },
)
PreProcessingParsedResponseTypeDef = TypedDict(
    "PreProcessingParsedResponseTypeDef",
    {
        "rationale": NotRequired[str],
        "isValid": NotRequired[bool],
    },
)
ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ServiceQuotaExceededExceptionTypeDef = TypedDict(
    "ServiceQuotaExceededExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ThrottlingExceptionTypeDef = TypedDict(
    "ThrottlingExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ValidationExceptionTypeDef = TypedDict(
    "ValidationExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
RetrievalResultS3LocationTypeDef = TypedDict(
    "RetrievalResultS3LocationTypeDef",
    {
        "uri": NotRequired[str],
    },
)
RetrieveAndGenerateInputTypeDef = TypedDict(
    "RetrieveAndGenerateInputTypeDef",
    {
        "text": str,
    },
)
RetrieveAndGenerateOutputTypeDef = TypedDict(
    "RetrieveAndGenerateOutputTypeDef",
    {
        "text": str,
    },
)
RetrieveAndGenerateSessionConfigurationTypeDef = TypedDict(
    "RetrieveAndGenerateSessionConfigurationTypeDef",
    {
        "kmsKeyArn": str,
    },
)
SpanTypeDef = TypedDict(
    "SpanTypeDef",
    {
        "start": NotRequired[int],
        "end": NotRequired[int],
    },
)
RequestBodyTypeDef = TypedDict(
    "RequestBodyTypeDef",
    {
        "content": NotRequired[Dict[str, List[ParameterTypeDef]]],
    },
)
ModelInvocationInputTypeDef = TypedDict(
    "ModelInvocationInputTypeDef",
    {
        "traceId": NotRequired[str],
        "text": NotRequired[str],
        "type": NotRequired[PromptTypeType],
        "inferenceConfiguration": NotRequired[InferenceConfigurationTypeDef],
        "overrideLambda": NotRequired[str],
        "promptCreationMode": NotRequired[CreationModeType],
        "parserMode": NotRequired[CreationModeType],
    },
)
InvokeAgentRequestRequestTypeDef = TypedDict(
    "InvokeAgentRequestRequestTypeDef",
    {
        "agentId": str,
        "agentAliasId": str,
        "sessionId": str,
        "inputText": str,
        "sessionState": NotRequired[SessionStateTypeDef],
        "endSession": NotRequired[bool],
        "enableTrace": NotRequired[bool],
    },
)
KnowledgeBaseRetrievalConfigurationTypeDef = TypedDict(
    "KnowledgeBaseRetrievalConfigurationTypeDef",
    {
        "vectorSearchConfiguration": KnowledgeBaseVectorSearchConfigurationTypeDef,
    },
)
RetrieveAndGenerateConfigurationTypeDef = TypedDict(
    "RetrieveAndGenerateConfigurationTypeDef",
    {
        "type": Literal["KNOWLEDGE_BASE"],
        "knowledgeBaseConfiguration": NotRequired[
            KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef
        ],
    },
)
PostProcessingModelInvocationOutputTypeDef = TypedDict(
    "PostProcessingModelInvocationOutputTypeDef",
    {
        "traceId": NotRequired[str],
        "parsedResponse": NotRequired[PostProcessingParsedResponseTypeDef],
    },
)
PreProcessingModelInvocationOutputTypeDef = TypedDict(
    "PreProcessingModelInvocationOutputTypeDef",
    {
        "traceId": NotRequired[str],
        "parsedResponse": NotRequired[PreProcessingParsedResponseTypeDef],
    },
)
RetrievalResultLocationTypeDef = TypedDict(
    "RetrievalResultLocationTypeDef",
    {
        "type": Literal["S3"],
        "s3Location": NotRequired[RetrievalResultS3LocationTypeDef],
    },
)
TextResponsePartTypeDef = TypedDict(
    "TextResponsePartTypeDef",
    {
        "text": NotRequired[str],
        "span": NotRequired[SpanTypeDef],
    },
)
ActionGroupInvocationInputTypeDef = TypedDict(
    "ActionGroupInvocationInputTypeDef",
    {
        "actionGroupName": NotRequired[str],
        "verb": NotRequired[str],
        "apiPath": NotRequired[str],
        "parameters": NotRequired[List[ParameterTypeDef]],
        "requestBody": NotRequired[RequestBodyTypeDef],
    },
)
RetrieveRequestRequestTypeDef = TypedDict(
    "RetrieveRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "retrievalQuery": KnowledgeBaseQueryTypeDef,
        "retrievalConfiguration": NotRequired[KnowledgeBaseRetrievalConfigurationTypeDef],
        "nextToken": NotRequired[str],
    },
)
RetrieveRequestRetrievePaginateTypeDef = TypedDict(
    "RetrieveRequestRetrievePaginateTypeDef",
    {
        "knowledgeBaseId": str,
        "retrievalQuery": KnowledgeBaseQueryTypeDef,
        "retrievalConfiguration": NotRequired[KnowledgeBaseRetrievalConfigurationTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
RetrieveAndGenerateRequestRequestTypeDef = TypedDict(
    "RetrieveAndGenerateRequestRequestTypeDef",
    {
        "input": RetrieveAndGenerateInputTypeDef,
        "sessionId": NotRequired[str],
        "retrieveAndGenerateConfiguration": NotRequired[RetrieveAndGenerateConfigurationTypeDef],
        "sessionConfiguration": NotRequired[RetrieveAndGenerateSessionConfigurationTypeDef],
    },
)
PostProcessingTraceTypeDef = TypedDict(
    "PostProcessingTraceTypeDef",
    {
        "modelInvocationInput": NotRequired[ModelInvocationInputTypeDef],
        "modelInvocationOutput": NotRequired[PostProcessingModelInvocationOutputTypeDef],
    },
)
PreProcessingTraceTypeDef = TypedDict(
    "PreProcessingTraceTypeDef",
    {
        "modelInvocationInput": NotRequired[ModelInvocationInputTypeDef],
        "modelInvocationOutput": NotRequired[PreProcessingModelInvocationOutputTypeDef],
    },
)
KnowledgeBaseRetrievalResultTypeDef = TypedDict(
    "KnowledgeBaseRetrievalResultTypeDef",
    {
        "content": RetrievalResultContentTypeDef,
        "location": NotRequired[RetrievalResultLocationTypeDef],
        "score": NotRequired[float],
    },
)
RetrievedReferenceTypeDef = TypedDict(
    "RetrievedReferenceTypeDef",
    {
        "content": NotRequired[RetrievalResultContentTypeDef],
        "location": NotRequired[RetrievalResultLocationTypeDef],
    },
)
GeneratedResponsePartTypeDef = TypedDict(
    "GeneratedResponsePartTypeDef",
    {
        "textResponsePart": NotRequired[TextResponsePartTypeDef],
    },
)
InvocationInputTypeDef = TypedDict(
    "InvocationInputTypeDef",
    {
        "traceId": NotRequired[str],
        "invocationType": NotRequired[InvocationTypeType],
        "actionGroupInvocationInput": NotRequired[ActionGroupInvocationInputTypeDef],
        "knowledgeBaseLookupInput": NotRequired[KnowledgeBaseLookupInputTypeDef],
    },
)
RetrieveResponseTypeDef = TypedDict(
    "RetrieveResponseTypeDef",
    {
        "retrievalResults": List[KnowledgeBaseRetrievalResultTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
KnowledgeBaseLookupOutputTypeDef = TypedDict(
    "KnowledgeBaseLookupOutputTypeDef",
    {
        "retrievedReferences": NotRequired[List[RetrievedReferenceTypeDef]],
    },
)
CitationTypeDef = TypedDict(
    "CitationTypeDef",
    {
        "generatedResponsePart": NotRequired[GeneratedResponsePartTypeDef],
        "retrievedReferences": NotRequired[List[RetrievedReferenceTypeDef]],
    },
)
ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "traceId": NotRequired[str],
        "type": NotRequired[TypeType],
        "actionGroupInvocationOutput": NotRequired[ActionGroupInvocationOutputTypeDef],
        "knowledgeBaseLookupOutput": NotRequired[KnowledgeBaseLookupOutputTypeDef],
        "finalResponse": NotRequired[FinalResponseTypeDef],
        "repromptResponse": NotRequired[RepromptResponseTypeDef],
    },
)
AttributionTypeDef = TypedDict(
    "AttributionTypeDef",
    {
        "citations": NotRequired[List[CitationTypeDef]],
    },
)
RetrieveAndGenerateResponseTypeDef = TypedDict(
    "RetrieveAndGenerateResponseTypeDef",
    {
        "sessionId": str,
        "output": RetrieveAndGenerateOutputTypeDef,
        "citations": List[CitationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OrchestrationTraceTypeDef = TypedDict(
    "OrchestrationTraceTypeDef",
    {
        "rationale": NotRequired[RationaleTypeDef],
        "invocationInput": NotRequired[InvocationInputTypeDef],
        "observation": NotRequired[ObservationTypeDef],
        "modelInvocationInput": NotRequired[ModelInvocationInputTypeDef],
    },
)
PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "bytes": NotRequired[bytes],
        "attribution": NotRequired[AttributionTypeDef],
    },
)
TraceTypeDef = TypedDict(
    "TraceTypeDef",
    {
        "preProcessingTrace": NotRequired[PreProcessingTraceTypeDef],
        "orchestrationTrace": NotRequired[OrchestrationTraceTypeDef],
        "postProcessingTrace": NotRequired[PostProcessingTraceTypeDef],
        "failureTrace": NotRequired[FailureTraceTypeDef],
    },
)
TracePartTypeDef = TypedDict(
    "TracePartTypeDef",
    {
        "agentId": NotRequired[str],
        "agentAliasId": NotRequired[str],
        "sessionId": NotRequired[str],
        "trace": NotRequired[TraceTypeDef],
    },
)
ResponseStreamTypeDef = TypedDict(
    "ResponseStreamTypeDef",
    {
        "chunk": NotRequired[PayloadPartTypeDef],
        "trace": NotRequired[TracePartTypeDef],
        "internalServerException": NotRequired[InternalServerExceptionTypeDef],
        "validationException": NotRequired[ValidationExceptionTypeDef],
        "resourceNotFoundException": NotRequired[ResourceNotFoundExceptionTypeDef],
        "serviceQuotaExceededException": NotRequired[ServiceQuotaExceededExceptionTypeDef],
        "throttlingException": NotRequired[ThrottlingExceptionTypeDef],
        "accessDeniedException": NotRequired[AccessDeniedExceptionTypeDef],
        "conflictException": NotRequired[ConflictExceptionTypeDef],
        "dependencyFailedException": NotRequired[DependencyFailedExceptionTypeDef],
        "badGatewayException": NotRequired[BadGatewayExceptionTypeDef],
    },
)
InvokeAgentResponseTypeDef = TypedDict(
    "InvokeAgentResponseTypeDef",
    {
        "completion": "AioEventStream[ResponseStreamTypeDef]",
        "contentType": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
