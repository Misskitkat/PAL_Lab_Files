# have names
# function
# open names
# print fstring
# names.title()
# writing to a file

from pathlib import Path

def write_greetings():
    path = Path('names.txt')
    contents = path.read_text()
    lines = contents.splitlines()
    msg = ''
    for line in lines:
        msg += ('Dear ' + line.title() + ',\n')
        # print(f'Dear {line.title()},')
    # print(f'Dear {contents},')
    out = Path('file_out.txt')
    out.write_text(msg)

write_greetings()

def compute_median():
    path = Path('numbers_sorted.txt')
    contents = path.read_text()
    lines = contents.splitlines()
    median = 0
    for line in lines:

    out = Path('median_out.txt')
    out.write_text(median)