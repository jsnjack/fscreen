#!/usr/bin/env python2
import argparse
from subprocess import call


class Message:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(args):
    """
    Adjust system configuration that scales system font
    """
    print("Applying font scale factor: %s" % args.factor)

    set_gnome_settings(args.factor)


def set_gnome_settings(factor):
    code = call(["gsettings", "set", "org.gnome.desktop.interface", "text-scaling-factor", "%s" % factor])
    print_result("Applying GNOME settings", code)


def print_result(message, code):
    if code == 0:
        color = Message.GREEN
        result = "OK"
    else:
        color = Message.FAIL
        result = "ERROR(%s)" % code

    print("    " + color + message + "... " + result)


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("factor",
                        type=float,
                        action='store',
                        help='Font scale factor')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = get_args()
    main(args)
