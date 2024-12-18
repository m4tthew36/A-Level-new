def applyDiscount(price: float, discount: int) -> float: 
    """Takes a price and discount. It then calcualtes a new price whith the discount applied"""

    adiscount = discount / 100
    return price * adiscount

print(applyDiscount(100, 20))


