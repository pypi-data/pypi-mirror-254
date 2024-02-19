from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest
from falu.list_options import BasicListOptions


class WebhookEndpoint(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):
    """
    You can configure webhook endpoints via the API to be notified about events that happen in your Falu workspace.
    Most users configure webhooks from the dashboard, which provides a user interface to registering and testing your webhook endpoints.
    """

    @classmethod
    def get_webhook_endpoints(cls, options: BasicListOptions = None, api_key=None, idempotency_key: str = None,
                              workspace=None,
                              live: bool = None):
        """
        List webhook endpoints

        :param options:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/webhooks/endpoint",
            options=options,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_webhook_endpoint(cls, data, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        Create webhook endpoint

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/webhooks/endpoint",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_webhook_endpoint(cls, webhook_endpoint, api_key=None, idempotency_key: str = None, workspace=None,
                             live: bool = None):
        """
        Get webhook endpoint

        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_webhook(cls, webhook_endpoint, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                       workspace=None, live: bool = None):
        """
        Update webhook endpoint

        :param document:
        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_webhook_endpoint(cls, webhook_endpoint, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        Get webhook endpoint

        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def roll_webhook_endpoint(cls, webhook_endpoint, data, api_key=None, idempotency_key: str = None, workspace=None,
                     live: bool = None):
        """
        Roll a webhook endpoint secret

        :param data:
        :param webhook_endpoint:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/webhooks/endpoint/{webhook_endpoint}".format(webhook_endpoint=webhook_endpoint),
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
