
--------------------------------------------------
Voly
------------------------------------------------
A Python application that analyzes real-time market data from 
multiple brokers to identify potential high-probability entry points.
Designed for traders seeking data-driven decisions using technical indicators,
sentiment signals, and cross-exchange insights.

 Features
----------------
✅ Real-time OHLCV data fetching from Binance and BigONE via ccxt

📊 Candlestick chart visualization using mplfinance

📉 Highlights volume discrepancies that could signal potential trade setups

🧠 Adjustable symbol, timeframe, and interval

💾 Saves analysis as a PNG image (volume_analysis.png)


Requirements 
------------------
Make sure you have the following installed:

pip install PyQt5 ccxt pandas matplotlib mplfinance


Run the App
---------------------------------------

python voly.py



UI Controls
------------------------
Symbol: Trading pair (e.g., ETH/USDT ,BTC/USDT)

Timeframe: Candlestick resolution (1m, 5m, 15m, 1h)

Interval: Number of candles to fetch (50–400)

Compute: Fetches data and updates the visualization


Data Source
------------------------------------------
The default brokers are Binance and BigONE, but any broker 
from the CCXT library can be used—provided that the selected 
trading pair is supported by both brokers.




 Output
------------------------
The plot is saved as:

volume_analysis.png

# Disclaimer:
This app is intended for research purposes only. The developers do not take any responsibility for any financial losses or damages resulting from the use of this app. Users are advised to make their own independent decisions and conduct thorough research before taking any actions based on the information provided by this app.

Voly Project. All rights reserved.

Open-source code, developed by [CHAKRAR ABDELMALIK].
