#!/usr/bin/env python2
import argparse
import re
from subprocess import call, check_output


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
    set_firefox_settings(args.factor)


def set_gnome_settings(factor):
    code = call(["gsettings", "set", "org.gnome.desktop.interface", "text-scaling-factor", "%s" % factor])
    print_result("Applying GNOME settings", code)


def set_firefox_settings(factor):
    current_user = check_output(["whoami"]).replace("\n", "")
    config_re = re.compile("^/home/%s/\.mozilla/firefox/[\w]*\.default/prefs.js$" % current_user)
    prefs_locations = check_output(["locate", "prefs.js"]).split("\n")
    code = 1
    for item in prefs_locations:
        if config_re.match(item):
            print("Found configuration file: %s" % item)
            new_data = None
            with open(item, "rb") as config_file:
                data = config_file.read()
                new_data = re.sub(
                    'user_pref\("layout\.css\.devPixelsPerPx",\s"[\-\.0-9]*"\);',
                    'user_pref("layout.css.devPixelsPerPx", "%s");' % factor, data,
                    flags=re.M
                )
            if new_data:
                with open(item, "wb") as config_file:
                    config_file.write(new_data)
                    code = 0
            break
    print_result("Applying Firefox settings", code)


def print_result(message, code):
    if code == 0:
        color = Message.GREEN
        result = "OK"
    else:
        color = Message.FAIL
        result = "ERROR(%s)" % code

    print(color + message + "... " + result + Message.END)


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
