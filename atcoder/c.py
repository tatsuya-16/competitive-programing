s = input()
i = 0
flag = 0
ans = 0
tmp = ""

for c in s:
    if i == 0:
        tmp = c
    else:
        if tmp != c:
            ans += 1
        tmp = c
    i += 1

print(ans)