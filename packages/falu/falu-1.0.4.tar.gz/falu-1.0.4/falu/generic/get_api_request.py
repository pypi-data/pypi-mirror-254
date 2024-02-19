from falu.client.api_client import ApiClient


class GetApiRequest(ApiClient):

    @classmethod
    def get(cls, path, options=None, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None,
            params=None):
        return cls._execute(method="GET", path=path, options=options, key=api_key, idempotency_key=idempotency_key,
                            workspace=workspace, live=live, params=params)
