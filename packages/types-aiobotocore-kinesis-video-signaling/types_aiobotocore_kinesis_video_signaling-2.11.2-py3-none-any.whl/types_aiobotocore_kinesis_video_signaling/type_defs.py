"""
Type annotations for kinesis-video-signaling service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_signaling/type_defs/)

Usage::

    ```python
    from types_aiobotocore_kinesis_video_signaling.type_defs import GetIceServerConfigRequestRequestTypeDef

    data: GetIceServerConfigRequestRequestTypeDef = ...
    ```
"""

import sys
from typing import Dict, List

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
    "GetIceServerConfigRequestRequestTypeDef",
    "IceServerTypeDef",
    "ResponseMetadataTypeDef",
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    "GetIceServerConfigResponseTypeDef",
    "SendAlexaOfferToMasterResponseTypeDef",
)

GetIceServerConfigRequestRequestTypeDef = TypedDict(
    "GetIceServerConfigRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "ClientId": NotRequired[str],
        "Service": NotRequired[Literal["TURN"]],
        "Username": NotRequired[str],
    },
)
IceServerTypeDef = TypedDict(
    "IceServerTypeDef",
    {
        "Uris": NotRequired[List[str]],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "Ttl": NotRequired[int],
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
SendAlexaOfferToMasterRequestRequestTypeDef = TypedDict(
    "SendAlexaOfferToMasterRequestRequestTypeDef",
    {
        "ChannelARN": str,
        "SenderClientId": str,
        "MessagePayload": str,
    },
)
GetIceServerConfigResponseTypeDef = TypedDict(
    "GetIceServerConfigResponseTypeDef",
    {
        "IceServerList": List[IceServerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SendAlexaOfferToMasterResponseTypeDef = TypedDict(
    "SendAlexaOfferToMasterResponseTypeDef",
    {
        "Answer": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
