"""Divider bar by Constant price"""
import decimal as dec
from datetime import datetime


class PriceDivider:
    """Class provider Golder Bar Restrictions"""

    def __init__(self, static_restriction: dec.Decimal) -> None:
        self._restriction: dec.Decimal = static_restriction

    def calc_bar_restriction(self, *args, **kwargs) -> dec.Decimal:
        return self._restriction
