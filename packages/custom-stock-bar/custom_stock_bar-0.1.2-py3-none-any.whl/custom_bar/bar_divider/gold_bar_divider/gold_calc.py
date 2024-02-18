"""Gold Bar Calculator"""
from datetime import datetime
import pandas as pd
from .gold_models import GoldBar
import decimal as dec


class GoldBarCalc:
    def __init__(self, gold_df: pd.DataFrame) -> None:
        """param:
        gold_df - DataFrame For Gold Price
        """
        self._gold_df = gold_df

    def calc_gold_price(
        self,
        gold_unit: GoldBar,
        for_date_time: datetime,
    ) -> dec.Decimal:
        """Function for calculate price of Gold
        param:
        gold_unit - Size of gold (1g, 1ouz, 1kg. etc)
        for_date_time - Date and Time for which Date it will be calculater
        """

        trads = self._gold_df[self._gold_df["date_time"] <= for_date_time].iloc[-1]
        price_for_gram = trads.close

        return round(
            dec.Decimal(price_for_gram)
            * dec.Decimal(gold_unit.count * gold_unit.bar_type.value),
            4,
        )
