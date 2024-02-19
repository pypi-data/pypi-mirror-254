from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class MessageBatch(PostApiRequest, GetApiRequest, PatchApiRequest):

    @classmethod
    def send_bulk_messages(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None,
                           live: bool = None):
        """
        Create a new message batch.
        You can send up to 1,000 messages in one API request.

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_batches",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message_batches(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List message batches

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/message_batches",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message_batch(cls, batch_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve a message batch

        :param batch_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/message_batches/{batch_id}".format(batch_id=batch_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_message_batch(cls, batch_id, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                             workspace=None, live: bool = None):
        """
        Retrieve a message batch

        :param document:
        :param batch_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path="/message_batches/{batch_id}".format(batch_id=batch_id),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_status(cls, batch_id, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve the status of a message batch

        :param batch_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/message_batches/{batch_id}/status".format(batch_id=batch_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def cancel_message_batch(cls, batch_id, api_key=None, idempotency_key: str = None, workspace=None,
                             live: bool = None):
        """
        A message batch can be cancelled when all its messages are in accepted status.

        :param batch_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_batches/{batch_id}/cancel".format(batch_id=batch_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def redact_message_batch(cls, batch_id, api_key=None, idempotency_key: str = None, workspace=None,
                             live: bool = None):
        """
        Redact a message batch to remove all collected information from Falu. This will redact the Message Batch,
        its Messages and all objects related to it, including Events, request logs, etc. A message batch can be redacted
        when its message are not in sending status. Redacting a message batch when all its messages are in accepted state
        will automatically cancel it and its messages.
        The redaction process may take up a week. When the redaction process is in progress, the MessageBatch's redaction.status
        field will be set to processing; when the process is finished, it will change to redacted and a message_batch.redacted
        event will be emitted. Redaction is irreversible. Redacted objects are still accessible in the API,
        but all the fields that contain personal data will be replaced by the string [redacted] or a similar placeholder.
        The metadata field will also be erased. Redacted objects cannot be updated or used for any purpose.

        :param batch_id:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_batches/{batch_id}/redact".format(batch_id=batch_id),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
