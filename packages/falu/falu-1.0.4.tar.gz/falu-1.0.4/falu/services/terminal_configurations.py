from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class TerminalConfiguration(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):
    """
    A TerminalConfiguration object represents how features should be configured for terminal devices.
    """

    @classmethod
    def get_configurations(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List terminal configurations

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/terminals/configurations",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_configuration(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create a terminal configuration

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/terminals/configurations",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_configuration(cls, config, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get terminal configuration

        :param config:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/terminals/configurations/{config}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_configuration(cls, config, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                             workspace=None, live: bool = None):
        """
        Update terminal configuration

        :param document:
        :param config:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/terminals/configurations/{config}",
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_configuration(cls, config, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get terminal configuration

        :param config:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"/terminals/configurations/{config}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
