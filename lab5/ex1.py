import re



pattern = re.compile(r'^a[b]*$')

with open('C:/Users/Alina/PPPP2/lab5/labka.txt', 'r', encoding='utf-8') as file:
    for line_number, line in enumerate(file, start=1):
        line = line.strip()
        match = pattern.fullmatch(line)

        if match:
            print(f"Line {line_number}: '{line}' matches the pattern.")
        # else:
        #     print(f"Line {line_number}: '{line}' does not match the pattern.")
