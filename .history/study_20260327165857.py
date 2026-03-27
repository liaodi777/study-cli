import sys
import json
import datetime
from pathlib import Path

DATA_FILE = Path("data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"sessions": [], "active_start": None}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def start():
    data = load_data()
    if data["active_start"] is not None:
        print("もう学習中だよ！先にstopしてね")
        return
    now = datetime.datetime.now().isoformat()
    data["active_start"] = now
    save_data(data)
    print(f"学習開始！({now})")

def main():
    if len(sys.argv) < 2:
        print("使い方: python3 study.py [start/stop/list]")
        return
    command = sys.argv[1]
    if command == "start":
        start()
    else:
        print(f"知らないコマンドだよ: {command}")

main()