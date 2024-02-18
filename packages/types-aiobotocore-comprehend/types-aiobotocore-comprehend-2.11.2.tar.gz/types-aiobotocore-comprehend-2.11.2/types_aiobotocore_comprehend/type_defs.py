"""
Type annotations for comprehend service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_comprehend/type_defs/)

Usage::

    ```python
    from types_aiobotocore_comprehend.type_defs import AugmentedManifestsListItemPaginatorTypeDef

    data: AugmentedManifestsListItemPaginatorTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from aiobotocore.response import StreamingBody

from .literals import (
    AugmentedManifestsDocumentTypeFormatType,
    BlockTypeType,
    DatasetDataFormatType,
    DatasetStatusType,
    DatasetTypeType,
    DocumentClassifierDataFormatType,
    DocumentClassifierDocumentTypeFormatType,
    DocumentClassifierModeType,
    DocumentReadActionType,
    DocumentReadFeatureTypesType,
    DocumentReadModeType,
    DocumentTypeType,
    EndpointStatusType,
    EntityRecognizerDataFormatType,
    EntityTypeType,
    FlywheelIterationStatusType,
    FlywheelStatusType,
    InputFormatType,
    JobStatusType,
    LanguageCodeType,
    ModelStatusType,
    ModelTypeType,
    PageBasedErrorCodeType,
    PageBasedWarningCodeType,
    PartOfSpeechTagTypeType,
    PiiEntitiesDetectionMaskModeType,
    PiiEntitiesDetectionModeType,
    PiiEntityTypeType,
    SentimentTypeType,
    SplitType,
    SyntaxLanguageCodeType,
    TargetedSentimentEntityTypeType,
    ToxicContentTypeType,
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
    "AugmentedManifestsListItemPaginatorTypeDef",
    "AugmentedManifestsListItemTypeDef",
    "DominantLanguageTypeDef",
    "BatchDetectDominantLanguageRequestRequestTypeDef",
    "BatchItemErrorTypeDef",
    "ResponseMetadataTypeDef",
    "BatchDetectEntitiesRequestRequestTypeDef",
    "KeyPhraseTypeDef",
    "BatchDetectKeyPhrasesRequestRequestTypeDef",
    "SentimentScoreTypeDef",
    "BatchDetectSentimentRequestRequestTypeDef",
    "BatchDetectSyntaxRequestRequestTypeDef",
    "BatchDetectTargetedSentimentRequestRequestTypeDef",
    "BlobTypeDef",
    "ChildBlockTypeDef",
    "RelationshipsListItemTypeDef",
    "BoundingBoxTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "DocumentReaderConfigTypeDef",
    "DocumentClassTypeDef",
    "DocumentLabelTypeDef",
    "DocumentTypeListItemTypeDef",
    "ErrorsListItemTypeDef",
    "WarningsListItemTypeDef",
    "ContainsPiiEntitiesRequestRequestTypeDef",
    "EntityLabelTypeDef",
    "TagTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "VpcConfigTypeDef",
    "DatasetAugmentedManifestsListItemTypeDef",
    "DatasetDocumentClassifierInputDataConfigTypeDef",
    "DatasetEntityRecognizerAnnotationsTypeDef",
    "DatasetEntityRecognizerDocumentsTypeDef",
    "DatasetEntityRecognizerEntityListTypeDef",
    "TimestampTypeDef",
    "DatasetPropertiesTypeDef",
    "DeleteDocumentClassifierRequestRequestTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEntityRecognizerRequestRequestTypeDef",
    "DeleteFlywheelRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDocumentClassificationJobRequestRequestTypeDef",
    "DescribeDocumentClassifierRequestRequestTypeDef",
    "DescribeDominantLanguageDetectionJobRequestRequestTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "EndpointPropertiesTypeDef",
    "DescribeEntitiesDetectionJobRequestRequestTypeDef",
    "DescribeEntityRecognizerRequestRequestTypeDef",
    "DescribeEventsDetectionJobRequestRequestTypeDef",
    "DescribeFlywheelIterationRequestRequestTypeDef",
    "DescribeFlywheelRequestRequestTypeDef",
    "DescribeKeyPhrasesDetectionJobRequestRequestTypeDef",
    "DescribePiiEntitiesDetectionJobRequestRequestTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    "DescribeTargetedSentimentDetectionJobRequestRequestTypeDef",
    "DescribeTopicsDetectionJobRequestRequestTypeDef",
    "DetectDominantLanguageRequestRequestTypeDef",
    "DetectKeyPhrasesRequestRequestTypeDef",
    "DetectPiiEntitiesRequestRequestTypeDef",
    "PiiEntityTypeDef",
    "DetectSentimentRequestRequestTypeDef",
    "DetectSyntaxRequestRequestTypeDef",
    "DetectTargetedSentimentRequestRequestTypeDef",
    "TextSegmentTypeDef",
    "DocumentClassificationConfigTypeDef",
    "OutputDataConfigTypeDef",
    "VpcConfigPaginatorTypeDef",
    "DocumentClassifierDocumentsTypeDef",
    "DocumentReaderConfigPaginatorTypeDef",
    "DocumentClassifierSummaryTypeDef",
    "ExtractedCharactersListItemTypeDef",
    "EntityTypesListItemTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityRecognizerOutputDataConfigTypeDef",
    "EntityRecognizerSummaryTypeDef",
    "FlywheelModelEvaluationMetricsTypeDef",
    "FlywheelSummaryTypeDef",
    "PointTypeDef",
    "PaginatorConfigTypeDef",
    "ListDocumentClassifierSummariesRequestRequestTypeDef",
    "ListEntityRecognizerSummariesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiOutputDataConfigTypeDef",
    "RedactionConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "StartFlywheelIterationRequestRequestTypeDef",
    "StopDominantLanguageDetectionJobRequestRequestTypeDef",
    "StopEntitiesDetectionJobRequestRequestTypeDef",
    "StopEventsDetectionJobRequestRequestTypeDef",
    "StopKeyPhrasesDetectionJobRequestRequestTypeDef",
    "StopPiiEntitiesDetectionJobRequestRequestTypeDef",
    "StopSentimentDetectionJobRequestRequestTypeDef",
    "StopTargetedSentimentDetectionJobRequestRequestTypeDef",
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    "ToxicContentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "BatchDetectDominantLanguageItemResultTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDocumentClassifierResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEntityRecognizerResponseTypeDef",
    "CreateFlywheelResponseTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DetectDominantLanguageResponseTypeDef",
    "ImportModelResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "StartDocumentClassificationJobResponseTypeDef",
    "StartDominantLanguageDetectionJobResponseTypeDef",
    "StartEntitiesDetectionJobResponseTypeDef",
    "StartEventsDetectionJobResponseTypeDef",
    "StartFlywheelIterationResponseTypeDef",
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    "StartSentimentDetectionJobResponseTypeDef",
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    "StartTopicsDetectionJobResponseTypeDef",
    "StopDominantLanguageDetectionJobResponseTypeDef",
    "StopEntitiesDetectionJobResponseTypeDef",
    "StopEventsDetectionJobResponseTypeDef",
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    "StopSentimentDetectionJobResponseTypeDef",
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    "UpdateEndpointResponseTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "DetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "DetectSentimentResponseTypeDef",
    "MentionSentimentTypeDef",
    "BlockReferenceTypeDef",
    "ClassifierMetadataTypeDef",
    "ClassifyDocumentRequestRequestTypeDef",
    "DetectEntitiesRequestRequestTypeDef",
    "InputDataConfigTypeDef",
    "ContainsPiiEntitiesResponseTypeDef",
    "CreateEndpointRequestRequestTypeDef",
    "ImportModelRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "DataSecurityConfigTypeDef",
    "UpdateDataSecurityConfigTypeDef",
    "DatasetEntityRecognizerInputDataConfigTypeDef",
    "DatasetFilterTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "EndpointFilterTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "FlywheelFilterTypeDef",
    "FlywheelIterationFilterTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "SentimentDetectionJobFilterTypeDef",
    "TargetedSentimentDetectionJobFilterTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "DescribeDatasetResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "DescribeEndpointResponseTypeDef",
    "ListEndpointsResponseTypeDef",
    "DetectPiiEntitiesResponseTypeDef",
    "DetectToxicContentRequestRequestTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierInputDataConfigPaginatorTypeDef",
    "InputDataConfigPaginatorTypeDef",
    "ListDocumentClassifierSummariesResponseTypeDef",
    "DocumentMetadataTypeDef",
    "EntityRecognitionConfigTypeDef",
    "EntityRecognizerInputDataConfigPaginatorTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "ListEntityRecognizerSummariesResponseTypeDef",
    "FlywheelIterationPropertiesTypeDef",
    "ListFlywheelsResponseTypeDef",
    "GeometryTypeDef",
    "SyntaxTokenTypeDef",
    "ToxicLabelsTypeDef",
    "BatchDetectDominantLanguageResponseTypeDef",
    "BatchDetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentResponseTypeDef",
    "TargetedSentimentMentionTypeDef",
    "EntityTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "StartDocumentClassificationJobRequestRequestTypeDef",
    "StartDominantLanguageDetectionJobRequestRequestTypeDef",
    "StartEntitiesDetectionJobRequestRequestTypeDef",
    "StartEventsDetectionJobRequestRequestTypeDef",
    "StartKeyPhrasesDetectionJobRequestRequestTypeDef",
    "StartPiiEntitiesDetectionJobRequestRequestTypeDef",
    "StartSentimentDetectionJobRequestRequestTypeDef",
    "StartTargetedSentimentDetectionJobRequestRequestTypeDef",
    "StartTopicsDetectionJobRequestRequestTypeDef",
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "UpdateFlywheelRequestRequestTypeDef",
    "DatasetInputDataConfigTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDocumentClassificationJobsRequestListDocumentClassificationJobsPaginateTypeDef",
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    "ListDocumentClassifiersRequestListDocumentClassifiersPaginateTypeDef",
    "ListDocumentClassifiersRequestRequestTypeDef",
    "ListDominantLanguageDetectionJobsRequestListDominantLanguageDetectionJobsPaginateTypeDef",
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    "ListEndpointsRequestListEndpointsPaginateTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEntitiesDetectionJobsRequestListEntitiesDetectionJobsPaginateTypeDef",
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    "ListEntityRecognizersRequestListEntityRecognizersPaginateTypeDef",
    "ListEntityRecognizersRequestRequestTypeDef",
    "ListEventsDetectionJobsRequestRequestTypeDef",
    "ListFlywheelsRequestRequestTypeDef",
    "ListFlywheelIterationHistoryRequestRequestTypeDef",
    "ListKeyPhrasesDetectionJobsRequestListKeyPhrasesDetectionJobsPaginateTypeDef",
    "ListKeyPhrasesDetectionJobsRequestRequestTypeDef",
    "ListPiiEntitiesDetectionJobsRequestListPiiEntitiesDetectionJobsPaginateTypeDef",
    "ListPiiEntitiesDetectionJobsRequestRequestTypeDef",
    "ListSentimentDetectionJobsRequestListSentimentDetectionJobsPaginateTypeDef",
    "ListSentimentDetectionJobsRequestRequestTypeDef",
    "ListTargetedSentimentDetectionJobsRequestRequestTypeDef",
    "ListTopicsDetectionJobsRequestListTopicsDetectionJobsPaginateTypeDef",
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    "CreateDocumentClassifierRequestRequestTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentClassifierPropertiesPaginatorTypeDef",
    "DocumentClassificationJobPropertiesPaginatorTypeDef",
    "DominantLanguageDetectionJobPropertiesPaginatorTypeDef",
    "EntitiesDetectionJobPropertiesPaginatorTypeDef",
    "KeyPhrasesDetectionJobPropertiesPaginatorTypeDef",
    "PiiEntitiesDetectionJobPropertiesPaginatorTypeDef",
    "SentimentDetectionJobPropertiesPaginatorTypeDef",
    "TopicsDetectionJobPropertiesPaginatorTypeDef",
    "ClassifyDocumentResponseTypeDef",
    "TaskConfigTypeDef",
    "CreateEntityRecognizerRequestRequestTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "DescribeFlywheelIterationResponseTypeDef",
    "ListFlywheelIterationHistoryResponseTypeDef",
    "BlockTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "DetectSyntaxResponseTypeDef",
    "DetectToxicContentResponseTypeDef",
    "TargetedSentimentEntityTypeDef",
    "BatchDetectEntitiesItemResultTypeDef",
    "DescribeDocumentClassificationJobResponseTypeDef",
    "ListDocumentClassificationJobsResponseTypeDef",
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    "DescribeEntitiesDetectionJobResponseTypeDef",
    "ListEntitiesDetectionJobsResponseTypeDef",
    "DescribeEventsDetectionJobResponseTypeDef",
    "ListEventsDetectionJobsResponseTypeDef",
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    "DescribeSentimentDetectionJobResponseTypeDef",
    "ListSentimentDetectionJobsResponseTypeDef",
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    "DescribeTopicsDetectionJobResponseTypeDef",
    "ListTopicsDetectionJobsResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "DescribeDocumentClassifierResponseTypeDef",
    "ListDocumentClassifiersResponseTypeDef",
    "ListDocumentClassifiersResponsePaginatorTypeDef",
    "ListDocumentClassificationJobsResponsePaginatorTypeDef",
    "ListDominantLanguageDetectionJobsResponsePaginatorTypeDef",
    "ListEntitiesDetectionJobsResponsePaginatorTypeDef",
    "ListKeyPhrasesDetectionJobsResponsePaginatorTypeDef",
    "ListPiiEntitiesDetectionJobsResponsePaginatorTypeDef",
    "ListSentimentDetectionJobsResponsePaginatorTypeDef",
    "ListTopicsDetectionJobsResponsePaginatorTypeDef",
    "CreateFlywheelRequestRequestTypeDef",
    "FlywheelPropertiesTypeDef",
    "EntityRecognizerPropertiesPaginatorTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "DetectEntitiesResponseTypeDef",
    "BatchDetectSyntaxResponseTypeDef",
    "BatchDetectTargetedSentimentItemResultTypeDef",
    "DetectTargetedSentimentResponseTypeDef",
    "BatchDetectEntitiesResponseTypeDef",
    "DescribeFlywheelResponseTypeDef",
    "UpdateFlywheelResponseTypeDef",
    "ListEntityRecognizersResponsePaginatorTypeDef",
    "DescribeEntityRecognizerResponseTypeDef",
    "ListEntityRecognizersResponseTypeDef",
    "BatchDetectTargetedSentimentResponseTypeDef",
)

AugmentedManifestsListItemPaginatorTypeDef = TypedDict(
    "AugmentedManifestsListItemPaginatorTypeDef",
    {
        "S3Uri": str,
        "AttributeNames": List[str],
        "Split": NotRequired[SplitType],
        "AnnotationDataS3Uri": NotRequired[str],
        "SourceDocumentsS3Uri": NotRequired[str],
        "DocumentType": NotRequired[AugmentedManifestsDocumentTypeFormatType],
    },
)
AugmentedManifestsListItemTypeDef = TypedDict(
    "AugmentedManifestsListItemTypeDef",
    {
        "S3Uri": str,
        "AttributeNames": Sequence[str],
        "Split": NotRequired[SplitType],
        "AnnotationDataS3Uri": NotRequired[str],
        "SourceDocumentsS3Uri": NotRequired[str],
        "DocumentType": NotRequired[AugmentedManifestsDocumentTypeFormatType],
    },
)
DominantLanguageTypeDef = TypedDict(
    "DominantLanguageTypeDef",
    {
        "LanguageCode": NotRequired[str],
        "Score": NotRequired[float],
    },
)
BatchDetectDominantLanguageRequestRequestTypeDef = TypedDict(
    "BatchDetectDominantLanguageRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
    },
)
BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Index": NotRequired[int],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
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
BatchDetectEntitiesRequestRequestTypeDef = TypedDict(
    "BatchDetectEntitiesRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)
KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {
        "Score": NotRequired[float],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
BatchDetectKeyPhrasesRequestRequestTypeDef = TypedDict(
    "BatchDetectKeyPhrasesRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)
SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "Positive": NotRequired[float],
        "Negative": NotRequired[float],
        "Neutral": NotRequired[float],
        "Mixed": NotRequired[float],
    },
)
BatchDetectSentimentRequestRequestTypeDef = TypedDict(
    "BatchDetectSentimentRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)
BatchDetectSyntaxRequestRequestTypeDef = TypedDict(
    "BatchDetectSyntaxRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": SyntaxLanguageCodeType,
    },
)
BatchDetectTargetedSentimentRequestRequestTypeDef = TypedDict(
    "BatchDetectTargetedSentimentRequestRequestTypeDef",
    {
        "TextList": Sequence[str],
        "LanguageCode": LanguageCodeType,
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
ChildBlockTypeDef = TypedDict(
    "ChildBlockTypeDef",
    {
        "ChildBlockId": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
RelationshipsListItemTypeDef = TypedDict(
    "RelationshipsListItemTypeDef",
    {
        "Ids": NotRequired[List[str]],
        "Type": NotRequired[Literal["CHILD"]],
    },
)
BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {
        "Height": NotRequired[float],
        "Left": NotRequired[float],
        "Top": NotRequired[float],
        "Width": NotRequired[float],
    },
)
ClassifierEvaluationMetricsTypeDef = TypedDict(
    "ClassifierEvaluationMetricsTypeDef",
    {
        "Accuracy": NotRequired[float],
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1Score": NotRequired[float],
        "MicroPrecision": NotRequired[float],
        "MicroRecall": NotRequired[float],
        "MicroF1Score": NotRequired[float],
        "HammingLoss": NotRequired[float],
    },
)
DocumentReaderConfigTypeDef = TypedDict(
    "DocumentReaderConfigTypeDef",
    {
        "DocumentReadAction": DocumentReadActionType,
        "DocumentReadMode": NotRequired[DocumentReadModeType],
        "FeatureTypes": NotRequired[Sequence[DocumentReadFeatureTypesType]],
    },
)
DocumentClassTypeDef = TypedDict(
    "DocumentClassTypeDef",
    {
        "Name": NotRequired[str],
        "Score": NotRequired[float],
        "Page": NotRequired[int],
    },
)
DocumentLabelTypeDef = TypedDict(
    "DocumentLabelTypeDef",
    {
        "Name": NotRequired[str],
        "Score": NotRequired[float],
        "Page": NotRequired[int],
    },
)
DocumentTypeListItemTypeDef = TypedDict(
    "DocumentTypeListItemTypeDef",
    {
        "Page": NotRequired[int],
        "Type": NotRequired[DocumentTypeType],
    },
)
ErrorsListItemTypeDef = TypedDict(
    "ErrorsListItemTypeDef",
    {
        "Page": NotRequired[int],
        "ErrorCode": NotRequired[PageBasedErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)
WarningsListItemTypeDef = TypedDict(
    "WarningsListItemTypeDef",
    {
        "Page": NotRequired[int],
        "WarnCode": NotRequired[PageBasedWarningCodeType],
        "WarnMessage": NotRequired[str],
    },
)
ContainsPiiEntitiesRequestRequestTypeDef = TypedDict(
    "ContainsPiiEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
EntityLabelTypeDef = TypedDict(
    "EntityLabelTypeDef",
    {
        "Name": NotRequired[PiiEntityTypeType],
        "Score": NotRequired[float],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
DocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "DocumentClassifierOutputDataConfigTypeDef",
    {
        "S3Uri": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "FlywheelStatsS3Prefix": NotRequired[str],
    },
)
VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": Sequence[str],
        "Subnets": Sequence[str],
    },
)
DatasetAugmentedManifestsListItemTypeDef = TypedDict(
    "DatasetAugmentedManifestsListItemTypeDef",
    {
        "AttributeNames": Sequence[str],
        "S3Uri": str,
        "AnnotationDataS3Uri": NotRequired[str],
        "SourceDocumentsS3Uri": NotRequired[str],
        "DocumentType": NotRequired[AugmentedManifestsDocumentTypeFormatType],
    },
)
DatasetDocumentClassifierInputDataConfigTypeDef = TypedDict(
    "DatasetDocumentClassifierInputDataConfigTypeDef",
    {
        "S3Uri": str,
        "LabelDelimiter": NotRequired[str],
    },
)
DatasetEntityRecognizerAnnotationsTypeDef = TypedDict(
    "DatasetEntityRecognizerAnnotationsTypeDef",
    {
        "S3Uri": str,
    },
)
DatasetEntityRecognizerDocumentsTypeDef = TypedDict(
    "DatasetEntityRecognizerDocumentsTypeDef",
    {
        "S3Uri": str,
        "InputFormat": NotRequired[InputFormatType],
    },
)
DatasetEntityRecognizerEntityListTypeDef = TypedDict(
    "DatasetEntityRecognizerEntityListTypeDef",
    {
        "S3Uri": str,
    },
)
TimestampTypeDef = Union[datetime, str]
DatasetPropertiesTypeDef = TypedDict(
    "DatasetPropertiesTypeDef",
    {
        "DatasetArn": NotRequired[str],
        "DatasetName": NotRequired[str],
        "DatasetType": NotRequired[DatasetTypeType],
        "DatasetS3Uri": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[DatasetStatusType],
        "Message": NotRequired[str],
        "NumberOfDocuments": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)
DeleteDocumentClassifierRequestRequestTypeDef = TypedDict(
    "DeleteDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)
DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
DeleteEntityRecognizerRequestRequestTypeDef = TypedDict(
    "DeleteEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)
DeleteFlywheelRequestRequestTypeDef = TypedDict(
    "DeleteFlywheelRequestRequestTypeDef",
    {
        "FlywheelArn": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "PolicyRevisionId": NotRequired[str],
    },
)
DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)
DescribeDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeDocumentClassificationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeDocumentClassifierRequestRequestTypeDef = TypedDict(
    "DescribeDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)
DescribeDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeEndpointRequestRequestTypeDef = TypedDict(
    "DescribeEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
EndpointPropertiesTypeDef = TypedDict(
    "EndpointPropertiesTypeDef",
    {
        "EndpointArn": NotRequired[str],
        "Status": NotRequired[EndpointStatusType],
        "Message": NotRequired[str],
        "ModelArn": NotRequired[str],
        "DesiredModelArn": NotRequired[str],
        "DesiredInferenceUnits": NotRequired[int],
        "CurrentInferenceUnits": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "DataAccessRoleArn": NotRequired[str],
        "DesiredDataAccessRoleArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
    },
)
DescribeEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeEntityRecognizerRequestRequestTypeDef = TypedDict(
    "DescribeEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)
DescribeEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeEventsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeFlywheelIterationRequestRequestTypeDef = TypedDict(
    "DescribeFlywheelIterationRequestRequestTypeDef",
    {
        "FlywheelArn": str,
        "FlywheelIterationId": str,
    },
)
DescribeFlywheelRequestRequestTypeDef = TypedDict(
    "DescribeFlywheelRequestRequestTypeDef",
    {
        "FlywheelArn": str,
    },
)
DescribeKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribePiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
DescribeSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DescribeTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeTopicsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
DetectDominantLanguageRequestRequestTypeDef = TypedDict(
    "DetectDominantLanguageRequestRequestTypeDef",
    {
        "Text": str,
    },
)
DetectKeyPhrasesRequestRequestTypeDef = TypedDict(
    "DetectKeyPhrasesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
DetectPiiEntitiesRequestRequestTypeDef = TypedDict(
    "DetectPiiEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {
        "Score": NotRequired[float],
        "Type": NotRequired[PiiEntityTypeType],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
DetectSentimentRequestRequestTypeDef = TypedDict(
    "DetectSentimentRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
DetectSyntaxRequestRequestTypeDef = TypedDict(
    "DetectSyntaxRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": SyntaxLanguageCodeType,
    },
)
DetectTargetedSentimentRequestRequestTypeDef = TypedDict(
    "DetectTargetedSentimentRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
TextSegmentTypeDef = TypedDict(
    "TextSegmentTypeDef",
    {
        "Text": str,
    },
)
DocumentClassificationConfigTypeDef = TypedDict(
    "DocumentClassificationConfigTypeDef",
    {
        "Mode": DocumentClassifierModeType,
        "Labels": NotRequired[Sequence[str]],
    },
)
OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
    },
)
VpcConfigPaginatorTypeDef = TypedDict(
    "VpcConfigPaginatorTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)
DocumentClassifierDocumentsTypeDef = TypedDict(
    "DocumentClassifierDocumentsTypeDef",
    {
        "S3Uri": str,
        "TestS3Uri": NotRequired[str],
    },
)
DocumentReaderConfigPaginatorTypeDef = TypedDict(
    "DocumentReaderConfigPaginatorTypeDef",
    {
        "DocumentReadAction": DocumentReadActionType,
        "DocumentReadMode": NotRequired[DocumentReadModeType],
        "FeatureTypes": NotRequired[List[DocumentReadFeatureTypesType]],
    },
)
DocumentClassifierSummaryTypeDef = TypedDict(
    "DocumentClassifierSummaryTypeDef",
    {
        "DocumentClassifierName": NotRequired[str],
        "NumberOfVersions": NotRequired[int],
        "LatestVersionCreatedAt": NotRequired[datetime],
        "LatestVersionName": NotRequired[str],
        "LatestVersionStatus": NotRequired[ModelStatusType],
    },
)
ExtractedCharactersListItemTypeDef = TypedDict(
    "ExtractedCharactersListItemTypeDef",
    {
        "Page": NotRequired[int],
        "Count": NotRequired[int],
    },
)
EntityTypesListItemTypeDef = TypedDict(
    "EntityTypesListItemTypeDef",
    {
        "Type": str,
    },
)
EntityRecognizerAnnotationsTypeDef = TypedDict(
    "EntityRecognizerAnnotationsTypeDef",
    {
        "S3Uri": str,
        "TestS3Uri": NotRequired[str],
    },
)
EntityRecognizerDocumentsTypeDef = TypedDict(
    "EntityRecognizerDocumentsTypeDef",
    {
        "S3Uri": str,
        "TestS3Uri": NotRequired[str],
        "InputFormat": NotRequired[InputFormatType],
    },
)
EntityRecognizerEntityListTypeDef = TypedDict(
    "EntityRecognizerEntityListTypeDef",
    {
        "S3Uri": str,
    },
)
EntityRecognizerEvaluationMetricsTypeDef = TypedDict(
    "EntityRecognizerEvaluationMetricsTypeDef",
    {
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1Score": NotRequired[float],
    },
)
EntityTypesEvaluationMetricsTypeDef = TypedDict(
    "EntityTypesEvaluationMetricsTypeDef",
    {
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1Score": NotRequired[float],
    },
)
EntityRecognizerOutputDataConfigTypeDef = TypedDict(
    "EntityRecognizerOutputDataConfigTypeDef",
    {
        "FlywheelStatsS3Prefix": NotRequired[str],
    },
)
EntityRecognizerSummaryTypeDef = TypedDict(
    "EntityRecognizerSummaryTypeDef",
    {
        "RecognizerName": NotRequired[str],
        "NumberOfVersions": NotRequired[int],
        "LatestVersionCreatedAt": NotRequired[datetime],
        "LatestVersionName": NotRequired[str],
        "LatestVersionStatus": NotRequired[ModelStatusType],
    },
)
FlywheelModelEvaluationMetricsTypeDef = TypedDict(
    "FlywheelModelEvaluationMetricsTypeDef",
    {
        "AverageF1Score": NotRequired[float],
        "AveragePrecision": NotRequired[float],
        "AverageRecall": NotRequired[float],
        "AverageAccuracy": NotRequired[float],
    },
)
FlywheelSummaryTypeDef = TypedDict(
    "FlywheelSummaryTypeDef",
    {
        "FlywheelArn": NotRequired[str],
        "ActiveModelArn": NotRequired[str],
        "DataLakeS3Uri": NotRequired[str],
        "Status": NotRequired[FlywheelStatusType],
        "ModelType": NotRequired[ModelTypeType],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LatestFlywheelIteration": NotRequired[str],
    },
)
PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": NotRequired[float],
        "Y": NotRequired[float],
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
ListDocumentClassifierSummariesRequestRequestTypeDef = TypedDict(
    "ListDocumentClassifierSummariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEntityRecognizerSummariesRequestRequestTypeDef = TypedDict(
    "ListEntityRecognizerSummariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PartOfSpeechTagTypeDef = TypedDict(
    "PartOfSpeechTagTypeDef",
    {
        "Tag": NotRequired[PartOfSpeechTagTypeType],
        "Score": NotRequired[float],
    },
)
PiiOutputDataConfigTypeDef = TypedDict(
    "PiiOutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": NotRequired[str],
    },
)
RedactionConfigTypeDef = TypedDict(
    "RedactionConfigTypeDef",
    {
        "PiiEntityTypes": NotRequired[List[PiiEntityTypeType]],
        "MaskMode": NotRequired[PiiEntitiesDetectionMaskModeType],
        "MaskCharacter": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
        "PolicyRevisionId": NotRequired[str],
    },
)
StartFlywheelIterationRequestRequestTypeDef = TypedDict(
    "StartFlywheelIterationRequestRequestTypeDef",
    {
        "FlywheelArn": str,
        "ClientRequestToken": NotRequired[str],
    },
)
StopDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "StopEventsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StopSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StopTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
StopTrainingDocumentClassifierRequestRequestTypeDef = TypedDict(
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)
StopTrainingEntityRecognizerRequestRequestTypeDef = TypedDict(
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)
ToxicContentTypeDef = TypedDict(
    "ToxicContentTypeDef",
    {
        "Name": NotRequired[ToxicContentTypeType],
        "Score": NotRequired[float],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
        "DesiredModelArn": NotRequired[str],
        "DesiredInferenceUnits": NotRequired[int],
        "DesiredDataAccessRoleArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
    },
)
BatchDetectDominantLanguageItemResultTypeDef = TypedDict(
    "BatchDetectDominantLanguageItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Languages": NotRequired[List[DominantLanguageTypeDef]],
    },
)
CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDocumentClassifierResponseTypeDef = TypedDict(
    "CreateDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "EndpointArn": str,
        "ModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEntityRecognizerResponseTypeDef = TypedDict(
    "CreateEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFlywheelResponseTypeDef = TypedDict(
    "CreateFlywheelResponseTypeDef",
    {
        "FlywheelArn": str,
        "ActiveModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "ResourcePolicy": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "PolicyRevisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectDominantLanguageResponseTypeDef = TypedDict(
    "DetectDominantLanguageResponseTypeDef",
    {
        "Languages": List[DominantLanguageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportModelResponseTypeDef = TypedDict(
    "ImportModelResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyRevisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDocumentClassificationJobResponseTypeDef = TypedDict(
    "StartDocumentClassificationJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "DocumentClassifierArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "EntityRecognizerArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartEventsDetectionJobResponseTypeDef = TypedDict(
    "StartEventsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartFlywheelIterationResponseTypeDef = TypedDict(
    "StartFlywheelIterationResponseTypeDef",
    {
        "FlywheelArn": str,
        "FlywheelIterationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartTopicsDetectionJobResponseTypeDef = TypedDict(
    "StartTopicsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopEventsDetectionJobResponseTypeDef = TypedDict(
    "StopEventsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateEndpointResponseTypeDef = TypedDict(
    "UpdateEndpointResponseTypeDef",
    {
        "DesiredModelArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectKeyPhrasesItemResultTypeDef = TypedDict(
    "BatchDetectKeyPhrasesItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "KeyPhrases": NotRequired[List[KeyPhraseTypeDef]],
    },
)
DetectKeyPhrasesResponseTypeDef = TypedDict(
    "DetectKeyPhrasesResponseTypeDef",
    {
        "KeyPhrases": List[KeyPhraseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectSentimentItemResultTypeDef = TypedDict(
    "BatchDetectSentimentItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Sentiment": NotRequired[SentimentTypeType],
        "SentimentScore": NotRequired[SentimentScoreTypeDef],
    },
)
DetectSentimentResponseTypeDef = TypedDict(
    "DetectSentimentResponseTypeDef",
    {
        "Sentiment": SentimentTypeType,
        "SentimentScore": SentimentScoreTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MentionSentimentTypeDef = TypedDict(
    "MentionSentimentTypeDef",
    {
        "Sentiment": NotRequired[SentimentTypeType],
        "SentimentScore": NotRequired[SentimentScoreTypeDef],
    },
)
BlockReferenceTypeDef = TypedDict(
    "BlockReferenceTypeDef",
    {
        "BlockId": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "ChildBlocks": NotRequired[List[ChildBlockTypeDef]],
    },
)
ClassifierMetadataTypeDef = TypedDict(
    "ClassifierMetadataTypeDef",
    {
        "NumberOfLabels": NotRequired[int],
        "NumberOfTrainedDocuments": NotRequired[int],
        "NumberOfTestDocuments": NotRequired[int],
        "EvaluationMetrics": NotRequired[ClassifierEvaluationMetricsTypeDef],
    },
)
ClassifyDocumentRequestRequestTypeDef = TypedDict(
    "ClassifyDocumentRequestRequestTypeDef",
    {
        "EndpointArn": str,
        "Text": NotRequired[str],
        "Bytes": NotRequired[BlobTypeDef],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigTypeDef],
    },
)
DetectEntitiesRequestRequestTypeDef = TypedDict(
    "DetectEntitiesRequestRequestTypeDef",
    {
        "Text": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "EndpointArn": NotRequired[str],
        "Bytes": NotRequired[BlobTypeDef],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigTypeDef],
    },
)
InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "InputFormat": NotRequired[InputFormatType],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigTypeDef],
    },
)
ContainsPiiEntitiesResponseTypeDef = TypedDict(
    "ContainsPiiEntitiesResponseTypeDef",
    {
        "Labels": List[EntityLabelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateEndpointRequestRequestTypeDef = TypedDict(
    "CreateEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "DesiredInferenceUnits": int,
        "ModelArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DataAccessRoleArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
    },
)
ImportModelRequestRequestTypeDef = TypedDict(
    "ImportModelRequestRequestTypeDef",
    {
        "SourceModelArn": str,
        "ModelName": NotRequired[str],
        "VersionName": NotRequired[str],
        "ModelKmsKeyId": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
DataSecurityConfigTypeDef = TypedDict(
    "DataSecurityConfigTypeDef",
    {
        "ModelKmsKeyId": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "DataLakeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
UpdateDataSecurityConfigTypeDef = TypedDict(
    "UpdateDataSecurityConfigTypeDef",
    {
        "ModelKmsKeyId": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
DatasetEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "DatasetEntityRecognizerInputDataConfigTypeDef",
    {
        "Documents": DatasetEntityRecognizerDocumentsTypeDef,
        "Annotations": NotRequired[DatasetEntityRecognizerAnnotationsTypeDef],
        "EntityList": NotRequired[DatasetEntityRecognizerEntityListTypeDef],
    },
)
DatasetFilterTypeDef = TypedDict(
    "DatasetFilterTypeDef",
    {
        "Status": NotRequired[DatasetStatusType],
        "DatasetType": NotRequired[DatasetTypeType],
        "CreationTimeAfter": NotRequired[TimestampTypeDef],
        "CreationTimeBefore": NotRequired[TimestampTypeDef],
    },
)
DocumentClassificationJobFilterTypeDef = TypedDict(
    "DocumentClassificationJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
DocumentClassifierFilterTypeDef = TypedDict(
    "DocumentClassifierFilterTypeDef",
    {
        "Status": NotRequired[ModelStatusType],
        "DocumentClassifierName": NotRequired[str],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
DominantLanguageDetectionJobFilterTypeDef = TypedDict(
    "DominantLanguageDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
EndpointFilterTypeDef = TypedDict(
    "EndpointFilterTypeDef",
    {
        "ModelArn": NotRequired[str],
        "Status": NotRequired[EndpointStatusType],
        "CreationTimeBefore": NotRequired[TimestampTypeDef],
        "CreationTimeAfter": NotRequired[TimestampTypeDef],
    },
)
EntitiesDetectionJobFilterTypeDef = TypedDict(
    "EntitiesDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
EntityRecognizerFilterTypeDef = TypedDict(
    "EntityRecognizerFilterTypeDef",
    {
        "Status": NotRequired[ModelStatusType],
        "RecognizerName": NotRequired[str],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
EventsDetectionJobFilterTypeDef = TypedDict(
    "EventsDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
FlywheelFilterTypeDef = TypedDict(
    "FlywheelFilterTypeDef",
    {
        "Status": NotRequired[FlywheelStatusType],
        "CreationTimeAfter": NotRequired[TimestampTypeDef],
        "CreationTimeBefore": NotRequired[TimestampTypeDef],
    },
)
FlywheelIterationFilterTypeDef = TypedDict(
    "FlywheelIterationFilterTypeDef",
    {
        "CreationTimeAfter": NotRequired[TimestampTypeDef],
        "CreationTimeBefore": NotRequired[TimestampTypeDef],
    },
)
KeyPhrasesDetectionJobFilterTypeDef = TypedDict(
    "KeyPhrasesDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
PiiEntitiesDetectionJobFilterTypeDef = TypedDict(
    "PiiEntitiesDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
SentimentDetectionJobFilterTypeDef = TypedDict(
    "SentimentDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
TargetedSentimentDetectionJobFilterTypeDef = TypedDict(
    "TargetedSentimentDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
TopicsDetectionJobFilterTypeDef = TypedDict(
    "TopicsDetectionJobFilterTypeDef",
    {
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "SubmitTimeBefore": NotRequired[TimestampTypeDef],
        "SubmitTimeAfter": NotRequired[TimestampTypeDef],
    },
)
DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetProperties": DatasetPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "DatasetPropertiesList": List[DatasetPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "EndpointProperties": EndpointPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEndpointsResponseTypeDef = TypedDict(
    "ListEndpointsResponseTypeDef",
    {
        "EndpointPropertiesList": List[EndpointPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectPiiEntitiesResponseTypeDef = TypedDict(
    "DetectPiiEntitiesResponseTypeDef",
    {
        "Entities": List[PiiEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectToxicContentRequestRequestTypeDef = TypedDict(
    "DetectToxicContentRequestRequestTypeDef",
    {
        "TextSegments": Sequence[TextSegmentTypeDef],
        "LanguageCode": LanguageCodeType,
    },
)
DocumentClassifierInputDataConfigTypeDef = TypedDict(
    "DocumentClassifierInputDataConfigTypeDef",
    {
        "DataFormat": NotRequired[DocumentClassifierDataFormatType],
        "S3Uri": NotRequired[str],
        "TestS3Uri": NotRequired[str],
        "LabelDelimiter": NotRequired[str],
        "AugmentedManifests": NotRequired[Sequence[AugmentedManifestsListItemTypeDef]],
        "DocumentType": NotRequired[DocumentClassifierDocumentTypeFormatType],
        "Documents": NotRequired[DocumentClassifierDocumentsTypeDef],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigTypeDef],
    },
)
DocumentClassifierInputDataConfigPaginatorTypeDef = TypedDict(
    "DocumentClassifierInputDataConfigPaginatorTypeDef",
    {
        "DataFormat": NotRequired[DocumentClassifierDataFormatType],
        "S3Uri": NotRequired[str],
        "TestS3Uri": NotRequired[str],
        "LabelDelimiter": NotRequired[str],
        "AugmentedManifests": NotRequired[List[AugmentedManifestsListItemPaginatorTypeDef]],
        "DocumentType": NotRequired[DocumentClassifierDocumentTypeFormatType],
        "Documents": NotRequired[DocumentClassifierDocumentsTypeDef],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigPaginatorTypeDef],
    },
)
InputDataConfigPaginatorTypeDef = TypedDict(
    "InputDataConfigPaginatorTypeDef",
    {
        "S3Uri": str,
        "InputFormat": NotRequired[InputFormatType],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigPaginatorTypeDef],
    },
)
ListDocumentClassifierSummariesResponseTypeDef = TypedDict(
    "ListDocumentClassifierSummariesResponseTypeDef",
    {
        "DocumentClassifierSummariesList": List[DocumentClassifierSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Pages": NotRequired[int],
        "ExtractedCharacters": NotRequired[List[ExtractedCharactersListItemTypeDef]],
    },
)
EntityRecognitionConfigTypeDef = TypedDict(
    "EntityRecognitionConfigTypeDef",
    {
        "EntityTypes": Sequence[EntityTypesListItemTypeDef],
    },
)
EntityRecognizerInputDataConfigPaginatorTypeDef = TypedDict(
    "EntityRecognizerInputDataConfigPaginatorTypeDef",
    {
        "EntityTypes": List[EntityTypesListItemTypeDef],
        "DataFormat": NotRequired[EntityRecognizerDataFormatType],
        "Documents": NotRequired[EntityRecognizerDocumentsTypeDef],
        "Annotations": NotRequired[EntityRecognizerAnnotationsTypeDef],
        "EntityList": NotRequired[EntityRecognizerEntityListTypeDef],
        "AugmentedManifests": NotRequired[List[AugmentedManifestsListItemPaginatorTypeDef]],
    },
)
EntityRecognizerInputDataConfigTypeDef = TypedDict(
    "EntityRecognizerInputDataConfigTypeDef",
    {
        "EntityTypes": Sequence[EntityTypesListItemTypeDef],
        "DataFormat": NotRequired[EntityRecognizerDataFormatType],
        "Documents": NotRequired[EntityRecognizerDocumentsTypeDef],
        "Annotations": NotRequired[EntityRecognizerAnnotationsTypeDef],
        "EntityList": NotRequired[EntityRecognizerEntityListTypeDef],
        "AugmentedManifests": NotRequired[Sequence[AugmentedManifestsListItemTypeDef]],
    },
)
EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": NotRequired[str],
        "EvaluationMetrics": NotRequired[EntityTypesEvaluationMetricsTypeDef],
        "NumberOfTrainMentions": NotRequired[int],
    },
)
ListEntityRecognizerSummariesResponseTypeDef = TypedDict(
    "ListEntityRecognizerSummariesResponseTypeDef",
    {
        "EntityRecognizerSummariesList": List[EntityRecognizerSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FlywheelIterationPropertiesTypeDef = TypedDict(
    "FlywheelIterationPropertiesTypeDef",
    {
        "FlywheelArn": NotRequired[str],
        "FlywheelIterationId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Status": NotRequired[FlywheelIterationStatusType],
        "Message": NotRequired[str],
        "EvaluatedModelArn": NotRequired[str],
        "EvaluatedModelMetrics": NotRequired[FlywheelModelEvaluationMetricsTypeDef],
        "TrainedModelArn": NotRequired[str],
        "TrainedModelMetrics": NotRequired[FlywheelModelEvaluationMetricsTypeDef],
        "EvaluationManifestS3Prefix": NotRequired[str],
    },
)
ListFlywheelsResponseTypeDef = TypedDict(
    "ListFlywheelsResponseTypeDef",
    {
        "FlywheelSummaryList": List[FlywheelSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "BoundingBox": NotRequired[BoundingBoxTypeDef],
        "Polygon": NotRequired[List[PointTypeDef]],
    },
)
SyntaxTokenTypeDef = TypedDict(
    "SyntaxTokenTypeDef",
    {
        "TokenId": NotRequired[int],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "PartOfSpeech": NotRequired[PartOfSpeechTagTypeDef],
    },
)
ToxicLabelsTypeDef = TypedDict(
    "ToxicLabelsTypeDef",
    {
        "Labels": NotRequired[List[ToxicContentTypeDef]],
        "Toxicity": NotRequired[float],
    },
)
BatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "BatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List[BatchDetectDominantLanguageItemResultTypeDef],
        "ErrorList": List[BatchItemErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "BatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List[BatchDetectKeyPhrasesItemResultTypeDef],
        "ErrorList": List[BatchItemErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectSentimentResponseTypeDef = TypedDict(
    "BatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List[BatchDetectSentimentItemResultTypeDef],
        "ErrorList": List[BatchItemErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetedSentimentMentionTypeDef = TypedDict(
    "TargetedSentimentMentionTypeDef",
    {
        "Score": NotRequired[float],
        "GroupScore": NotRequired[float],
        "Text": NotRequired[str],
        "Type": NotRequired[TargetedSentimentEntityTypeType],
        "MentionSentiment": NotRequired[MentionSentimentTypeDef],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Score": NotRequired[float],
        "Type": NotRequired[EntityTypeType],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "BlockReferences": NotRequired[List[BlockReferenceTypeDef]],
    },
)
DocumentClassificationJobPropertiesTypeDef = TypedDict(
    "DocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "DocumentClassifierArn": NotRequired[str],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "FlywheelArn": NotRequired[str],
    },
)
DominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "DominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
EntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "EntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "EntityRecognizerArn": NotRequired[str],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "FlywheelArn": NotRequired[str],
    },
)
EventsDetectionJobPropertiesTypeDef = TypedDict(
    "EventsDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "TargetEventTypes": NotRequired[List[str]],
    },
)
KeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
PiiEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[PiiOutputDataConfigTypeDef],
        "RedactionConfig": NotRequired[RedactionConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "Mode": NotRequired[PiiEntitiesDetectionModeType],
    },
)
SentimentDetectionJobPropertiesTypeDef = TypedDict(
    "SentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
StartDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "StartDocumentClassificationJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "JobName": NotRequired[str],
        "DocumentClassifierArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FlywheelArn": NotRequired[str],
    },
)
StartDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StartEntitiesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "EntityRecognizerArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FlywheelArn": NotRequired[str],
    },
)
StartEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "StartEventsDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "TargetEventTypes": Sequence[str],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "Mode": PiiEntitiesDetectionModeType,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "RedactionConfig": NotRequired[RedactionConfigTypeDef],
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StartSentimentDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StartTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "JobName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
StartTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "StartTopicsDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": InputDataConfigTypeDef,
        "OutputDataConfig": OutputDataConfigTypeDef,
        "DataAccessRoleArn": str,
        "JobName": NotRequired[str],
        "NumberOfTopics": NotRequired[int],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
TargetedSentimentDetectionJobPropertiesTypeDef = TypedDict(
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
TopicsDetectionJobPropertiesTypeDef = TypedDict(
    "TopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "NumberOfTopics": NotRequired[int],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
    },
)
UpdateFlywheelRequestRequestTypeDef = TypedDict(
    "UpdateFlywheelRequestRequestTypeDef",
    {
        "FlywheelArn": str,
        "ActiveModelArn": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "DataSecurityConfig": NotRequired[UpdateDataSecurityConfigTypeDef],
    },
)
DatasetInputDataConfigTypeDef = TypedDict(
    "DatasetInputDataConfigTypeDef",
    {
        "AugmentedManifests": NotRequired[Sequence[DatasetAugmentedManifestsListItemTypeDef]],
        "DataFormat": NotRequired[DatasetDataFormatType],
        "DocumentClassifierInputDataConfig": NotRequired[
            DatasetDocumentClassifierInputDataConfigTypeDef
        ],
        "EntityRecognizerInputDataConfig": NotRequired[
            DatasetEntityRecognizerInputDataConfigTypeDef
        ],
    },
)
ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "FlywheelArn": NotRequired[str],
        "Filter": NotRequired[DatasetFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDocumentClassificationJobsRequestListDocumentClassificationJobsPaginateTypeDef = TypedDict(
    "ListDocumentClassificationJobsRequestListDocumentClassificationJobsPaginateTypeDef",
    {
        "Filter": NotRequired[DocumentClassificationJobFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDocumentClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[DocumentClassificationJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDocumentClassifiersRequestListDocumentClassifiersPaginateTypeDef = TypedDict(
    "ListDocumentClassifiersRequestListDocumentClassifiersPaginateTypeDef",
    {
        "Filter": NotRequired[DocumentClassifierFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListDocumentClassifiersRequestRequestTypeDef = TypedDict(
    "ListDocumentClassifiersRequestRequestTypeDef",
    {
        "Filter": NotRequired[DocumentClassifierFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListDominantLanguageDetectionJobsRequestListDominantLanguageDetectionJobsPaginateTypeDef = (
    TypedDict(
        "ListDominantLanguageDetectionJobsRequestListDominantLanguageDetectionJobsPaginateTypeDef",
        {
            "Filter": NotRequired[DominantLanguageDetectionJobFilterTypeDef],
            "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
        },
    )
)
ListDominantLanguageDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[DominantLanguageDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEndpointsRequestListEndpointsPaginateTypeDef = TypedDict(
    "ListEndpointsRequestListEndpointsPaginateTypeDef",
    {
        "Filter": NotRequired[EndpointFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "Filter": NotRequired[EndpointFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEntitiesDetectionJobsRequestListEntitiesDetectionJobsPaginateTypeDef = TypedDict(
    "ListEntitiesDetectionJobsRequestListEntitiesDetectionJobsPaginateTypeDef",
    {
        "Filter": NotRequired[EntitiesDetectionJobFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEntitiesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[EntitiesDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEntityRecognizersRequestListEntityRecognizersPaginateTypeDef = TypedDict(
    "ListEntityRecognizersRequestListEntityRecognizersPaginateTypeDef",
    {
        "Filter": NotRequired[EntityRecognizerFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEntityRecognizersRequestRequestTypeDef = TypedDict(
    "ListEntityRecognizersRequestRequestTypeDef",
    {
        "Filter": NotRequired[EntityRecognizerFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListEventsDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListEventsDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[EventsDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFlywheelsRequestRequestTypeDef = TypedDict(
    "ListFlywheelsRequestRequestTypeDef",
    {
        "Filter": NotRequired[FlywheelFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListFlywheelIterationHistoryRequestRequestTypeDef = TypedDict(
    "ListFlywheelIterationHistoryRequestRequestTypeDef",
    {
        "FlywheelArn": str,
        "Filter": NotRequired[FlywheelIterationFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListKeyPhrasesDetectionJobsRequestListKeyPhrasesDetectionJobsPaginateTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsRequestListKeyPhrasesDetectionJobsPaginateTypeDef",
    {
        "Filter": NotRequired[KeyPhrasesDetectionJobFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListKeyPhrasesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[KeyPhrasesDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListPiiEntitiesDetectionJobsRequestListPiiEntitiesDetectionJobsPaginateTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsRequestListPiiEntitiesDetectionJobsPaginateTypeDef",
    {
        "Filter": NotRequired[PiiEntitiesDetectionJobFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPiiEntitiesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[PiiEntitiesDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListSentimentDetectionJobsRequestListSentimentDetectionJobsPaginateTypeDef = TypedDict(
    "ListSentimentDetectionJobsRequestListSentimentDetectionJobsPaginateTypeDef",
    {
        "Filter": NotRequired[SentimentDetectionJobFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSentimentDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListSentimentDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[SentimentDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTargetedSentimentDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListTargetedSentimentDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[TargetedSentimentDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListTopicsDetectionJobsRequestListTopicsDetectionJobsPaginateTypeDef = TypedDict(
    "ListTopicsDetectionJobsRequestListTopicsDetectionJobsPaginateTypeDef",
    {
        "Filter": NotRequired[TopicsDetectionJobFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTopicsDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    {
        "Filter": NotRequired[TopicsDetectionJobFilterTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
CreateDocumentClassifierRequestRequestTypeDef = TypedDict(
    "CreateDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": DocumentClassifierInputDataConfigTypeDef,
        "LanguageCode": LanguageCodeType,
        "VersionName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "OutputDataConfig": NotRequired[DocumentClassifierOutputDataConfigTypeDef],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Mode": NotRequired[DocumentClassifierModeType],
        "ModelKmsKeyId": NotRequired[str],
        "ModelPolicy": NotRequired[str],
    },
)
DocumentClassifierPropertiesTypeDef = TypedDict(
    "DocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "Status": NotRequired[ModelStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[DocumentClassifierInputDataConfigTypeDef],
        "OutputDataConfig": NotRequired[DocumentClassifierOutputDataConfigTypeDef],
        "ClassifierMetadata": NotRequired[ClassifierMetadataTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "Mode": NotRequired[DocumentClassifierModeType],
        "ModelKmsKeyId": NotRequired[str],
        "VersionName": NotRequired[str],
        "SourceModelArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
    },
)
DocumentClassifierPropertiesPaginatorTypeDef = TypedDict(
    "DocumentClassifierPropertiesPaginatorTypeDef",
    {
        "DocumentClassifierArn": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "Status": NotRequired[ModelStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[DocumentClassifierInputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[DocumentClassifierOutputDataConfigTypeDef],
        "ClassifierMetadata": NotRequired[ClassifierMetadataTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
        "Mode": NotRequired[DocumentClassifierModeType],
        "ModelKmsKeyId": NotRequired[str],
        "VersionName": NotRequired[str],
        "SourceModelArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
    },
)
DocumentClassificationJobPropertiesPaginatorTypeDef = TypedDict(
    "DocumentClassificationJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "DocumentClassifierArn": NotRequired[str],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
        "FlywheelArn": NotRequired[str],
    },
)
DominantLanguageDetectionJobPropertiesPaginatorTypeDef = TypedDict(
    "DominantLanguageDetectionJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
EntitiesDetectionJobPropertiesPaginatorTypeDef = TypedDict(
    "EntitiesDetectionJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "EntityRecognizerArn": NotRequired[str],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
        "FlywheelArn": NotRequired[str],
    },
)
KeyPhrasesDetectionJobPropertiesPaginatorTypeDef = TypedDict(
    "KeyPhrasesDetectionJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
PiiEntitiesDetectionJobPropertiesPaginatorTypeDef = TypedDict(
    "PiiEntitiesDetectionJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[PiiOutputDataConfigTypeDef],
        "RedactionConfig": NotRequired[RedactionConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "Mode": NotRequired[PiiEntitiesDetectionModeType],
    },
)
SentimentDetectionJobPropertiesPaginatorTypeDef = TypedDict(
    "SentimentDetectionJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "LanguageCode": NotRequired[LanguageCodeType],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
TopicsDetectionJobPropertiesPaginatorTypeDef = TypedDict(
    "TopicsDetectionJobPropertiesPaginatorTypeDef",
    {
        "JobId": NotRequired[str],
        "JobArn": NotRequired[str],
        "JobName": NotRequired[str],
        "JobStatus": NotRequired[JobStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[InputDataConfigPaginatorTypeDef],
        "OutputDataConfig": NotRequired[OutputDataConfigTypeDef],
        "NumberOfTopics": NotRequired[int],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
    },
)
ClassifyDocumentResponseTypeDef = TypedDict(
    "ClassifyDocumentResponseTypeDef",
    {
        "Classes": List[DocumentClassTypeDef],
        "Labels": List[DocumentLabelTypeDef],
        "DocumentMetadata": DocumentMetadataTypeDef,
        "DocumentType": List[DocumentTypeListItemTypeDef],
        "Errors": List[ErrorsListItemTypeDef],
        "Warnings": List[WarningsListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TaskConfigTypeDef = TypedDict(
    "TaskConfigTypeDef",
    {
        "LanguageCode": LanguageCodeType,
        "DocumentClassificationConfig": NotRequired[DocumentClassificationConfigTypeDef],
        "EntityRecognitionConfig": NotRequired[EntityRecognitionConfigTypeDef],
    },
)
CreateEntityRecognizerRequestRequestTypeDef = TypedDict(
    "CreateEntityRecognizerRequestRequestTypeDef",
    {
        "RecognizerName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": EntityRecognizerInputDataConfigTypeDef,
        "LanguageCode": LanguageCodeType,
        "VersionName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "ModelKmsKeyId": NotRequired[str],
        "ModelPolicy": NotRequired[str],
    },
)
EntityRecognizerMetadataTypeDef = TypedDict(
    "EntityRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": NotRequired[int],
        "NumberOfTestDocuments": NotRequired[int],
        "EvaluationMetrics": NotRequired[EntityRecognizerEvaluationMetricsTypeDef],
        "EntityTypes": NotRequired[List[EntityRecognizerMetadataEntityTypesListItemTypeDef]],
    },
)
DescribeFlywheelIterationResponseTypeDef = TypedDict(
    "DescribeFlywheelIterationResponseTypeDef",
    {
        "FlywheelIterationProperties": FlywheelIterationPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListFlywheelIterationHistoryResponseTypeDef = TypedDict(
    "ListFlywheelIterationHistoryResponseTypeDef",
    {
        "FlywheelIterationPropertiesList": List[FlywheelIterationPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "Id": NotRequired[str],
        "BlockType": NotRequired[BlockTypeType],
        "Text": NotRequired[str],
        "Page": NotRequired[int],
        "Geometry": NotRequired[GeometryTypeDef],
        "Relationships": NotRequired[List[RelationshipsListItemTypeDef]],
    },
)
BatchDetectSyntaxItemResultTypeDef = TypedDict(
    "BatchDetectSyntaxItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "SyntaxTokens": NotRequired[List[SyntaxTokenTypeDef]],
    },
)
DetectSyntaxResponseTypeDef = TypedDict(
    "DetectSyntaxResponseTypeDef",
    {
        "SyntaxTokens": List[SyntaxTokenTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectToxicContentResponseTypeDef = TypedDict(
    "DetectToxicContentResponseTypeDef",
    {
        "ResultList": List[ToxicLabelsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TargetedSentimentEntityTypeDef = TypedDict(
    "TargetedSentimentEntityTypeDef",
    {
        "DescriptiveMentionIndex": NotRequired[List[int]],
        "Mentions": NotRequired[List[TargetedSentimentMentionTypeDef]],
    },
)
BatchDetectEntitiesItemResultTypeDef = TypedDict(
    "BatchDetectEntitiesItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Entities": NotRequired[List[EntityTypeDef]],
    },
)
DescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "DescribeDocumentClassificationJobResponseTypeDef",
    {
        "DocumentClassificationJobProperties": DocumentClassificationJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "ListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[DocumentClassificationJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": DominantLanguageDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            DominantLanguageDetectionJobPropertiesTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": EntitiesDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[EntitiesDetectionJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEventsDetectionJobResponseTypeDef = TypedDict(
    "DescribeEventsDetectionJobResponseTypeDef",
    {
        "EventsDetectionJobProperties": EventsDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEventsDetectionJobsResponseTypeDef = TypedDict(
    "ListEventsDetectionJobsResponseTypeDef",
    {
        "EventsDetectionJobPropertiesList": List[EventsDetectionJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": KeyPhrasesDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[KeyPhrasesDetectionJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    {
        "PiiEntitiesDetectionJobProperties": PiiEntitiesDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPiiEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    {
        "PiiEntitiesDetectionJobPropertiesList": List[PiiEntitiesDetectionJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeSentimentDetectionJobResponseTypeDef",
    {
        "SentimentDetectionJobProperties": SentimentDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[SentimentDetectionJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    {
        "TargetedSentimentDetectionJobProperties": TargetedSentimentDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTargetedSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    {
        "TargetedSentimentDetectionJobPropertiesList": List[
            TargetedSentimentDetectionJobPropertiesTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "DescribeTopicsDetectionJobResponseTypeDef",
    {
        "TopicsDetectionJobProperties": TopicsDetectionJobPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "ListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[TopicsDetectionJobPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "FlywheelArn": str,
        "DatasetName": str,
        "InputDataConfig": DatasetInputDataConfigTypeDef,
        "DatasetType": NotRequired[DatasetTypeType],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
DescribeDocumentClassifierResponseTypeDef = TypedDict(
    "DescribeDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierProperties": DocumentClassifierPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDocumentClassifiersResponseTypeDef = TypedDict(
    "ListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List[DocumentClassifierPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDocumentClassifiersResponsePaginatorTypeDef = TypedDict(
    "ListDocumentClassifiersResponsePaginatorTypeDef",
    {
        "DocumentClassifierPropertiesList": List[DocumentClassifierPropertiesPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDocumentClassificationJobsResponsePaginatorTypeDef = TypedDict(
    "ListDocumentClassificationJobsResponsePaginatorTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            DocumentClassificationJobPropertiesPaginatorTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDominantLanguageDetectionJobsResponsePaginatorTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsResponsePaginatorTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            DominantLanguageDetectionJobPropertiesPaginatorTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntitiesDetectionJobsResponsePaginatorTypeDef = TypedDict(
    "ListEntitiesDetectionJobsResponsePaginatorTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List[EntitiesDetectionJobPropertiesPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListKeyPhrasesDetectionJobsResponsePaginatorTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsResponsePaginatorTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List[
            KeyPhrasesDetectionJobPropertiesPaginatorTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPiiEntitiesDetectionJobsResponsePaginatorTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsResponsePaginatorTypeDef",
    {
        "PiiEntitiesDetectionJobPropertiesList": List[
            PiiEntitiesDetectionJobPropertiesPaginatorTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSentimentDetectionJobsResponsePaginatorTypeDef = TypedDict(
    "ListSentimentDetectionJobsResponsePaginatorTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List[
            SentimentDetectionJobPropertiesPaginatorTypeDef
        ],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTopicsDetectionJobsResponsePaginatorTypeDef = TypedDict(
    "ListTopicsDetectionJobsResponsePaginatorTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List[TopicsDetectionJobPropertiesPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFlywheelRequestRequestTypeDef = TypedDict(
    "CreateFlywheelRequestRequestTypeDef",
    {
        "FlywheelName": str,
        "DataAccessRoleArn": str,
        "DataLakeS3Uri": str,
        "ActiveModelArn": NotRequired[str],
        "TaskConfig": NotRequired[TaskConfigTypeDef],
        "ModelType": NotRequired[ModelTypeType],
        "DataSecurityConfig": NotRequired[DataSecurityConfigTypeDef],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
FlywheelPropertiesTypeDef = TypedDict(
    "FlywheelPropertiesTypeDef",
    {
        "FlywheelArn": NotRequired[str],
        "ActiveModelArn": NotRequired[str],
        "DataAccessRoleArn": NotRequired[str],
        "TaskConfig": NotRequired[TaskConfigTypeDef],
        "DataLakeS3Uri": NotRequired[str],
        "DataSecurityConfig": NotRequired[DataSecurityConfigTypeDef],
        "Status": NotRequired[FlywheelStatusType],
        "ModelType": NotRequired[ModelTypeType],
        "Message": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
        "LatestFlywheelIteration": NotRequired[str],
    },
)
EntityRecognizerPropertiesPaginatorTypeDef = TypedDict(
    "EntityRecognizerPropertiesPaginatorTypeDef",
    {
        "EntityRecognizerArn": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "Status": NotRequired[ModelStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[EntityRecognizerInputDataConfigPaginatorTypeDef],
        "RecognizerMetadata": NotRequired[EntityRecognizerMetadataTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigPaginatorTypeDef],
        "ModelKmsKeyId": NotRequired[str],
        "VersionName": NotRequired[str],
        "SourceModelArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
        "OutputDataConfig": NotRequired[EntityRecognizerOutputDataConfigTypeDef],
    },
)
EntityRecognizerPropertiesTypeDef = TypedDict(
    "EntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "Status": NotRequired[ModelStatusType],
        "Message": NotRequired[str],
        "SubmitTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "TrainingStartTime": NotRequired[datetime],
        "TrainingEndTime": NotRequired[datetime],
        "InputDataConfig": NotRequired[EntityRecognizerInputDataConfigTypeDef],
        "RecognizerMetadata": NotRequired[EntityRecognizerMetadataTypeDef],
        "DataAccessRoleArn": NotRequired[str],
        "VolumeKmsKeyId": NotRequired[str],
        "VpcConfig": NotRequired[VpcConfigTypeDef],
        "ModelKmsKeyId": NotRequired[str],
        "VersionName": NotRequired[str],
        "SourceModelArn": NotRequired[str],
        "FlywheelArn": NotRequired[str],
        "OutputDataConfig": NotRequired[EntityRecognizerOutputDataConfigTypeDef],
    },
)
DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef",
    {
        "Entities": List[EntityTypeDef],
        "DocumentMetadata": DocumentMetadataTypeDef,
        "DocumentType": List[DocumentTypeListItemTypeDef],
        "Blocks": List[BlockTypeDef],
        "Errors": List[ErrorsListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectSyntaxResponseTypeDef = TypedDict(
    "BatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List[BatchDetectSyntaxItemResultTypeDef],
        "ErrorList": List[BatchItemErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectTargetedSentimentItemResultTypeDef = TypedDict(
    "BatchDetectTargetedSentimentItemResultTypeDef",
    {
        "Index": NotRequired[int],
        "Entities": NotRequired[List[TargetedSentimentEntityTypeDef]],
    },
)
DetectTargetedSentimentResponseTypeDef = TypedDict(
    "DetectTargetedSentimentResponseTypeDef",
    {
        "Entities": List[TargetedSentimentEntityTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectEntitiesResponseTypeDef = TypedDict(
    "BatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List[BatchDetectEntitiesItemResultTypeDef],
        "ErrorList": List[BatchItemErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeFlywheelResponseTypeDef = TypedDict(
    "DescribeFlywheelResponseTypeDef",
    {
        "FlywheelProperties": FlywheelPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlywheelResponseTypeDef = TypedDict(
    "UpdateFlywheelResponseTypeDef",
    {
        "FlywheelProperties": FlywheelPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntityRecognizersResponsePaginatorTypeDef = TypedDict(
    "ListEntityRecognizersResponsePaginatorTypeDef",
    {
        "EntityRecognizerPropertiesList": List[EntityRecognizerPropertiesPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeEntityRecognizerResponseTypeDef = TypedDict(
    "DescribeEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerProperties": EntityRecognizerPropertiesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntityRecognizersResponseTypeDef = TypedDict(
    "ListEntityRecognizersResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List[EntityRecognizerPropertiesTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDetectTargetedSentimentResponseTypeDef = TypedDict(
    "BatchDetectTargetedSentimentResponseTypeDef",
    {
        "ResultList": List[BatchDetectTargetedSentimentItemResultTypeDef],
        "ErrorList": List[BatchItemErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
