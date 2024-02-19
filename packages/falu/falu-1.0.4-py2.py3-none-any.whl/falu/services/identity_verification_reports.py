from falu.generic.get_api_request import GetApiRequest
from falu.list_options import IdentityVerificationReportsListOptions


class IdentityVerificationReport(GetApiRequest):
    """
    An IdentityVerificationReport is the result of an attempt to collect and verify data from a user.
    You can find the result of each verification check performed in the appropriate node: document, id_number, tax_number.
    Each IdentityVerificationReport contains a copy of any data collected by the user as well as reference identifiers which can be used to access collected images.
    IdentityVerificationReports are created automatically via the IdentityVerification API.
    """

    @classmethod
    def get_identity_verification_reports(cls, options: IdentityVerificationReportsListOptions = None, api_key=None,
                                          idempotency_key: str = None, workspace=None, live: bool = None):
        """
        List identity verification reports

        :param options:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/identity/verification_reports",
            options=options,
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)

    @classmethod
    def get_identity_verification_report(cls, report, api_key=None, idempotency_key: str = None, workspace=None,
                                         live: bool = None):
        """
        List identity verification reports

        :param report:
        :param api_key:
        :param idempotency_key:
        :param workspace:
        :param live:
        :return:
        """

        return cls.get(
            path="/identity/verification_reports/{report}".format(report=report),
            api_key=api_key,
            idempotency_key=idempotency_key,
            workspace=workspace,
            live=live)
