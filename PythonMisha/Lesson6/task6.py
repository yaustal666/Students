def calculateTip(totalPrice: float, percentage: float) -> float:
    return totalPrice * percentage

def calculateTotal(totalPrice: float, percentage: float) -> float:
    return calculateTip(totalPrice, percentage) + totalPrice

print(calculateTotal(20, 0.1))
