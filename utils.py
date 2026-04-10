cat > utils.py << 'EOF'
def divide(a, b):
    return a / b

def get_user(users, index):
    return users[index]

def calculate_discount(price, discount):
    final = price - discount
    return final
