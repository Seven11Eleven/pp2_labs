import os
for root, directories, files in os.walk(r"C:\Users\Alina\PPPP2"):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)