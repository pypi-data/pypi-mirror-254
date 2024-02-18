"""Gold Bar Divider models"""

from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class GoldBarTypes(Enum):
    GRAM = 1  # One Gram
    T_OUNCE = 31.1034768  # One troy ounce
    KG = 1000  # 1 KG
    KG_11 = 1000 * 11   # 11 Kg (GOST-28058)
    T_OUNCE_400 = 31.1034768 * 400  # 400 troy ounce (or 12.4 Kg)


@dataclass
class GoldBar:
    count: int
    bar_type: GoldBarTypes
