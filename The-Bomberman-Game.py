#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#
import sys
def createGrid(r, c, grid_at_previous_step):
    grid_at_next_step = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            current_cell = grid_at_previous_step[i][j]
            if current_cell == 'O':
                grid_at_next_step[i][j] = '.'
                if i - 1 >= 0:
                    grid_at_next_step[i - 1][j] = '.'
                if i + 1 <= r - 1:
                    grid_at_next_step[i + 1][j] = '.'
                if j - 1 >= 0:
                    grid_at_next_step[i][j - 1] = '.'
                if j + 1 <= c - 1:
                    grid_at_next_step[i][j + 1] = '.'
    return grid_at_next_step


def bomberMan(n, r, c, initial_grid):

    grid_after_first_detonation = createGrid(r, c, initial_grid)

    if n % 2 == 0:
        return [['O'] * c for _ in range(r)]
    elif n < 4:
        return initial_grid if n == 1 else grid_after_first_detonation
    else:
        grid_after_second_detonation = createGrid(r, c, grid_after_first_detonation)
        grid_after_third_detonation = createGrid(r, c, grid_after_second_detonation)
        return grid_after_second_detonation if n % 4 == 1 else grid_after_third_detonation

if __name__ == "__main__":
    r, c, n = input().strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []
    for _ in range(r):
       grid.append(list(str(input().strip())))
    result = bomberMan(n, r, c, grid)
    for row in result:
        print("".join(row))