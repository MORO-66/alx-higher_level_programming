#!/usr/bin/python3
""" Puzzle queen challenge """

from sys import argv, exit


def place(N, row, col, result):
    """ Place queens recursively """
    while col < N:
        if isvalid(row, col, result):
            result.append([row, col])
            if row == N-1:
                print(result)
                result.pop()
            else:
                place(N, row+1, 0, result)
        col += 1
    if len(result) > 0:
        result.pop()
    return


def isvalid(row, col, result):
    """ Check if the position is valid """
    diag1 = [pos[0] + pos[1] for pos in result]
    diag2 = [pos[1] - pos[0] for pos in result]
    cols = [pos[1] for pos in result]
    rows = [pos[0] for pos in result]
    if row in rows or col in cols or row + col in diag1 or col - row in diag2:
        return False
    return True


if __name__ == "__main__":
    length = len(argv)
    if length != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)
    result = []
    place(N, 0, 0, result)
