"""
Type annotations for connect-contact-lens service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_connect_contact_lens/type_defs/)

Usage::

    ```python
    from types_aiobotocore_connect_contact_lens.type_defs import PointOfInterestTypeDef

    data: PointOfInterestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

from .literals import SentimentValueType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "PointOfInterestTypeDef",
    "CharacterOffsetsTypeDef",
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CategoryDetailsTypeDef",
    "IssueDetectedTypeDef",
    "CategoriesTypeDef",
    "TranscriptTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
)

PointOfInterestTypeDef = TypedDict(
    "PointOfInterestTypeDef",
    {
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
    },
)
CharacterOffsetsTypeDef = TypedDict(
    "CharacterOffsetsTypeDef",
    {
        "BeginOffsetChar": int,
        "EndOffsetChar": int,
    },
)
ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
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
CategoryDetailsTypeDef = TypedDict(
    "CategoryDetailsTypeDef",
    {
        "PointsOfInterest": List[PointOfInterestTypeDef],
    },
)
IssueDetectedTypeDef = TypedDict(
    "IssueDetectedTypeDef",
    {
        "CharacterOffsets": CharacterOffsetsTypeDef,
    },
)
CategoriesTypeDef = TypedDict(
    "CategoriesTypeDef",
    {
        "MatchedCategories": List[str],
        "MatchedDetails": Dict[str, CategoryDetailsTypeDef],
    },
)
TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "Id": str,
        "ParticipantId": str,
        "ParticipantRole": str,
        "Content": str,
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
        "Sentiment": SentimentValueType,
        "IssuesDetected": NotRequired[List[IssueDetectedTypeDef]],
    },
)
RealtimeContactAnalysisSegmentTypeDef = TypedDict(
    "RealtimeContactAnalysisSegmentTypeDef",
    {
        "Transcript": NotRequired[TranscriptTypeDef],
        "Categories": NotRequired[CategoriesTypeDef],
    },
)
ListRealtimeContactAnalysisSegmentsResponseTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    {
        "Segments": List[RealtimeContactAnalysisSegmentTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
