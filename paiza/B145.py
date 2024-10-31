import sys

def main(lines):

    l0 = lines[0].split()
    nums = lines[int(l0[0]) + 1].split()
    print(nums)
    print(lines)
    b = [0] * 3
    for i in range(int(l0[0])):
        b[i] = lines[i+1].split()
        print(b[i])
    
    ans = 0
    flag = 0
    # 縦
    for i in b:
        flag = 0
        for j in b[i]:
            for num in nums:
                if b[i][j] == num:
                    flag += 1
        if flag == int(l0[0]):
            ans += 1

    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
