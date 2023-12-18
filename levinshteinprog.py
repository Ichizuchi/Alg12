def edit_td(a, b, matrix, infinity, i, j):
    if matrix[i][j] == infinity:
        if i == 0:
            matrix[i][j] = j
        elif j == 0:
            matrix[i][j] = i
        else:
            ins = edit_td(a, b, matrix, infinity, i, j - 1) + 1
            del_val = edit_td(a, b, matrix, infinity, i - 1, j) + 1
            sub = edit_td(a, b, matrix, infinity, i - 1, j - 1) + (a[i - 1] != b[j - 1])
            matrix[i][j] = min(ins, del_val, sub)
    return matrix[i][j]


def edit_bu(a, b, len_a, len_b):
    matrix = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    for i in range(len_a + 1):
        matrix[i][0] = i
    for j in range(1, len_b + 1):
        matrix[0][j] = j
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            c = a[i - 1] != b[j - 1]
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + c
            )
    return matrix


def restore(a, b, matrix, len_a, len_b):
    str_re1, str_re2 = "", ""
    i, j = len_a, len_b
    while i != 0 or j != 0:
        if i != 0 and matrix[i][j] == matrix[i - 1][j] + 1:
            str_re1 += a[i - 1]
            str_re2 += '-'
            i -= 1
        elif j != 0 and matrix[i][j] == matrix[i][j - 1] + 1:
            str_re1 += '-'
            str_re2 += b[j - 1]
            j -= 1
        else:
            str_re1 += a[i - 1]
            str_re2 += b[j - 1]
            i -= 1
            j -= 1
    return str_re1[::-1], str_re2[::-1]


def edit_dist(a, b, len_a, len_b):
    infinity = float('inf')
    matrix = [[infinity] * (len_b + 1) for _ in range(len_a + 1)]
    edit_1 = edit_td(a, b, matrix, infinity, len_a, len_b)
    edit_2 = edit_bu(a, b, len_a, len_b)
    solution = restore(a, b, matrix, len_a, len_b)
    if matrix == edit_2:
        return edit_1, solution
    else:
        print("Incorrect")
        exit(1)


if __name__ == "__main__":
    str_1 = "editing"
    str_2 = "distance"
    result = edit_dist(str_1, str_2, len(str_1), len(str_2))
    print(result[1][0])
    print(result[1][1])
    print(result[0])
