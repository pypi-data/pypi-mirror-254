"""Divider Bar by Gold Bars"""
from datetime import datetime
from .gold_calc import GoldBarCalc
from .gold_models import GoldBar
import decimal as dec


class GoldBarDivider:
    """Class provider static restriction"""

    def __init__(self, gold_bar_calc: GoldBarCalc, gold_bars: GoldBar) -> None:
        self._gold_bar_calc: GoldBarCalc = gold_bar_calc
        self._gold_bars = gold_bars

    def calc_bar_restriction(self, for_date_time: datetime) -> dec.Decimal:
        return self._gold_bar_calc.calc_gold_price(
            gold_unit=self._gold_bars,
            for_date_time=for_date_time,
        )
