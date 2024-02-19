from falu.list_options import FileListOptions
from falu.generic.get_api_request import GetApiRequest
from falu.generic.post_api_request import PostApiRequest


class File(PostApiRequest, GetApiRequest):
    """
    This is an object representing a file hosted on Falu's servers.
    The file may have been uploaded by yourself using the create file request (for example, when uploading an identity document)
    or it may have been created by Falu (for example, a statement of accounts).
    """

    @classmethod
    def get_files(cls, options: FileListOptions = None, api_key=None, idempotency_key: str = None, workspace=None,
                  live: bool = None):
        """
        Get files

        :param options:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/files",
            options=options,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def upload_files(cls, data, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Upload files

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path="/files",
            data=data,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_file(cls, file, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Get file

        :param file:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/files/{file}".format(file=file),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def download_file(cls, file, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Download file

        :param file:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        pass

    @classmethod
    def redact_file(cls, file, api_key=None, idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Redact file content

        :param file:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/files/{file}/redact".format(file=file),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
