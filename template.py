import os
import sys


CODE_TEMPLATE = """\
def solve(f):
    for line in open(f).read().splitlines():
        pass

def solve2(f):
    pass
    

if __name__ == '__main__':
    print(solve('{day:02d}_test.txt'))
    # print(solve('{day:02d}.txt'))
    # print(solve2('{day:02d}_test.txt'))
    # print(solve2('{day:02d}.txt'))
"""

def make_files(year, day):
    prefix = f"{year}/{day:02d}"
    py_path = prefix + '.py'
    if os.path.exists(py_path):
        print(py_path, 'already exists, will not replace existing file')
    txt_path = prefix + '.txt'
    test_path = prefix + '_test.txt'

    code = CODE_TEMPLATE.format(day=day)
    with open(py_path, 'w') as f:
        f.write(code)
    with open(txt_path, 'w') as f:
        pass
    with open(test_path, 'w') as f:
        pass


if __name__ == '__main__':
    year, day = sys.argv[1:3]
    make_files(int(year), int(day))
