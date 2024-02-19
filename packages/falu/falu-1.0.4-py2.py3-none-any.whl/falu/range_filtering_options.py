class RangeFilteringOptions(object):
    """
     Standard options for range filtering
    """

    def __init__(self, less_than=None, less_than_or_equal_to=None, greater_than=None, greater_than_or_equal_to=None):
        self.less_than = less_than
        self.less_than_or_equal_to = less_than_or_equal_to
        self.greater_than = greater_than
        self.greater_than_or_equal_to = greater_than_or_equal_to
