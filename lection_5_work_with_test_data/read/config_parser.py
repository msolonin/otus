import os
import configparser

# https://python-scripts.com/configparser-python-example
# Write cfg
path = '../data/local.cfg'
# config = configparser.ConfigParser()
# config.add_section("Settings")
# config.set("Settings", "font", "Courier")
# config.set("Settings", "font_size", "10")
# config.set("Settings", "font_style", "Normal")
# config.set("Settings", "font_info",
#            "You are using %(font)s at %(font_size)s pt")
#
# with open(path, "w") as config_file:
#     config.write(config_file)


# Read cfg


config = configparser.ConfigParser()
config.read(path)
# Читаем некоторые значения из конфиг. файла.
font = config.get("Settings", "font")
font_size = config.get("Settings", "font_size")

# Меняем значения из конфиг. файла.
config.set("Settings", "font_size", "12")

# Удаляем значение из конфиг. файла.
config.remove_option("Settings", "font_style")

# Вносим изменения в конфиг. файл.
with open(path, "w") as config_file:
    config.write(config_file)
