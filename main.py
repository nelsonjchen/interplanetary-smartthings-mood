import asyncio
import logging
import msvcrt
import os
import time

import aiohttp
import pysmartthings
import win32file


def main():
    init_complete = False
    set_light_color("blue")

    log_file_name = r"C:\Program Files (x86)\Steam\steamapps\common\Interplanetary Enhanced " \
                    r"Edition\Interplanetary_Data\output_log.txt"

    file_handle = win32file.CreateFile(
        log_file_name, win32file.GENERIC_READ,
        win32file.FILE_SHARE_DELETE | win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE,
        None,
        win32file.OPEN_EXISTING,
        win32file.FILE_ATTRIBUTE_NORMAL,
        None
    )
    file = os.fdopen(msvcrt.open_osfhandle(int(file_handle), os.O_RDONLY))
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
    if 'DisplayActionphase' in line:
        set_light_color("red")
    if 'Actionphase ended!' in line:
        set_light_color("blue")


def set_light_color(color: str):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_set_light_color(color))


async def _set_light_color(color: str):
    logging.info("Setting color to %s", color)
    token = os.environ['TOKEN']
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()
        for device in devices:
            pass
            # print("{}: {}".format(device.device_id, device.label))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    main()
