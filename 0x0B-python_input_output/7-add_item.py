#!/usr/bin/python3
"""Add arguments to a Python list and save them to a JSON file"""
import sys

save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        #To load existing list from the file
        args = load_from("add_item.json")
    except FileNotFoundError:
        #Create an empty list if file doesnt exist
        args = []

    #Add command-line arguments to the list
    args.extend(sys.argv[1:])

    #Save the updated list to the file
    save_to(args, "add_item.json")
