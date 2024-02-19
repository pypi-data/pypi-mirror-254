from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class TerminalDevice(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):
    """
    A TerminalDevice represents a physical device for performing identity verifications.
    """

    @classmethod
    def get_terminal_devices(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List terminal devices

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/terminals/devices",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_terminal_device(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create terminal device

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/terminals/devices",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_terminal_device(cls, device, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get terminal device

        :param device:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/terminals/devices/{device}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_terminal_device(cls, device, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                               workspace=None, live: bool = None):
        """
        Update terminal devices

        :param document:
        :param device:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/terminals/devices/{device}",
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_terminal_device(cls, device, api_key=None, idempotency_key: str = None, workspace=None,
                               live: bool = None):
        """
        Get terminal device

        :param device:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"/terminals/devices/{device}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def handoff_terminal_device(cls, device, data, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        Hand-off processing of a visit to a terminal device

        :param data:
        :param device:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/terminals/devices/{device}/process_visit",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
