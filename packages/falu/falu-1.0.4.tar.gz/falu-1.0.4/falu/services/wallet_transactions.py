from falu.generic.get_api_request import GetApiRequest


class WalletTransaction(GetApiRequest):
    """
    Wallet transactions represent funds moving through your Falu account.
    They're created for every type of transaction that comes into or flows out of your Falu workspace balance..
    """

    @classmethod
    def get_transactions(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve wallet transactions

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/wallet_transactions",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_transaction(cls, transaction, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve wallet transaction

        :param transaction:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/wallet_transactions/{transaction}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
