import logging

from main import set_light_color


def test_color_blue(caplog):
    caplog.set_level(logging.INFO)
    set_light_color("blue")

