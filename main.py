import logging
import sys
import time
from enum import Enum, auto
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class LogLineEvent(Enum):
    UnmatchedLine = auto()
    ActionPhaseStartLine = auto()
    ActionPhaseEndLine = auto()


def main():
    log_file_name = r"C:\Program Files (x86)\Steam\steamapps\common\Interplanetary Enhanced " \
                    r"Edition\Interplanetary_Data"
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = log_file_name
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == '__main__':
    main()
