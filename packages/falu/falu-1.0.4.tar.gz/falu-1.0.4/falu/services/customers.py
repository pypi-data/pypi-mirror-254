from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class Customer(PostApiRequest, GetApiRequest, DeleteApiRequest, PatchApiRequest):
    """
    This object represents a customer of your business.
    It lets you track payments, transfers, and messages that belong to the same customer.
    """

    @classmethod
    def get_customers(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List customers

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/customers",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_customer(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create customer

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/customers",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_customer(cls, customer, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get customer

        :param customer:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/customers/{customer}".format(customer=customer),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_customer(cls, customer, document: JsonPatchDocument, api_key=None, idempotency_key: str = None,
                        workspace=None, live: bool = None):
        """
        Update customer

        :param document:
        :param customer:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path="/customers/{customer}".format(customer=customer),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_customer(cls, customer, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Delete a customer. It cannot be undone.

        :param customer:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.delete(
            path="/customers/{customer}".format(customer=customer),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
