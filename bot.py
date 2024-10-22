import ccxt
import pandas as pd

exchange = ccxt.binance()

def fetch_historical_data(symbol, timeframe, since):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=since)
    return pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Calculate RSI
def calculate_rsi(data, window=14):
    delta = data['close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Generate Buy/Sell signals based on RSI
def calculate_signals_with_rsi(data):
    data['RSI'] = calculate_rsi(data)

    # Buy signal: RSI falls below 30 and then rises above it
    data['Buy_Signal'] = ((data['RSI'] < 30) & (data['RSI'].shift(1) >= 30)).astype(int)
    
    # Sell signal: RSI rises above 70 and then falls below it
    data['Sell_Signal'] = ((data['RSI'] > 70) & (data['RSI'].shift(1) <= 70)).astype(int)

    return data

symbol = 'BTC/USDT'
timeframe = '1d'
since = exchange.parse8601('2024-09-01T00:00:00Z')

data = fetch_historical_data(symbol, timeframe, since)

data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
data.set_index('timestamp', inplace=True)

data = calculate_signals_with_rsi(data)

print(data[['close', 'RSI', 'Buy_Signal', 'Sell_Signal']])
