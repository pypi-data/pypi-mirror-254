import decimal as dec
import typing as tp
from datetime import datetime


class PriceBarModel(tp.TypedDict):
    date_time: datetime
    open: dec.Decimal
    high: dec.Decimal
    low: dec.Decimal
    close: dec.Decimal
    volume: int
