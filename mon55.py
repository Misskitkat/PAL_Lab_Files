from pathlib import Path

def count_letters():
    # read paragraph
    # count number of es using a for loop
    # export it to an out file (write)
    path = Path('paragraph.txt')
    contents = path.read_text()
    lines = contents.splitlines()
    count = 0
    out = Path('e_out.txt')
    for line in lines:
        for char in line:
            if char.lower() == 'e':
                count += 1
    msg = "There are " + str(count) + " e's in this paragraph!"
    out.write_text(msg)
count_letters()

def compute_median():
    # read numbers
    # convert to floats
    # compute median
    # write to out file
    path = Path('numbers_sorted.txt')
    contents = path.read_text()
    lines = contents.splitlines()
    num_list = []
    out = Path('median_out.txt')
    for line in lines:
        num_list.append(float(line))
        mid = len(num_list)/2
    if mid % 2 != 0:
        msg = "The median of the given list of numbers is: " + str(num_list[round(mid)])
        out.write_text(msg)
    else:
        med = num_list[int(mid)] + num_list[int(mid-1)]
        msg = "The median of the given list of numbers is: " + str(med/2)
        out.write_text(msg)
    print(num_list)


compute_median()