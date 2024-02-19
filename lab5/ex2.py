import re

pattern = re.compile(r'^ab{2,3}$')

file_path = r'C:\Users\Alina\PPPP2\lab5\labka.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()
        match = pattern.fullmatch(line)

        if match:
            print(line_number,line)
