def divide(a: float, b: float) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_user(users: list, index: int):
    if not isinstance(users, list) or not isinstance(index, int):
        raise TypeError("users must be a list and index must be an int")
    if index < 0 or index >= len(users):
        raise IndexError(f"Index {index} is out of bounds for list of length {len(users)}")
    return users[index]

def calculate_discount(price: float, discount: float) -> float:
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("price and discount must be numeric")
    if discount > price:
        raise ValueError("Discount cannot be greater than price")
    final = price - discount
    return final
