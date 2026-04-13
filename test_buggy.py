def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # crashes if numbers is empty

def get_user(conn, username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return conn.execute(query)  # SQL injection

def read_config(path):
    f = open(path, "r")
    return f.read()  # file never closed
