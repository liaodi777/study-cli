import sys

def start():
    print("学習を開始するよ！")

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