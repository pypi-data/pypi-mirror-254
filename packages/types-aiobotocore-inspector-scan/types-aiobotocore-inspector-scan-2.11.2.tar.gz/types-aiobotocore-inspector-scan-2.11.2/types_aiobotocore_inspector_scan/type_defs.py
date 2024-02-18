"""
Type annotations for inspector-scan service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_inspector_scan/type_defs/)

Usage::

    ```python
    from types_aiobotocore_inspector_scan.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

import sys
from typing import Any, Dict, Mapping

from .literals import OutputFormatType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = ("ResponseMetadataTypeDef", "ScanSbomRequestRequestTypeDef", "ScanSbomResponseTypeDef")

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
ScanSbomRequestRequestTypeDef = TypedDict(
    "ScanSbomRequestRequestTypeDef",
    {
        "sbom": Mapping[str, Any],
        "outputFormat": NotRequired[OutputFormatType],
    },
)
ScanSbomResponseTypeDef = TypedDict(
    "ScanSbomResponseTypeDef",
    {
        "sbom": Dict[str, Any],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
