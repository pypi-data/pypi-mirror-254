"""Main Converter Price to Custom Bar"""
import pandas as pd
from .protocols.divider_protocol import BarDividerProtocol
from .models import PriceBarModel


class BarConverter:
    def __init__(self, bar_divider: BarDividerProtocol) -> None:
        self._bar_divider: BarDividerProtocol = bar_divider

    @staticmethod
    def _aggregate_price(curr_ohlc: pd.Series):
        # calc curr. total traid price
        # (mean, we don't have all transaction dataset)
        return (curr_ohlc.open + curr_ohlc.high + curr_ohlc.low + curr_ohlc.close) / 4

    @staticmethod
    def _make_output_df(price_bars: list[PriceBarModel]) -> pd.DataFrame:
        price_bars_df = pd.DataFrame(
            data=price_bars,
            columns=["date_time", "open", "high", "low", "close", "volume"],
        )
        price_bars_df = price_bars_df.set_index("date_time")
        price_bars_df["date_time"] = price_bars_df.index

        return price_bars_df

    def make_custom_bars(self, trades: pd.DataFrame) -> pd.DataFrame:
        """Convert TimeSeries to Custom Bar (DollarBar, Gold Bar, etc.)"""
        summ_price = 0
        start_bar = 0
        price_bars = []
        for i in range(len(trades)):
            current_price = self._aggregate_price(trades.iloc[i])
            summ_price += current_price * trades.iloc[i].volume
            current_time = trades.iloc[i].date_time

            # Dynamical provide current restriction
            if (
                summ_price >= self._bar_divider.calc_bar_restriction(current_time)
                or i == len(trades) - 1
            ):
                price_bars.append(
                    PriceBarModel(
                        date_time=trades.iloc[start_bar].date_time,
                        open=trades.iloc[start_bar].open,
                        high=trades.iloc[start_bar:i].high.max(),
                        low=trades.iloc[start_bar:i].low.min(),
                        close=trades.iloc[i].close,
                        volume=trades.iloc[start_bar:i].volume.sum(),
                    ),
                )
                start_bar = i + 1
                summ_price = 0

        return self._make_output_df(price_bars=price_bars)
