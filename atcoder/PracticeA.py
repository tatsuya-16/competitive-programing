import sys

def main(lines):
    # print(lines)
    l2 = lines[1].split()
    sum = int(lines[0]) + int(l2[0]) + int(l2[1])
    print(str(sum) + ' ' + lines[2])


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
