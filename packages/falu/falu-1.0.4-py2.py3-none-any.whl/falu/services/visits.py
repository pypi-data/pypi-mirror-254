from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.delete_api_request import DeleteApiRequest
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest


class Visit(PostApiRequest, GetApiRequest, PatchApiRequest, DeleteApiRequest):
    """
    A Visit represents a record that a Visitor did visit a given VisitorDestination.
    """

    @classmethod
    def get_visits(cls, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List visits

        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/visits/visits",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_visit(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Create visit

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/visits/visits",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_visit(cls, visit, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Retrieve a visit

        :param visit:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/visits/visits/{visit}",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_visit(cls, visit, document: JsonPatchDocument, api_key=None, idempotency_key: str = None, workspace=None,
                     live: bool = None):
        """
        Update a visit

        :param document:
        :param visit:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/visits/visits/{visit}",
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def start_visit(cls, visit, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Start visit

        :param visit:
        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/visits/visits/{visit}/start",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def end_visit(cls, visit, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        End visit

        :param visit:
        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/visits/visits/{visit}/end",
            data=cls.serialize(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def redact_visit(cls, visit, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Redact visit

        :param visit:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/visits/visits/{visit}/redact",
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
