def deserialize_falu_response(code, headers, response):
    """
    If we get a server a json response from Falu's server, the response needs to be converted to a Falu Class object.
    :param headers:
    :param code:
    :param response: json response from the server.
    :return: FaluModel
    """

    if isinstance(response, list):
        return [deserialize_falu_response(code, headers, r) for r in response]
    elif isinstance(response, dict):
        model = FaluModel
        resource = model.create_object(code, headers, response)
        return resource


class FaluModel(object):
    def __init__(self, code=None, headers=None, resource=None):
        super(FaluModel, self).__init__()
        self.code = code
        self.headers = headers
        self.resource = resource

    @classmethod
    def create_object(cls, code=None, headers=None, resource=None):
        instance = cls(
            code,
            headers,
            resource
        )
        instance._create_from(resource)
        return instance

    def _create_from(self, resource):
        for k, v in resource.items():
            super(FaluModel, self).__setattr__(k, v)
        return resource
