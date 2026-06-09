VALID_SIDES = {"BUY", "SELL"}
VALID_ORDER_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol):
    if not symbol or not symbol.isalnum():
        raise ValueError(f"Invalid symbol '{symbol}'. Example: BTCUSDT")
    return symbol.upper()


def validate_side(side):
    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError(f"Invalid side '{side}'. Must be BUY or SELL.")
    return side


def validate_order_type(order_type):
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type '{order_type}'. Must be MARKET or LIMIT.")
    return order_type


def validate_quantity(quantity):
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError
        return qty
    except (ValueError, TypeError):
        raise ValueError(f"Invalid quantity '{quantity}'. Must be positive.")


def validate_price(price):
    try:
        p = float(price)
        if p <= 0:
            raise ValueError
        return p
    except (ValueError, TypeError):
        raise ValueError(f"Invalid price '{price}'. Must be positive.")


def validate_all(symbol, side, order_type, quantity, price=None):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    order_type = validate_order_type(order_type)
    quantity = validate_quantity(quantity)
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders.")
        price = validate_price(price)
    return symbol, side, order_type, quantity, price
