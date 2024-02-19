from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class Payment(PostApiRequest, GetApiRequest, PatchApiRequest):
    """
    To initiate a payment from a customer, you create a Payment object.
    You can retrieve and refund individual payments as well as a list all payments.
    Payment objects can also be created if your workspace supports payment providers that allow customers to initiate the payments such as MPESA and EFT/RTGS.
    In this case, the provider may require you to authorize the payment before it is completed.
    """

    @classmethod
    def get_payments(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List payments

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/payments",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_payment(cls, payment, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve a payment

        :param payment:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/payments/{payment}".format(payment=payment),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_payment(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create a payment

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/payments",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_payment(cls, payment, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                       workspace=None, live: bool = None):
        """
        Update a payment

        :param document:
        :param payment:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/payments/{payment}".format(payment=payment),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
