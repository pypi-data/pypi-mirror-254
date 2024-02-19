from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest
from falu.list_options import MessageListOptions


class Messages(PostApiRequest, GetApiRequest, PatchApiRequest):

    @classmethod
    def get_messages(cls, options: MessageListOptions = None, api_key=None, idempotency_key: str = None, workspace=None,
                     live: bool = None):
        """
        List messages

        :param options:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/messages",
            options=options,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def send_message(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create a message

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/messages",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message(cls, message_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve message

        :param message_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/messages/{message_id}".format(message_id=message_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_message(cls, message_id, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                       workspace=None, live: bool = None):
        """
        Update message

        :param document:
        :param message_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path="/messages/{message_id}".format(message_id=message_id),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def cancel_message(cls, message_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Cancel a message. A message can be cancelled when it is in accepted status.

        :param message_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/messages/{message_id}/cancel".format(message_id=message_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
