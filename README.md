# Trading Bot with RSI Strategy

This is a simple trading bot built in Python that uses the **Relative Strength Index (RSI)** to generate buy and sell signals for cryptocurrency trading. The bot fetches historical price data from Binance using the `ccxt` library, calculates the RSI, and identifies trading opportunities based on the RSI values.

## How It Works

The trading bot uses the **RSI Strategy**, a popular momentum indicator that measures the speed and change of price movements. The bot:
- Fetches historical market data from the Binance exchange.
- Calculates the **Relative Strength Index (RSI)** based on the closing prices.
- Generates **Buy Signals** when the RSI crosses above 30 (indicating oversold conditions).
- Generates **Sell Signals** when the RSI crosses below 70 (indicating overbought conditions).

## Prerequisites

Before running the trading bot, make sure you have the following:
- Python 3.6 or higher
- Virtual environment (optional but recommended)
- An internet connection for fetching live market data

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/cmartdec/rsi_trading_bot_python
    cd trading-bot
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    ```
    - **Windows**: `venv\Scripts\activate`
    - **Mac/Linux**: `source venv/bin/activate`

3. **Install the Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```
   The main dependencies are:
   - `pandas`: For handling data structures.
   - `ccxt`: For fetching historical market data from the Binance exchange.

