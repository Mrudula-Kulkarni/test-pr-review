def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)


def get_user(conn, username):
    query = "SELECT * FROM users WHERE username = ?"
    result = conn.execute(query, (username,)).fetchone()
    if result is None:
        raise ValueError(f"User '{username}' not found")
    return result


def read_config(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {path}")
