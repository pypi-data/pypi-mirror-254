from falu.generic.post_api_request import PostApiRequest


class TemporaryKey(PostApiRequest):

    @classmethod
    def create_temporary_key(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create a temporary

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/temporary_keys",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
