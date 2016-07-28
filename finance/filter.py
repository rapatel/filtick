"""
Contains the filter options that can be used
to filter out tickers
"""

from abc import ABCMeta, abstractmethod

class BaseFilterOption(object):
    """
    Common filter properaties
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_filter_name(self):
        """
        Returns name of filter option
        """
        pass

class MarketCapFilterOpt(BaseFilterOption):
    """
    Market capitalization
    """
    NAME = "MKC"
    def __init__(self, mn, mx):
        self.min = mn
        self.max = mx
        return

    @classmethod
    def get_filter_name(cls):
        return cls.NAME

class EarningsPerShareFilterOpt(BaseFilterOption):
    """
    Earnings per share
    """
    NAME = "EPS"
    def __init__(self, mn, mx):
        self.min = mn
        self.max = mx
        return

    @classmethod
    def get_filter_name(cls):
        return cls.NAME

class StockExchangeFilterOpt(BaseFilterOption):
    """
    Stock exchange (NYSE, NASDAQ, AMEX)
    """
    VALID_EXCHANGES = ["NYSE", "NASDAQ", "AMEX"]
    NAME = "STX"
    def __init__(self, exchanges):
        self.exchanges = []
        try:
            for exchange in exchanges:
                if exchange not in self.VALID_EXCHANGES:
                    raise ValueError(exchange)
                self.exchanges.append(exchange)
        except ValueError as err:
            print"Invalid stock exchange!!: {}".format(err.message)
        return

    @classmethod
    def get_filter_name(cls):
        return cls.NAME
