from falu.client.api_client import ApiClient


class PatchApiRequest(ApiClient):

    @classmethod
    def patch(cls, path, data=None, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None,
              params=None):
        return cls._execute(method="PATCH", path=path, data=data, key=api_key, idempotency_key=idempotency_key,
                            workspace=workspace, live=live, params=params)
