"""
Type annotations for workmailmessageflow service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_workmailmessageflow/type_defs/)

Usage::

    ```python
    from types_aiobotocore_workmailmessageflow.type_defs import GetRawMessageContentRequestRequestTypeDef

    data: GetRawMessageContentRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict

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
    "GetRawMessageContentRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ReferenceTypeDef",
    "GetRawMessageContentResponseTypeDef",
    "RawMessageContentTypeDef",
    "PutRawMessageContentRequestRequestTypeDef",
)

GetRawMessageContentRequestRequestTypeDef = TypedDict(
    "GetRawMessageContentRequestRequestTypeDef",
    {
        "messageId": str,
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
S3ReferenceTypeDef = TypedDict(
    "S3ReferenceTypeDef",
    {
        "bucket": str,
        "key": str,
        "objectVersion": NotRequired[str],
    },
)
GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef",
    {
        "messageContent": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RawMessageContentTypeDef = TypedDict(
    "RawMessageContentTypeDef",
    {
        "s3Reference": S3ReferenceTypeDef,
    },
)
PutRawMessageContentRequestRequestTypeDef = TypedDict(
    "PutRawMessageContentRequestRequestTypeDef",
    {
        "messageId": str,
        "content": RawMessageContentTypeDef,
    },
)
