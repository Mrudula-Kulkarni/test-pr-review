def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def get_user(conn, username):
    query = "SELECT * FROM users WHERE username = ?"
    return conn.execute(query, (username,))


def read_config(path):
    with open(path, "r") as f:
        return f.read()
