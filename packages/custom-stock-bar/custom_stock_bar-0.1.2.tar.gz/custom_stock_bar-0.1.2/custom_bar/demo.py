import custom_bar.converter as conv
import custom_bar.bar_divider.gold_bar_divider as gold
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


def rename_yf_column_names(yf_df: pd.DataFrame) -> pd.DataFrame:
    return yf_df.rename(
        columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Volume": "volume",
        }
    )


def prepare_datetime(yf_df: pd.DataFrame) -> pd.DataFrame:
    yf_df["date_time"] = yf_df.index
    return yf_df


def plotting(main_price, gold_price):
    plt.figure(figsize=(10, 6))
    plt.plot(main_price["close"], label="Main Price", color="green")
    plt.plot(gold_price["close"], label="Gold Price", color="gold")
    plt.title("Main and Gold Price")
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.legend()
    plt.grid(True)
    plt.show()


# Fetch Gold price historical data
start_date, end_date = "2022-01-01", "2023-01-01"

demo_gold_ticker = "GC=F"
gold_price_data = yf.download(
    demo_gold_ticker,
    start=start_date,
    end=end_date,
    interval="1d",
)
gold_price_data = rename_yf_column_names(gold_price_data)
gold_price_data = prepare_datetime(gold_price_data)

demo_gold_ticker = "AAPL"
stock_price_data = yf.download(demo_gold_ticker, start=start_date, end=end_date)
stock_price_data = rename_yf_column_names(stock_price_data)
stock_price_data = prepare_datetime(stock_price_data)


gold_bar_provider = gold.GoldBarCalc(
    gold_df=gold_price_data,
)

gold_bar_restrict = gold.GoldBar(
    count=10_000,
    bar_type=gold.GoldBarTypes.T_OUNCE_400,
)

bar_divider = gold.GoldBarDivider(
    gold_bar_calc=gold_bar_provider,
    gold_bars=gold_bar_restrict,
)
gold_bar_converter = conv.BarConverter(
    bar_divider=bar_divider,
)


stock_price_in_gold_bar = gold_bar_converter.make_custom_bars(
    trades=stock_price_data,
)

show_columns = ["open", "high", "low", "close", "volume"]
print(stock_price_data[show_columns])
print(stock_price_in_gold_bar[show_columns])

print("len gold", len(stock_price_in_gold_bar))
print("len price", len(stock_price_data))
print("min", stock_price_data.low.min())
print("max", stock_price_data.high.max())
print(stock_price_data)

plotting(stock_price_data, stock_price_in_gold_bar)
