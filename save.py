import os, json

save_path = "save.json"

def save_exists():
    os.path.exists(save_path)