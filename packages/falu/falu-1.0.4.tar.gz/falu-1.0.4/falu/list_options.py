from falu.query_values import QueryValues
from falu.range_filtering_options import RangeFilteringOptions


class BasicListOptions(object):
    """
    Standard options for filtering and pagination in list operations.
    """

    def __init__(self, sorting=None, count=None, created: RangeFilteringOptions = None,
                 update: RangeFilteringOptions = None):
        self.sorting = sorting
        self.count = count
        self.created = created
        self.update = update

    def populate(self, values: QueryValues):
        if values is None: return

        values.add("sort", [self.sorting])
        values.add("count", self.count)
        values.add_query_values("created", QueryValues().fromRange(self.created))
        values.add_query_values("updated", QueryValues().fromRange(self.update))

class BasicListOptionsWithMoney(BasicListOptions):
    """
    Standard options for filtering and pagination in list operations with money.
    """

    def __init__(self, currency=None, amount: RangeFilteringOptions = None):
        super().__init__()
        self.currency = currency
        self.amount = amount

    def populate(self, values: QueryValues):
        super().populate(values)

        values.add("currency", self.currency).add_query_values("amount", QueryValues().fromRange(self.amount))


class MessageListOptions(BasicListOptions):
    """
    Options for filtering and pagination of messages.
    """

    def __init__(self, delivered: RangeFilteringOptions = None, status=None):
        super().__init__()
        self.delivered = delivered
        self.status = status

    def populate(self, values: QueryValues):
        super().populate(values)

        values \
            .add("delivered", QueryValues().fromRange(self.delivered)) \
            .add("status", self.status)


class IdentityVerificationListOptions(BasicListOptions):
    """
    Options for filtering identity verifications
    """

    def __init__(self, status=None, document_type=None, customer=None):
        super().__init__()
        self.status = status
        self.document_type = document_type
        self.customer = customer

    def populate(self, values: QueryValues):
        super().populate(values)
        values.add("status", self.status)
        values.add("type", self.document_type)
        values.add("customer", self.customer)

class IdentityVerificationReportsListOptions(BasicListOptions):
    """
    Options for filtering identity verification reports
    """

    def __init__(self, verification=None):
        super().__init__()
        self.verification = verification

    def populate(self, values: QueryValues):
        super().populate(values)
        values.add("verification", self.verification)


class FileListOptions(BasicListOptions):
    """
    Options for filtering and pagination of list files
    """

    def __init__(self, purpose=None):
        super().__init__()
        self.purpose = purpose

    def populate(self, values: QueryValues):
        super().populate(values)
        values.add("purpose", self.purpose)


class FileLinksListOptions(BasicListOptions):
    """
    Options for filtering and pagination of list file links.
    """

    def __init__(self, file=None):
        super().__init__()
        self.file = file

    def populate(self, values: QueryValues):
        super().populate(values)
        values.add("file", self.file)


class TransferListOptions(BasicListOptionsWithMoney):
    """
    Options for filtering and pagination of transfers.
    """

    def __init__(self, status=None):
        super().__init__()
        self.status = status

    def populate(self, values: QueryValues):
        super().populate(values)
        values.add("status", self.status)
