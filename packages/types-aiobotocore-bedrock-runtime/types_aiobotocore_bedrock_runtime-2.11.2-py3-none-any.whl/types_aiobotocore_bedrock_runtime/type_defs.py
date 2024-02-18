"""
Type annotations for bedrock-runtime service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_runtime/type_defs/)

Usage::

    ```python
    from types_aiobotocore_bedrock_runtime.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

import sys
from typing import IO, Any, Dict, Union

from aiobotocore.eventstream import AioEventStream
from aiobotocore.response import StreamingBody

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BlobTypeDef",
    "InternalServerExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "ModelStreamErrorExceptionTypeDef",
    "ModelTimeoutExceptionTypeDef",
    "PayloadPartTypeDef",
    "ThrottlingExceptionTypeDef",
    "ValidationExceptionTypeDef",
    "InvokeModelRequestRequestTypeDef",
    "InvokeModelWithResponseStreamRequestRequestTypeDef",
    "InvokeModelResponseTypeDef",
    "ResponseStreamTypeDef",
    "InvokeModelWithResponseStreamResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
InternalServerExceptionTypeDef = TypedDict(
    "InternalServerExceptionTypeDef",
    {
        "message": NotRequired[str],
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
ModelStreamErrorExceptionTypeDef = TypedDict(
    "ModelStreamErrorExceptionTypeDef",
    {
        "message": NotRequired[str],
        "originalStatusCode": NotRequired[int],
        "originalMessage": NotRequired[str],
    },
)
ModelTimeoutExceptionTypeDef = TypedDict(
    "ModelTimeoutExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "bytes": NotRequired[bytes],
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
InvokeModelRequestRequestTypeDef = TypedDict(
    "InvokeModelRequestRequestTypeDef",
    {
        "body": BlobTypeDef,
        "modelId": str,
        "contentType": NotRequired[str],
        "accept": NotRequired[str],
    },
)
InvokeModelWithResponseStreamRequestRequestTypeDef = TypedDict(
    "InvokeModelWithResponseStreamRequestRequestTypeDef",
    {
        "body": BlobTypeDef,
        "modelId": str,
        "contentType": NotRequired[str],
        "accept": NotRequired[str],
    },
)
InvokeModelResponseTypeDef = TypedDict(
    "InvokeModelResponseTypeDef",
    {
        "body": StreamingBody,
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseStreamTypeDef = TypedDict(
    "ResponseStreamTypeDef",
    {
        "chunk": NotRequired[PayloadPartTypeDef],
        "internalServerException": NotRequired[InternalServerExceptionTypeDef],
        "modelStreamErrorException": NotRequired[ModelStreamErrorExceptionTypeDef],
        "validationException": NotRequired[ValidationExceptionTypeDef],
        "throttlingException": NotRequired[ThrottlingExceptionTypeDef],
        "modelTimeoutException": NotRequired[ModelTimeoutExceptionTypeDef],
    },
)
InvokeModelWithResponseStreamResponseTypeDef = TypedDict(
    "InvokeModelWithResponseStreamResponseTypeDef",
    {
        "body": "AioEventStream[ResponseStreamTypeDef]",
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
