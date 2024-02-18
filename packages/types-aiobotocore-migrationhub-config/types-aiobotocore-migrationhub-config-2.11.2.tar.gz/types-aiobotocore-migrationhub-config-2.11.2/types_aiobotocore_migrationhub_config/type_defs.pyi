"""
Type annotations for migrationhub-config service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_migrationhub_config/type_defs/)

Usage::

    ```python
    from types_aiobotocore_migrationhub_config.type_defs import TargetTypeDef

    data: TargetTypeDef = ...
    ```
"""

import sys
from datetime import datetime
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
    "TargetTypeDef",
    "ResponseMetadataTypeDef",
    "DeleteHomeRegionControlRequestRequestTypeDef",
    "CreateHomeRegionControlRequestRequestTypeDef",
    "DescribeHomeRegionControlsRequestRequestTypeDef",
    "HomeRegionControlTypeDef",
    "GetHomeRegionResultTypeDef",
    "CreateHomeRegionControlResultTypeDef",
    "DescribeHomeRegionControlsResultTypeDef",
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Type": Literal["ACCOUNT"],
        "Id": NotRequired[str],
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
DeleteHomeRegionControlRequestRequestTypeDef = TypedDict(
    "DeleteHomeRegionControlRequestRequestTypeDef",
    {
        "ControlId": str,
    },
)
CreateHomeRegionControlRequestRequestTypeDef = TypedDict(
    "CreateHomeRegionControlRequestRequestTypeDef",
    {
        "HomeRegion": str,
        "Target": TargetTypeDef,
        "DryRun": NotRequired[bool],
    },
)
DescribeHomeRegionControlsRequestRequestTypeDef = TypedDict(
    "DescribeHomeRegionControlsRequestRequestTypeDef",
    {
        "ControlId": NotRequired[str],
        "HomeRegion": NotRequired[str],
        "Target": NotRequired[TargetTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
HomeRegionControlTypeDef = TypedDict(
    "HomeRegionControlTypeDef",
    {
        "ControlId": NotRequired[str],
        "HomeRegion": NotRequired[str],
        "Target": NotRequired[TargetTypeDef],
        "RequestedTime": NotRequired[datetime],
    },
)
GetHomeRegionResultTypeDef = TypedDict(
    "GetHomeRegionResultTypeDef",
    {
        "HomeRegion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateHomeRegionControlResultTypeDef = TypedDict(
    "CreateHomeRegionControlResultTypeDef",
    {
        "HomeRegionControl": HomeRegionControlTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeHomeRegionControlsResultTypeDef = TypedDict(
    "DescribeHomeRegionControlsResultTypeDef",
    {
        "HomeRegionControls": List[HomeRegionControlTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
