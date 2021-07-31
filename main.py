import logging
import time


def main():
    init_complete = False
    set_light_color("blue")

    log_file_name = r"C:\Program Files (x86)\Steam\steamapps\common\Interplanetary Enhanced " \
                    r"Edition\Interplanetary_Data\output_log.txt"
    file = open(log_file_name, 'r')
    pos = file.tell()

    while True:
        li = file.readline()
        new_pos = file.tell()
        if new_pos == pos:  # stream position hasn't changed -> EOF
            # continue
            time.sleep(1)
            if not init_complete:
                logging.info("Initializing complete")
                init_complete = True
        else:
            pos = new_pos
            if init_complete:
                process_line(li)


def process_line(line):
    if 'Start Actionphase!' in line:
        set_light_color("red")
    if 'Actionphase ended!' in line:
        set_light_color("blue")


def set_light_color(color: str):
    logging.info("Setting color to %s", color)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    main()
