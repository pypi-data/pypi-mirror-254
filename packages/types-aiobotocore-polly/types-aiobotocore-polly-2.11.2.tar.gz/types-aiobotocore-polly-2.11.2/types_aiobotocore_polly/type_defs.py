"""
Type annotations for polly service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_polly/type_defs/)

Usage::

    ```python
    from types_aiobotocore_polly.type_defs import DeleteLexiconInputRequestTypeDef

    data: DeleteLexiconInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence

from aiobotocore.response import StreamingBody

from .literals import (
    EngineType,
    GenderType,
    LanguageCodeType,
    OutputFormatType,
    SpeechMarkTypeType,
    TaskStatusType,
    TextTypeType,
    VoiceIdType,
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
    "DeleteLexiconInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeVoicesInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "VoiceTypeDef",
    "GetLexiconInputRequestTypeDef",
    "LexiconAttributesTypeDef",
    "LexiconTypeDef",
    "GetSpeechSynthesisTaskInputRequestTypeDef",
    "SynthesisTaskTypeDef",
    "ListLexiconsInputRequestTypeDef",
    "ListSpeechSynthesisTasksInputRequestTypeDef",
    "PutLexiconInputRequestTypeDef",
    "StartSpeechSynthesisTaskInputRequestTypeDef",
    "SynthesizeSpeechInputRequestTypeDef",
    "DescribeVoicesInputDescribeVoicesPaginateTypeDef",
    "ListLexiconsInputListLexiconsPaginateTypeDef",
    "ListSpeechSynthesisTasksInputListSpeechSynthesisTasksPaginateTypeDef",
    "SynthesizeSpeechOutputTypeDef",
    "DescribeVoicesOutputTypeDef",
    "LexiconDescriptionTypeDef",
    "GetLexiconOutputTypeDef",
    "GetSpeechSynthesisTaskOutputTypeDef",
    "ListSpeechSynthesisTasksOutputTypeDef",
    "StartSpeechSynthesisTaskOutputTypeDef",
    "ListLexiconsOutputTypeDef",
)

DeleteLexiconInputRequestTypeDef = TypedDict(
    "DeleteLexiconInputRequestTypeDef",
    {
        "Name": str,
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
DescribeVoicesInputRequestTypeDef = TypedDict(
    "DescribeVoicesInputRequestTypeDef",
    {
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "IncludeAdditionalLanguageCodes": NotRequired[bool],
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
VoiceTypeDef = TypedDict(
    "VoiceTypeDef",
    {
        "Gender": NotRequired[GenderType],
        "Id": NotRequired[VoiceIdType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LanguageName": NotRequired[str],
        "Name": NotRequired[str],
        "AdditionalLanguageCodes": NotRequired[List[LanguageCodeType]],
        "SupportedEngines": NotRequired[List[EngineType]],
    },
)
GetLexiconInputRequestTypeDef = TypedDict(
    "GetLexiconInputRequestTypeDef",
    {
        "Name": str,
    },
)
LexiconAttributesTypeDef = TypedDict(
    "LexiconAttributesTypeDef",
    {
        "Alphabet": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LastModified": NotRequired[datetime],
        "LexiconArn": NotRequired[str],
        "LexemesCount": NotRequired[int],
        "Size": NotRequired[int],
    },
)
LexiconTypeDef = TypedDict(
    "LexiconTypeDef",
    {
        "Content": NotRequired[str],
        "Name": NotRequired[str],
    },
)
GetSpeechSynthesisTaskInputRequestTypeDef = TypedDict(
    "GetSpeechSynthesisTaskInputRequestTypeDef",
    {
        "TaskId": str,
    },
)
SynthesisTaskTypeDef = TypedDict(
    "SynthesisTaskTypeDef",
    {
        "Engine": NotRequired[EngineType],
        "TaskId": NotRequired[str],
        "TaskStatus": NotRequired[TaskStatusType],
        "TaskStatusReason": NotRequired[str],
        "OutputUri": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "RequestCharacters": NotRequired[int],
        "SnsTopicArn": NotRequired[str],
        "LexiconNames": NotRequired[List[str]],
        "OutputFormat": NotRequired[OutputFormatType],
        "SampleRate": NotRequired[str],
        "SpeechMarkTypes": NotRequired[List[SpeechMarkTypeType]],
        "TextType": NotRequired[TextTypeType],
        "VoiceId": NotRequired[VoiceIdType],
        "LanguageCode": NotRequired[LanguageCodeType],
    },
)
ListLexiconsInputRequestTypeDef = TypedDict(
    "ListLexiconsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListSpeechSynthesisTasksInputRequestTypeDef = TypedDict(
    "ListSpeechSynthesisTasksInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Status": NotRequired[TaskStatusType],
    },
)
PutLexiconInputRequestTypeDef = TypedDict(
    "PutLexiconInputRequestTypeDef",
    {
        "Name": str,
        "Content": str,
    },
)
StartSpeechSynthesisTaskInputRequestTypeDef = TypedDict(
    "StartSpeechSynthesisTaskInputRequestTypeDef",
    {
        "OutputFormat": OutputFormatType,
        "OutputS3BucketName": str,
        "Text": str,
        "VoiceId": VoiceIdType,
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LexiconNames": NotRequired[Sequence[str]],
        "OutputS3KeyPrefix": NotRequired[str],
        "SampleRate": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SpeechMarkTypes": NotRequired[Sequence[SpeechMarkTypeType]],
        "TextType": NotRequired[TextTypeType],
    },
)
SynthesizeSpeechInputRequestTypeDef = TypedDict(
    "SynthesizeSpeechInputRequestTypeDef",
    {
        "OutputFormat": OutputFormatType,
        "Text": str,
        "VoiceId": VoiceIdType,
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "LexiconNames": NotRequired[Sequence[str]],
        "SampleRate": NotRequired[str],
        "SpeechMarkTypes": NotRequired[Sequence[SpeechMarkTypeType]],
        "TextType": NotRequired[TextTypeType],
    },
)
DescribeVoicesInputDescribeVoicesPaginateTypeDef = TypedDict(
    "DescribeVoicesInputDescribeVoicesPaginateTypeDef",
    {
        "Engine": NotRequired[EngineType],
        "LanguageCode": NotRequired[LanguageCodeType],
        "IncludeAdditionalLanguageCodes": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListLexiconsInputListLexiconsPaginateTypeDef = TypedDict(
    "ListLexiconsInputListLexiconsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSpeechSynthesisTasksInputListSpeechSynthesisTasksPaginateTypeDef = TypedDict(
    "ListSpeechSynthesisTasksInputListSpeechSynthesisTasksPaginateTypeDef",
    {
        "Status": NotRequired[TaskStatusType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SynthesizeSpeechOutputTypeDef = TypedDict(
    "SynthesizeSpeechOutputTypeDef",
    {
        "AudioStream": StreamingBody,
        "ContentType": str,
        "RequestCharacters": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeVoicesOutputTypeDef = TypedDict(
    "DescribeVoicesOutputTypeDef",
    {
        "Voices": List[VoiceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LexiconDescriptionTypeDef = TypedDict(
    "LexiconDescriptionTypeDef",
    {
        "Name": NotRequired[str],
        "Attributes": NotRequired[LexiconAttributesTypeDef],
    },
)
GetLexiconOutputTypeDef = TypedDict(
    "GetLexiconOutputTypeDef",
    {
        "Lexicon": LexiconTypeDef,
        "LexiconAttributes": LexiconAttributesTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSpeechSynthesisTaskOutputTypeDef = TypedDict(
    "GetSpeechSynthesisTaskOutputTypeDef",
    {
        "SynthesisTask": SynthesisTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSpeechSynthesisTasksOutputTypeDef = TypedDict(
    "ListSpeechSynthesisTasksOutputTypeDef",
    {
        "NextToken": str,
        "SynthesisTasks": List[SynthesisTaskTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSpeechSynthesisTaskOutputTypeDef = TypedDict(
    "StartSpeechSynthesisTaskOutputTypeDef",
    {
        "SynthesisTask": SynthesisTaskTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListLexiconsOutputTypeDef = TypedDict(
    "ListLexiconsOutputTypeDef",
    {
        "Lexicons": List[LexiconDescriptionTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
