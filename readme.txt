
--------------------------------------------------
Voly
------------------------------------------------
Voly is a lightweight PyQt5 desktop application designed to detect potential 
market activity by analyzing volume differences between
two major crypto exchanges (Binance and BigONE). 
The app visualizes price movements as candlestick 
charts alongside normalized  volume disparities 
to help users quickly identify unusual spikes that may indicate trading opportunities.

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



Voly Project. All rights reserved.

Open-source code, developed by [CHAKRAR ABDELMALIK].
