import json

from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class MessageStream(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):

    @classmethod
    def get_message_streams(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List message streams

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/message_streams",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_message_stream(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None,
                              live: bool = None):
        """
        Create message stream

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_streams",
            data=json.dumps(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message_stream(cls, stream, api_key=None, idempotency_key: str = None, workspace=None,
                           live: bool = None):
        """
        Get message stream

        :param stream:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/message_streams/{stream}".format(stream=stream),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_message_stream(cls, stream, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                              workspace=None, live: bool = None):
        """
        Update message stream

        :param document:
        :param stream:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path="/message_streams/{stream}".format(stream=stream),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_message_stream(cls, stream, api_key=None, idempotency_key: str = None, workspace=None,
                              live: bool = None):
        """
        Delete message stream

        :param stream:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        cls.delete(
            path="/message_streams/{stream}".format(stream=stream),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def archive_message_stream(cls, stream, api_key=None, idempotency_key: str = None, workspace=None,
                               live: bool = None):
        """
        Archive message stream

        :param stream:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_streams/{stream}/archive".format(stream=stream),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def unarchive_message_stream(cls, stream, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        Unarchive message stream

        :param stream:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_streams/{stream}/unarchive".format(stream=stream),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
