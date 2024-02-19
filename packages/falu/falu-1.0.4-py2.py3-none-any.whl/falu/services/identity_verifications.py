import json

from falu.client.json_patch_document import JsonPatchDocument
from falu.generic.get_api_request import GetApiRequest
from falu.generic.patch_api_request import PatchApiRequest
from falu.generic.post_api_request import PostApiRequest
from falu.list_options import IdentityVerificationListOptions


class IdentityVerification(PostApiRequest, GetApiRequest, PatchApiRequest):
    """
    An IdentityVerification guides you through the process of collecting and verifying the identities of your users.
    It contains details such as what verification check to perform. Only create one IdentityVerification for each verification in your system.
    An IdentityVerification transitions through multiple statuses throughout its lifetime as it progresses through the verification flow.
    The IdentityVerification contains the user’s verified data after verification checks are complete.
    """

    @classmethod
    def get_identity_verifications(cls, options: IdentityVerificationListOptions = None, api_key=None,
                                   idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List identity verifications

        :param options:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/identity/verifications",
            options=options,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def create_identity_verification(cls, data: dict, api_key=None, idempotency_key: str = None, workspace=None,
                                     live: bool = None):
        """
        Create an identity verification

        :param data:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.create(
            path="/identity/verifications",
            data=json.dumps(data),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_identity_verification(cls, verification, api_key=None, idempotency_key: str = None, workspace=None,
                                  live: bool = None):
        """
        Get an identity verification

        :param verification:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path=f"/identity/verifications/{verification}".format(verification=verification),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def update_identity_verification(cls, verification, document: JsonPatchDocument, api_key=None,
                                     idempotency_key: str = None, workspace=None, live: bool = None):
        """
        Update an identity verification

        :param document:
        :param verification:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """
        return cls.patch(
            path=f"/identity/verifications/{verification}".format(verification=verification),
            data=cls.serialize(document.operations),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def cancel_identity_verification(cls, verification, api_key=None, idempotency_key: str = None, workspace=None,
                                     live: bool = None):
        """
        Cancel an identity verification
        An identity verification can be cancelled when it is in input_required status.
        Once cancelled, future submission attempts are disabled. This cannot be undone!

        :param verification:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/identity/verifications/{verification}/cancel".format(verification=verification),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def redact_identity_verification(cls, verification, api_key=None, idempotency_key: str = None, workspace=None,
                                     live: bool = None):
        """
        Redact an identity verification
        Redact an identity verification to remove all collected information from Falu.
        This will redact the IdentityVerification and all objects related to it, including IdentityVerificationReports,
        Events, request logs, etc. An identity verification can be redacted when it is in input_required or verified status.
        Redacting an identity verification in input_required state will automatically cancel it.
        The redaction process may take up a week. When the redaction process is in progress, the IdentityVerification's redaction.status
        field will be set to processing; when the process is finished, it will change to redacted and an identity_verification.redacted event will be emitted.
        Redaction is irreversible. Redacted objects are still accessible in the API, but all the fields that contain personal data will be replaced by the string [redacted] or a similar placeholder.
        The metadata field will also be erased. Redacted objects cannot be updated or used for any purpose.

        :param verification:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.create(
            path=f"/identity/verifications/{verification}/redact".format(verification=verification),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
