import time
from worker import app


def main():
    while True:
        app.send_task("long_running_task")
        time.sleep(2)


if __name__ == "__main__":
    main()
