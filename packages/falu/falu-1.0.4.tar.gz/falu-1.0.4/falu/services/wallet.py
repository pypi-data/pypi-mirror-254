from falu.generic.get_api_request import GetApiRequest


class Wallet(GetApiRequest):
    """
    This is an object representing your Falu wallet. You can retrieve it to see the balance currently on your Falu account.
    You can also retrieve the wallet history, which contains a list of transactions that contributed to the balance (requests, payments, transfers, and so forth).
    """

    @classmethod
    def get_wallet(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve wallet

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/wallet",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
