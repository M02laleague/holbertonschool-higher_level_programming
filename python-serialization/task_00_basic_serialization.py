#!usr/bin/python3
"""Module coutain 2 function (Serialisize and deserialisize)"""
import json


def serialize_and_save_to_file(data, filename):
    """Function to serialize and save to file"""
    with open(filename, mode="w") as file:
        json.dump(data, file)
    
def load_and_deserialize(filename):
    """Function to load and deserialize from a file"""
    with open(filename, mode="r") as file:
        return json.load(file)