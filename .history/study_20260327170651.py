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

def stop():
    data = load_data()
    if data["active_start"] is None:
        print("まだ学習開始してないよ！先にstartしてね")
        return
    start_time = datetime.datetime.fromisoformat(data["active_start"])
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    total_seconds = int(duration.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    session = {
        "date": end_time.strftime("%Y-%m-%d"),
        "start": data["active_start"],
        "end": end_time.isoformat(),
        "minutes": minutes
    }
    data["sessions"].append(session)
    data["active_start"] = None
    save_data(data)
    print(f"お疲れ！{minutes}分{seconds}秒勉強したよ✨")

def main():
    if len(sys.argv) < 2:
        print("使い方: python3 study.py [start/stop/list]")
        return
    command = sys.argv[1]
    if command == "start":
        start()
    elif command == "stop":
        stop()
    else:
        print(f"知らないコマンドだよ: {command}")

main()