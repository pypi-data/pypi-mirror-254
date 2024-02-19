from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class TransferReversal(PostApiRequest, GetApiRequest, PatchApiRequest):
    """
    TransferReversal object allows you to reverse a transfer that has been previously created but not yet reversed.
    Funds will be refunded your workspace.
    NOTE: Some providers have a time windows after which reversals cannot happen.
    """

    @classmethod
    def get_transfer_reversals(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List transfer reversal

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/transfer_reversal",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_transfer_reversal(cls, data, api_key=None, idempotency_key: str = None, workspace=None,
                                 live: bool = None):
        """
        Create transfer reversal

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/transfer_reversal",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def retrieve_transfer_reversal(cls, reversal, api_key=None, idempotency_key: str = None, workspace=None,
                                   live: bool = None):
        """
        Update transfer reversal

        :param reversal:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/transfer_reversal/{reversal}".format(reversal=reversal),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_transfer_reversal(cls, reversal, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                                 workspace=None, live: bool = None):
        """
        Update transfer reversal

        :param document:
        :param reversal:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path="/transfer_reversal/{reversal}".format(reversal=reversal),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
