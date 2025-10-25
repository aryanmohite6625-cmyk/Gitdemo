import os
file_name="sample.txt"
if os.path.exists(file_name):
    print("Reading file content:")
    fh = open(file_name, "rt")
    content = fh.read()
    print(content)

else:
    print(f"Error: file {file_name} doesn't exist! ")