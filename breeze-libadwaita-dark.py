# /usr/bin/env python

import configparser

config = configparser.ConfigParser()
# KDE files often use case-sensitive keys for color names
config.optionxform = str

# Read the file
config.read("Breeze.colors")

config.read("/home/shane/.local/share/color-schemes/BreezeLibadwaitaDark.colors")

for section in config.sections():
    print(f"[{section}]")
    for option in config.options(section):
        mycolor = config.get(section, option)
        print(f" - {option}: {mycolor}")
