import sys
import json
from abc import ABCMeta, abstractmethod

class BaseFilter(object):
    """
    Common filter properaties
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_filter_name(self):
        pass

class MarketCapFilter(BaseFilter):
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

class EarningsPerShareFilter(BaseFilter):
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

class StockExchangeFilter(BaseFilter):
    """
    Stock exchange (NYSE, NASDAQ, AMEX)
    """
    VALID_EXCHANGES = ["NYSE", "NASDAQ", "AMEX"]
    NAME = "STX"
    def __init__(self, exchanges):
        self.exchanges = []
        try:
            for e in exchanges:
                if e not in StockExchangeFilter.VALID_EXCHANGES:
                    raise ValueError(e)
                self.exchanges.append(e)
        except ValueError as err:
            print("Invalid stock exchange!!: {}".format(err.message))
        return

    @classmethod
    def get_filter_name(cls):
        return cls.NAME
