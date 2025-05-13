import json
import os

DB_FILE = "admins.json"

def load_admins():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_admins(admins):
    with open(DB_FILE, "w") as f:
        json.dump(admins, f)
