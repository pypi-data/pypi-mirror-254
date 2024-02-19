from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class PaymentAuthorization(PostApiRequest, GetApiRequest, PatchApiRequest):
    """
    When a payment provider supports customer initiated payments and a customer initiates a payment, a Payment Authorization object is created.
    Authorizations must be approved for the payment to be completed successfully.
    """

    @classmethod
    def get_payment_authorizations(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List payment authorizations

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/payments_authorizations",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_payment_authorization(cls, payment_authorization, api_key=None, idempotency_key: str = None, workspace=None,
                                  live: bool = None):
        """
        Retrieve a payment authorization

        :param payment_authorization:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/payments_authorizations/{payment_authorization}".format(
                payment_authorization=payment_authorization),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_payment_authorization(cls, payment_authorization, document: JsonPatchDocument, api_key=None,
                                     idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Update a payment authorization

        :param document:
        :param payment_authorization:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/payments_authorizations/{payment_authorization}".format(
                payment_authorization=payment_authorization),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def approve_payment_authorization(cls, payment_authorization, data=None, api_key=None, idempotency_key: str = None,
                                      workspace=None, live: bool = None):
        """
        Approve a payment authorization

        :param data:
        :param payment_authorization:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/payments_authorizations/{payment_authorization}/approve".format(
                payment_authorization=payment_authorization),
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def decline_payment_authorization(cls, payment_authorization, data=None, api_key=None, idempotency_key: str = None,
                                      workspace=None, live: bool = None):
        """
        Decline a payment authorization

        :param data:
        :param payment_authorization:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/payments_authorizations/{payment_authorization}/decline".format(
                payment_authorization=payment_authorization),
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

