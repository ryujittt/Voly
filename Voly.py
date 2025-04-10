import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QTextEdit, QLabel,QSizePolicy, QHBoxLayout,QComboBox,QLineEdit,QCheckBox,QPushButton
from PyQt5.QtGui import QFont, QPalette, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer
import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf

class Voly(QMainWindow):
    def __init__(self):
        super().__init__()
        

        
        self.setWindowTitle("Voly")  # ← App name here
        self.binance_exchange = ccxt.binance()  
        self.bigone_exchange = ccxt.bigone()  



        self.setup_ui()
        self.fetch_and_plot_data()




    def setup_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)


        

        

        self.layout = QVBoxLayout(self.central_widget)
        self.labels = QHBoxLayout()
        self.layout.addLayout(self.labels)






        self.label_symbol = QLabel()
        self.label_symbol.setText('Symbol')
        self.labels.addWidget(self.label_symbol)


        self.symbol_combobox = QLineEdit()
    
        self.symbol_combobox.setText('ETH/USDT')
        self.labels.addWidget(self.symbol_combobox)


        self.label_timeframe = QLabel()
        self.label_timeframe.setText('Timeframe')
        self.labels.addWidget(self.label_timeframe)

        # Add QComboBox for timeframe
        self.timeframe_combobox = QComboBox(self)
        self.timeframe_combobox.addItems(['1m', '5m', '15m', '1h'])  # Add more options as needed
        self.labels.addWidget(self.timeframe_combobox)
        self.timeframe_combobox.setCurrentIndex(1)

        self.label_limit = QLabel()
        self.label_limit.setText('Interval')
        self.labels.addWidget(self.label_limit)

        # Add QComboBox for limit
        self.limit_combobox = QComboBox(self)
        self.limit_combobox.addItems(['50','100', '150', '200', '300', '400'])  # Add more options as needed
        self.labels.addWidget(self.limit_combobox)
        self.limit_combobox.setCurrentIndex(0)
        
        self.compute = QPushButton('Compute', self)
        self.compute.clicked.connect(self.update_data)
        self.labels.addWidget(self.compute)




        self.save_direction = 'volume_analysis.png'
    def update_data(self):
#         try:
        self.fetch_and_plot_data()
#         except:
#             pass
    def fetch_and_plot_data(self):
        volume_signal,data = self.fetch_historical_data()


        
        self.plot_data(data)

    def fetch_historical_data(self):
        
        self.symbol = self.symbol_combobox.text()
        self.timeframe = self.timeframe_combobox.currentText()
        self.limit = int(self.limit_combobox.currentText())
        
        binance_ohlcv = self.binance_exchange.fetch_ohlcv(self.symbol, self.timeframe, limit=self.limit)
        bigone_ohlcv = self.bigone_exchange.fetch_ohlcv(self.symbol, self.timeframe, limit=self.limit)

        binance_df = pd.DataFrame(binance_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        binance_df['timestamp'] = pd.to_datetime(binance_df['timestamp'], unit='ms')  # Convert timestamp to datetime format
        binance_df.set_index('timestamp', inplace=True)  # Set timestamp as index


        bigone_df = pd.DataFrame(bigone_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

        
        binance_df = binance_df.iloc[:-1]
        bigone_df = bigone_df.iloc[:-1]
        
        normalized_volume_bigone = abs(self.normalize_column(bigone_df.volume.values) - self.normalize_column(binance_df.volume.values))
        factor = 6
        volume_signal = normalized_volume_bigone[-1] > normalized_volume_bigone[-2]*factor
        
        data = [binance_df,normalized_volume_bigone]
        return volume_signal,data








    def plot_data(self, data):
        self.figure, (self.ax1) = plt.subplots(1,1,figsize=(45, 35), sharex=True)

        
        array = np.arange(len(data[1]))
        self.ax1.clear()

        

        mpf.plot(data[0], type='candle', style='charles',  volume=False,ax = self.ax1)
        
        self.ax2 = self.ax1.twinx()
        

        self.ax2.bar(array,data[1], color='#FFCC66' , alpha = 0.6)


        self.save_image()
        
    def save_image(self):
        plt.savefig(f'{self.save_direction}')
        
        
            
    def normalize_column(self,column):
        min_val = column.min()
        max_val = column.max()
        normalized_column = (column - min_val) / (max_val - min_val)
        return normalized_column


            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Voly()
    window.show()
    sys.exit(app.exec_())
