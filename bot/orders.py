from bot.client import BinanceClient
from bot.logging_config import get_logger

logger = get_logger(__name__)


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing {order_type} {side} order | symbol={symbol}")
        result = client.place_order(symbol, side, order_type, quantity, price)
        return result
    except Exception as e:
        logger.error(f"Order placement failed: {e}")
        raise


def print_order_summary(order, symbol, side, order_type, quantity, price=None):
    print("\n" + "=" * 50)
    print("       ORDER REQUEST SUMMARY")
    print("=" * 50)
    print(f"  Symbol     : {symbol.upper()}")
    print(f"  Side       : {side.upper()}")
    print(f"  Type       : {order_type.upper()}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("-" * 50)
    print("       ORDER RESPONSE")
    print("-" * 50)
    print(f"  Order ID   : {order.get('orderId', 'N/A')}")
    print(f"  Status     : {order.get('status', 'N/A')}")
    print(f"  Executed   : {order.get('executedQty', 'N/A')}")
    print(f"  Avg Price  : {order.get('avgPrice', 'N/A')}")
    print("=" * 50)
    print("  Order placed successfully!")
    print("=" * 50 + "\n")
