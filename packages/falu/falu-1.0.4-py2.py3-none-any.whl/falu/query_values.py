from datetime import datetime

from falu.range_filtering_options import RangeFilteringOptions


class QueryValues(object):
    """
    Helper for handling query parameters
    """

    def __init__(self, values=None):
        if values is None:
            values = {}
        self.values = values

    def add(self, key, value=None):
        if value is None:
            return self

        elif isinstance(value, datetime):
            self._add(key, [value])
        else:
            self._add(key, ["{}".format(value)])
        return self

    def _add(self, key, values):
        if values is not None and len(values) > 0:
            self.values[key] = tuple(values)
        return self

    def add_query_values(self, prop, other):
        if other is None:
            return self

        if prop is None or len(prop) < 1:
            return self

        if isinstance(other, QueryValues):
            for key, value in other.values.items():
                if value is not None:
                    self.add(prop + "." + key, value)
        else:
            return self

    def fromRange(self, options: RangeFilteringOptions):
        if options is not None:
            self.add("lt", options.less_than)
            self.add("lte", options.less_than_or_equal_to)
            self.add("gt", options.greater_than)
            self.add("gte", options.greater_than_or_equal_to)
        return self

    def get_keys(self):
        return self.values.keys()