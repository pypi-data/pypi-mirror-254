"""
Type annotations for eks-auth service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_eks_auth/type_defs/)

Usage::

    ```python
    from types_aiobotocore_eks_auth.type_defs import AssumeRoleForPodIdentityRequestRequestTypeDef

    data: AssumeRoleForPodIdentityRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict

if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssumeRoleForPodIdentityRequestRequestTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "PodIdentityAssociationTypeDef",
    "ResponseMetadataTypeDef",
    "SubjectTypeDef",
    "AssumeRoleForPodIdentityResponseTypeDef",
)

AssumeRoleForPodIdentityRequestRequestTypeDef = TypedDict(
    "AssumeRoleForPodIdentityRequestRequestTypeDef",
    {
        "clusterName": str,
        "token": str,
    },
)
AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "arn": str,
        "assumeRoleId": str,
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "sessionToken": str,
        "secretAccessKey": str,
        "accessKeyId": str,
        "expiration": datetime,
    },
)
PodIdentityAssociationTypeDef = TypedDict(
    "PodIdentityAssociationTypeDef",
    {
        "associationArn": str,
        "associationId": str,
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
SubjectTypeDef = TypedDict(
    "SubjectTypeDef",
    {
        "namespace": str,
        "serviceAccount": str,
    },
)
AssumeRoleForPodIdentityResponseTypeDef = TypedDict(
    "AssumeRoleForPodIdentityResponseTypeDef",
    {
        "subject": SubjectTypeDef,
        "audience": str,
        "podIdentityAssociation": PodIdentityAssociationTypeDef,
        "assumedRoleUser": AssumedRoleUserTypeDef,
        "credentials": CredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
