from falu.client.api_client import ApiClient

class DeleteApiRequest(ApiClient):

    @classmethod
    def delete(cls, path, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None,
               params=None):
        return cls._execute(method="DELETE", path=path, key=api_key, idempotency_key=idempotency_key,
                            workspace=workspace, live=live, params=params)
