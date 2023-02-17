import yfinance as yf
import pandas as pd

# Set the ticker symbol and time period
ticker = "AUDCAD=X"
start_date = pd.Timestamp.today() - pd.Timedelta(days=90)
end_date = pd.Timestamp.today()

# Retrieve the data from Yahoo Finance
data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Calculate the opening range for the first hour of trading
data["First Hour Range"] = data.apply(lambda x: x["High"] - x["Low"] if x.name.hour == 0 else pd.NaT, axis=1)

# Filter out rows without a first hour range
data = data[data["First Hour Range"].notnull()]

# Calculate the average opening range for the first hour of trading
avg_first_hour_range = data["First Hour Range"].mean()

print("Average opening range on AUD/CAD during the first hour of equities trading over the last 3 months: {:.2f} pips".format(avg_first_hour_range))
