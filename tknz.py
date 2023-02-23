import os
import string

# Specify the directory to search for Python files
root_dir = '/Users/zehragundogdu/Desktop/CS421/mplsci' 

# Initialize lists to hold Python file paths and their contents
python_files = []
file_contents = []

# Crawl through the directory looking for Python files
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(".py"):
            filepath = os.path.join(dirpath, filename)
            python_files.append(filepath)
            with open(filepath, "r") as f:
                file_contents.append(f.read())

# Write the Python files into a single text file
with open("python_files2.txt", "w") as f:
    for content in file_contents:
        f.write(content + "\n")

# Count the number of lines and tokens in the resulting file
num_lines = 0
num_tokens = 0

tokenlist = []

with open("python_files2.txt", "r") as f:
    for line in f:
        # Count the number of lines
        num_lines += 1

        # Tokenize the line by lowercasing everything and splitting on all whitespace and punctuation characters
        tokens = line.translate(str.maketrans("", "", string.punctuation)).lower().split()
        for word in tokens:
            tokenlist.append(word)
        num_tokens += len(tokens)

print(f"Number of lines: {num_lines}")
print(f"Number of tokens: {num_tokens}")

print(tokenlist[3])