#!/usr/bin/python3
"""this load,add,and save to a json file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__("6-load_from_json_file.py").load_from_json_file


args = argv
if len(args) > 1:
    args = args[1:]
else:
    args = []
filename = "add_item.json"
try:
    text = load_from_json_file(filename)
except Exception:
    text = []
for arg in args:
    text.append(arg)
save_to_json_file(text, filename)
