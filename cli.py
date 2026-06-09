import argparse
import os
import sys
from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.orders import place_order, print_order_summary
from bot.validators import validate_all

load_dotenv()


def get_credentials():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    if not api_key or not api_secret:
        print("❌ Error: BINANCE_API_KEY and BINANCE_API_SECRET must be set in .env file.")
        sys.exit(1)
    return api_key, api_secret


def build_parser():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity (e.g. 0.01)")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT orders)")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        symbol, side, order_type, quantity, price = validate_all(
            args.symbol, args.side, args.order_type, args.quantity, args.price
        )
    except ValueError as e:
        print(f"❌ Validation Error: {e}")
        sys.exit(1)

    api_key, api_secret = get_credentials()
    client = BinanceClient(api_key, api_secret)

    try:
        order = place_order(client, symbol, side, order_type, quantity, price)
        print_order_summary(order, symbol, side, order_type, quantity, price)
    except Exception as e:
        print(f"\n❌ Order Failed: {e}")
        print("Check logs/trading_bot.log for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
