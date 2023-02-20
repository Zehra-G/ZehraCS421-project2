"""
Zehra Gundogdu
CS421 Project 2 
tokenizecode.py
02/18/2023
"""
import os

root_dir = '/Users/zehragundogdu/Desktop/CS421/mplsci' #path to folder with matplotlib and scipy
python_files = []
file_contents = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".py"):
            print(filename)
            filepath = os.path.join(dirpath, filename)
            python_files.append(filepath)
            with open(filepath, "r") as f:
                file_contents.append(f.read())

with open("python_files.txt", "w") as f:
    for content in file_contents:
        f.write(content + "\n")