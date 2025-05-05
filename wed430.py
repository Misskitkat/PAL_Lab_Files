from pathlib import Path


def write_greetings():
    path = Path('names.txt')
    contents = path.read_text()
    lines = contents.splitlines()
    out = Path("file_out.txt")
    msg = ""
    for line in lines:
        msg += "Dear " + line.title() + ", \n"
        out.write_text(msg)


write_greetings()

def compute_average():
    path = Path('numbers.txt')
    contents = path.read_text()
    lines = contents.splitlines()
    out = Path("avg_out.txt")
    sum = 0
    num = 0
    for line in lines:
        sum += int(line)
        num += 1
    avg = sum/num
    out.write_text(str(avg))

compute_average()