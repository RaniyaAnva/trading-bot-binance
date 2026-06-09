# Trading Bot – Binance Futures Testnet

A simplified Python trading bot that places Market and Limit orders on the Binance Futures Testnet (USDT-M).

---

## Setup Steps

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd trading_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file
```bash
cp .env.example .env
```
Then open `.env` and add your Binance Futures Testnet API credentials:
```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

> Get testnet credentials at: https://testnet.binancefuture.com

---

## How to Run

### Place a MARKET order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a LIMIT order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 50000
```

### Arguments

| Argument     | Required | Description                        |
|--------------|----------|------------------------------------|
| `--symbol`   | Yes      | Trading pair e.g. BTCUSDT          |
| `--side`     | Yes      | BUY or SELL                        |
| `--type`     | Yes      | MARKET or LIMIT                    |
| `--quantity` | Yes      | Quantity to trade e.g. 0.01        |
| `--price`    | No*      | Required only for LIMIT orders     |

---

## Project Structure

```
trading_bot/
  bot/
    __init__.py
    client.py         # Binance API client wrapper
    orders.py         # Order placement logic
    validators.py     # Input validation
    logging_config.py # Logging setup
  cli.py              # CLI entry point
  README.md
  requirements.txt
  .env.example
```

---

## Assumptions

- Uses Binance Futures **Testnet** only (base URL: `https://testnet.binancefuture.com`)
- All orders use `timeInForce=GTC` for LIMIT orders
- Logs are stored in `logs/trading_bot.log`
- Credentials are loaded from `.env` file using `python-dotenv`

---

## Logs

All API requests, responses, and errors are logged to:
```
logs/trading_bot.log
```
