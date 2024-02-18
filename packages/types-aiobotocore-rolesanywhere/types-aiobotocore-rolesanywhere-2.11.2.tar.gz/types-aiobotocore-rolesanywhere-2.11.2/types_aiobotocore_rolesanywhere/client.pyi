"""
Type annotations for rolesanywhere service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_rolesanywhere.client import IAMRolesAnywhereClient

    session = get_session()
    async with session.create_client("rolesanywhere") as client:
        client: IAMRolesAnywhereClient
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .paginator import (
    ListCrlsPaginator,
    ListProfilesPaginator,
    ListSubjectsPaginator,
    ListTrustAnchorsPaginator,
)
from .type_defs import (
    BlobTypeDef,
    CrlDetailResponseTypeDef,
    ListCrlsResponseTypeDef,
    ListProfilesResponseTypeDef,
    ListSubjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustAnchorsResponseTypeDef,
    NotificationSettingKeyTypeDef,
    NotificationSettingTypeDef,
    ProfileDetailResponseTypeDef,
    PutNotificationSettingsResponseTypeDef,
    ResetNotificationSettingsResponseTypeDef,
    SourceTypeDef,
    SubjectDetailResponseTypeDef,
    TagTypeDef,
    TrustAnchorDetailResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IAMRolesAnywhereClient",)

class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IAMRolesAnywhereClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IAMRolesAnywhereClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#can_paginate)
        """

    async def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.close)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#close)
        """

    async def create_profile(
        self,
        *,
        name: str,
        roleArns: Sequence[str],
        durationSeconds: int = ...,
        enabled: bool = ...,
        managedPolicyArns: Sequence[str] = ...,
        requireInstanceProperties: bool = ...,
        sessionPolicy: str = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> ProfileDetailResponseTypeDef:
        """
        Creates a *profile*, a list of the roles that Roles Anywhere service is trusted
        to
        assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.create_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#create_profile)
        """

    async def create_trust_anchor(
        self,
        *,
        name: str,
        source: SourceTypeDef,
        enabled: bool = ...,
        notificationSettings: Sequence[NotificationSettingTypeDef] = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Creates a trust anchor to establish trust between IAM Roles Anywhere and your
        certificate authority
        (CA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.create_trust_anchor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#create_trust_anchor)
        """

    async def delete_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Deletes a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.delete_crl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#delete_crl)
        """

    async def delete_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Deletes a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.delete_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#delete_profile)
        """

    async def delete_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Deletes a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.delete_trust_anchor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#delete_trust_anchor)
        """

    async def disable_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Disables a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.disable_crl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#disable_crl)
        """

    async def disable_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Disables a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.disable_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#disable_profile)
        """

    async def disable_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Disables a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.disable_trust_anchor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#disable_trust_anchor)
        """

    async def enable_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Enables a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.enable_crl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#enable_crl)
        """

    async def enable_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Enables temporary credential requests for a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.enable_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#enable_profile)
        """

    async def enable_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Enables a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.enable_trust_anchor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#enable_trust_anchor)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#generate_presigned_url)
        """

    async def get_crl(self, *, crlId: str) -> CrlDetailResponseTypeDef:
        """
        Gets a certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_crl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_crl)
        """

    async def get_profile(self, *, profileId: str) -> ProfileDetailResponseTypeDef:
        """
        Gets a profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_profile)
        """

    async def get_subject(self, *, subjectId: str) -> SubjectDetailResponseTypeDef:
        """
        Gets a *subject*, which associates a certificate identity with authentication
        attempts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_subject)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_subject)
        """

    async def get_trust_anchor(self, *, trustAnchorId: str) -> TrustAnchorDetailResponseTypeDef:
        """
        Gets a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_trust_anchor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_trust_anchor)
        """

    async def import_crl(
        self,
        *,
        crlData: BlobTypeDef,
        name: str,
        trustAnchorArn: str,
        enabled: bool = ...,
        tags: Sequence[TagTypeDef] = ...,
    ) -> CrlDetailResponseTypeDef:
        """
        Imports the certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.import_crl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#import_crl)
        """

    async def list_crls(
        self, *, nextToken: str = ..., pageSize: int = ...
    ) -> ListCrlsResponseTypeDef:
        """
        Lists all certificate revocation lists (CRL) in the authenticated account and
        Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_crls)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#list_crls)
        """

    async def list_profiles(
        self, *, nextToken: str = ..., pageSize: int = ...
    ) -> ListProfilesResponseTypeDef:
        """
        Lists all profiles in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_profiles)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#list_profiles)
        """

    async def list_subjects(
        self, *, nextToken: str = ..., pageSize: int = ...
    ) -> ListSubjectsResponseTypeDef:
        """
        Lists the subjects in the authenticated account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_subjects)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#list_subjects)
        """

    async def list_tags_for_resource(
        self, *, resourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags attached to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#list_tags_for_resource)
        """

    async def list_trust_anchors(
        self, *, nextToken: str = ..., pageSize: int = ...
    ) -> ListTrustAnchorsResponseTypeDef:
        """
        Lists the trust anchors in the authenticated account and Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.list_trust_anchors)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#list_trust_anchors)
        """

    async def put_notification_settings(
        self, *, notificationSettings: Sequence[NotificationSettingTypeDef], trustAnchorId: str
    ) -> PutNotificationSettingsResponseTypeDef:
        """
        Attaches a list of *notification settings* to a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.put_notification_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#put_notification_settings)
        """

    async def reset_notification_settings(
        self,
        *,
        notificationSettingKeys: Sequence[NotificationSettingKeyTypeDef],
        trustAnchorId: str,
    ) -> ResetNotificationSettingsResponseTypeDef:
        """
        Resets the *custom notification setting* to IAM Roles Anywhere default setting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.reset_notification_settings)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#reset_notification_settings)
        """

    async def tag_resource(self, *, resourceArn: str, tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Attaches tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#tag_resource)
        """

    async def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#untag_resource)
        """

    async def update_crl(
        self, *, crlId: str, crlData: BlobTypeDef = ..., name: str = ...
    ) -> CrlDetailResponseTypeDef:
        """
        Updates the certificate revocation list (CRL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.update_crl)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#update_crl)
        """

    async def update_profile(
        self,
        *,
        profileId: str,
        durationSeconds: int = ...,
        managedPolicyArns: Sequence[str] = ...,
        name: str = ...,
        roleArns: Sequence[str] = ...,
        sessionPolicy: str = ...,
    ) -> ProfileDetailResponseTypeDef:
        """
        Updates a *profile*, a list of the roles that IAM Roles Anywhere service is
        trusted to
        assume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.update_profile)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#update_profile)
        """

    async def update_trust_anchor(
        self, *, trustAnchorId: str, name: str = ..., source: SourceTypeDef = ...
    ) -> TrustAnchorDetailResponseTypeDef:
        """
        Updates a trust anchor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.update_trust_anchor)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#update_trust_anchor)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_crls"]) -> ListCrlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_profiles"]) -> ListProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_subjects"]) -> ListSubjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trust_anchors"]
    ) -> ListTrustAnchorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client.get_paginator)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/#get_paginator)
        """

    async def __aenter__(self) -> "IAMRolesAnywhereClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rolesanywhere.html#IAMRolesAnywhere.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_rolesanywhere/client/)
        """
