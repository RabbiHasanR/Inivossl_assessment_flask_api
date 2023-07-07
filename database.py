class Reading:
   def __init__(self, time, name, value):
    self.time = time
    self.name = name
    self.value = value

database = {}


def add_reading(key: str, reading: Reading) -> None:
    database[key] = reading


def get_reading(key: str) -> Reading | None:
    return database.get(key)