from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class TerminalLocation(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):
    """
    A TerminalLocation represents a grouping of devices.
    """

    @classmethod
    def get_terminal_locations(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List terminal locations

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/terminals/locations",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_terminal_location(cls, data, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        List terminal locations

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/terminals/locations",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_terminal_location(cls, terminal_location, api_key=None, idempotency_key: str = None, workspace=None,
                              live: bool = None):
        """
        Get terminal location

        :param terminal_location:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/terminals/locations/{terminal_location}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_terminal_location(cls, terminal_location, document: JsonPatchDocument, api_key=None,
                                 idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Update terminal location

        :param document:
        :param terminal_location:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/terminals/locations/{terminal_location}",
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_terminal_location(cls, terminal_location, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        Delete terminal location

        :param terminal_location:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.delete(
            path=f"/terminals/locations/{terminal_location}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
