from pypika.terms import AnalyticFunction


class RowNumber(AnalyticFunction):
    def __init__(self, **kwargs):
        super(RowNumber, self).__init__("ROW_NUMBER", **kwargs)
