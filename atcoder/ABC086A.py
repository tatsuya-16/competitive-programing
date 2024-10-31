import sys

def main(lines):
    num = lines[0].split()
    if (int(num[0]) * int(num[1])) % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
