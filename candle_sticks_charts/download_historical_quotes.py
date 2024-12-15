from yfinance import download

stock_name = "ITC"

data =download(f"{stock_name}.NS")
data.to_csv(r"\candle_sticks_charts\Data\ITC.csv")
