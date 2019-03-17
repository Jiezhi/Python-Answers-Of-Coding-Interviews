"""
Des: 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样一个二维数组和一个整数，判断数组中是否含有该整数。

See: 《剑指 Offer》（第二版）P.44

How: P.47
"""


def find(matrix, num):
    if not matrix:
        return False
    rows = len(matrix)
    columns = len(matrix[0])
    column = columns - 1
    row = 0
    while column >= 0 and row < rows:
        tmp = matrix[row][column]
        if tmp == num:
            return True
        elif tmp > num:
            column -= 1
        else:
            row += 1
    return False


if __name__ == '__main__':
    matrix = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    assert find(matrix, num=7)
    assert not find(matrix, 18)
    assert not find([], num=8)
