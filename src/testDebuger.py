def calculate_total(price: float, quantity: int) -> float:
    total = price + quantity
    return total


price = 100
quantity = 3

result = calculate_total(price, quantity)

print(result)
