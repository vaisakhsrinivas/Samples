def applyDiscount(price, discount):

    finalprice = 0

    if not isinstance(price, (int, float)) or isinstance(price, bool):
        return "The price should be a number"

    if not isinstance(discount, (int, float)) or isinstance(discount, bool):
        return "The price should be a number"

    if price <= 0:
        return "The price should greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    finalprice = price - price * (discount / 100)
    return finalprice


print(applyDiscount(100, 20)) #should return 80.
print(applyDiscount(200, 50)) #should return 100.
print(applyDiscount(50, 0)) #should return 50.
print(applyDiscount(50, 100)) #When apply_discount is called with a discount of 100, it should return 0.
print(applyDiscount(74.5, 20.0))# should return 59.6
