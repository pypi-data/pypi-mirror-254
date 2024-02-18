import typing as tp
import decimal as dec
from datetime import datetime


class BarDividerProtocol(tp.Protocol):
    """Protocol for Bar Divider"""

    def calc_bar_restriction(self, for_date_time: datetime) -> dec.Decimal:
        """Calculate bar restriction"""
