import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "db")
LOG_FILE = os.path.join(DB_DIR, "log.csv")