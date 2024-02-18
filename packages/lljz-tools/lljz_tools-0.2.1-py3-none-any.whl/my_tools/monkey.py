# coding=utf-8
import logging
import sys

from my_tools.log_manager import LogManager

_print_logger = LogManager(
    'print',
    level=logging.DEBUG,
    console_colors={"INFO": "cyan"},
    formatter='%(asctime)s.%(msecs)03d - %(name)s - %(message)s',
    log_file='/pythonlog/print.log', error_log_file=''
).get_logger()


def my_print(*args, sep=' ', end='\n', file=None, flush=False):
    fra = sys._getframe(1)
    line = fra.f_lineno
    file_name = fra.f_code.co_filename
    # logger.info(fra.f_code.co_name)
    args = (f'"{file_name}:{line}" - {fra.f_code.co_name} :', *args)
    if file in [sys.stdout, None]:
        _print_logger.info(sep.join(map(str, args)))
    else:
        _print_logger.error(sep.join(map(str, args)))


print_raw = print


def patch_print():
    try:
        __builtins__.print = my_print

    except AttributeError:
        __builtins__['print'] = my_print


def restore_print():
    try:
        __builtins__.print = print_raw
    except AttributeError:
        __builtins__['print'] = print_raw


if __name__ == '__main__':
    patch_print()


    def func():
        print("Hello World")


    def to():
        func()


    to()
