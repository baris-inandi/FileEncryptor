import os
import sys
import base64
from itertools import chain, islice
from fsplit.filesplit import Filesplit
fs = Filesplit()


def chunk(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def get_splits(size, str_len):
    threshold = 64
    if size >= 2:
        splits = round(size/2)
        return threshold if splits >= threshold else splits, round(str_len/splits)
    else:
        return 0, None


def insert_newlines(string, every=64):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    print()
    return '\n'.join(lines)

def splitfile(filename: str):
    b64filename = filename + ".b64"

    with open(filename, "rb") as basefile:
        b64str = str(base64.b64encode(basefile.read()))
        formatted_b64str = insert_newlines(b64str)
    with open(b64filename, "w+") as x:
        x.write(formatted_b64str)

    splits, split_stringsize = get_splits(round(os.path.getsize(b64filename)/1000000), len(formatted_b64str))

    if splits > 0:
        chunks_arr = chunk(b64str, split_stringsize)
        for i in chunks_arr:
            print(i + "\n\n\n")
    else:
        print("call encrypt function")

def join(source_dir, dest_file, read_size):
    output_file = open(dest_file, 'wb')
    parts = os.listdir(source_dir)
    parts.sort()
    for file in parts:
        path = os.path.join(source_dir, file)
        input_file = open(path, 'rb')
        while True:
            bytes = input_file.read(read_size)
            if not bytes:
                break
            output_file.write(bytes)
        input_file.close()
    output_file.close()

splitfile("uwu.txt")