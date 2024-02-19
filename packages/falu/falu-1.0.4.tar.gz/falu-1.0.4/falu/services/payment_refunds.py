from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class PaymentRefund(PostApiRequest, GetApiRequest, PatchApiRequest):
    """
    PaymentRefund object allows you to refund a payment that has been previously been created but not yet refunded.
    Funds will be refunded to the payment instrument that was originally charged.
    Some payment providers have a time window after which refunds cannot happen.
    In this case you can initiate a Transfer to the customer with the appropriate amount.
    """

    @classmethod
    def get_payment_refunds(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List payment refunds

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/payment_refunds",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_payment_refund(cls, data, api_key=None, idempotency_key: str = None, workspace=None,
                              live: bool = None):
        """
        Create a payment refund

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/payment_refunds",
            api_key=api_key,
            data=cls.serialize(data),
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def retrieve_payment_refund(cls, refund, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        Retrieve a payment refund

        :param refund:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/payment_refunds/{refund}".format(refund=refund),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_payment_refund(cls, refund, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                              workspace=None, live: bool = None):
        """
        Update a payment refund

        :param document:
        :param refund:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/payment_refunds/{refund}".format(refund=refund),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
