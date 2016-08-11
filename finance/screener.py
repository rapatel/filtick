from . import filteropts

class StockScreener(object):
    """
    Stock screener class
    """
    def __init__(self):
        self.filter_list = []
        return

    def add_filter(self, filteropt):
        try:
            if filteropts.BaseFilterOption not in filteropt.__class__.__bases__:
                raise ValueError(filteropt.__class__.__bases__)
            self.filter_list.append(filteropt)
        except ValueError as err:
            print "Invalid filter option: {}".format(err.message)
        return
