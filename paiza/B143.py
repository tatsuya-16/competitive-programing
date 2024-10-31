import sys

def main(lines):

    # print(lines)
    nm = lines[0].split()
    # print(nm[0])
    result = [1] * (int(nm[0]) + 1)
    result[0] = 0
    i = 0

    for data in lines:
        if i >= 1:
            j = data.split()
            # print(j)
            if result[int(j[1])] == 0:
                result[int(j[0])] += 1
            else :
                result[int(j[0])] += result[int(j[1])]
            result[int(j[1])] = 0
        i += 1

    print(result)

    # 0でない要素とそのインデックスのペアを作成
    non_zero_elements = [(value, index) for index, value in enumerate(result) if value != 0]

    # 要素の大きさで降順、同じ要素の場合はインデックスで昇順にソート
    non_zero_elements.sort(key=lambda x: (-x[0], x[1]))

    # ソートされたインデックスのみを取得
    sorted_indices = [index for _, index in non_zero_elements]
    print(sorted_indices)

    max = 0


    for ans in sorted_indices:
        if max > int(ans) :
            break
        print(ans)
        max = int(ans)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)