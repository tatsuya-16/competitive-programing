n = int(input())
ct, cx, cy = 0, 0, 0
flag = 0
for i in range(n):
    t, x, y = map(int, input().split())
    abs_x = abs(x - cx)
    abs_y = abs(y - cy)
    if (abs_x + abs_y) == (t - ct):
        flag += 1
    ct, cx, cy = t, x, y

if flag == n:
    print('Yes')
else:
    print('No')
