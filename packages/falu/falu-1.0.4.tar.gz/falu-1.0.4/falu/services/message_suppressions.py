import json

from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class MessageSuppressions(PostApiRequest, GetApiRequest, DeleteApiRequest):
    """
    A MessageSuppression object allows you to manage the phone number destinations that are not currently active for sending to.
    """

    @classmethod
    def get_message_suppressions(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List message suppression

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path="/message_suppressions",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_message_suppression(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None,
                                   live: bool = None):
        """
        Create message suppression

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/message_suppressions",
            data=json.dumps(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_message_suppression(cls, suppression, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        List message suppression

        :param suppression:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(
            path=f"/message_suppressions/{suppression}".format(suppression=suppression),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def delete_message_suppression(cls, suppression, api_key=None, idempotency_key: str = None, workspace=None,
                                live: bool = None):
        """
        List message suppression

        :param suppression:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.delete(
            path=f"/message_suppressions/{suppression}".format(suppression=suppression),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
