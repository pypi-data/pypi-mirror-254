from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class Visitor(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):
    """
    A Visitor represents an individual who visited the premises.
    """

    @classmethod
    def get_visitors(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List visitor

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/visits/visitors",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_visitor(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create visitor

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/visits/visitors",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_visitor(cls, visitor, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get terminal device

        :param visitor:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/visits/visitors/{visitor}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_visitor(cls, visitor, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                       workspace=None, live: bool = None):
        """
        Update visitor

        :param document:
        :param visitor:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/visits/visitors/{visitor}",
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_visitor(cls, visitor, api_key=None, idempotency_key: str = None, workspace=None,
                       live: bool = None):
        """
        Delete visitor

        :param visitor:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"/visits/visitors/{visitor}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def redact_visitor(cls, visitor, api_key=None, idempotency_key: str = None, workspace=None,
                       live: bool = None):
        """
        Redact visitor

        :param visitor:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/visits/visitors/{visitor}/redact",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
