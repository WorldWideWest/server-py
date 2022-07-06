from enum import Enum
from random import randrange
class Constants(Enum):
    HOST_NAME = "localhost"
    PORT = randrange(8000, 8999, 1)
    CONNECTION_STRING = "./task.db"
