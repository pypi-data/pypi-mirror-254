from falu.generic.post_api_request import PostApiRequest
from falu.generic.get_api_request import GetApiRequest


class Money(PostApiRequest, GetApiRequest):

    @classmethod
    def get_money_balance(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve balances for money services

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.get(path="/money_balances", api_key=api_key, idempotency_key=idempotency_key,
                       workspace=workspace, live=live)

    @classmethod
    def force_balance_refresh(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
          Balance request will be made upstream if the current balance is older than 5 min.

          :param api_key:
          :param idempotency_key:
          :param workspace:
          :param live:
          :return:
          """
        return cls.create(path="/money_balances/refresh", api_key=api_key, idempotency_key=idempotency_key,
                          workspace=workspace, live=live)
