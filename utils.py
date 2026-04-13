def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except (FileNotFoundError, PermissionError) as e:
        raise RuntimeError(f"Failed to read file '{path}': {e}")

def get_config(config, key):
    if key not in config:
        raise KeyError(f"Config key '{key}' not found")
    return config[key]
