"""
八皇后问题 (Eight Queens) — 回溯法经典实现

在 8x8 棋盘上放置 8 个皇后, 使任意两个皇后不在同一行、同一列、
同一斜线上。本实现用回溯 + 剪枝求出全部 92 种解, 并打印前 3 种。

运行: python3 eight_queens.py
"""

N = 8


def solve_n_queens(n=N):
    """返回全部解, 每个解是长度为 n 的列表, solutions[i] = 第 i 行皇后所在的列."""
    solutions = []
    cols = [False] * n          # 列是否已被占用
    diag1 = [False] * (2 * n)   # 主对角线 r - c + n - 1
    diag2 = [False] * (2 * n)   # 副对角线 r + c
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            d1 = row - col + n - 1
            d2 = row + col
            if cols[col] or diag1[d1] or diag2[d2]:
                continue
            board[row] = col
            cols[col] = diag1[d1] = diag2[d2] = True
            backtrack(row + 1)
            cols[col] = diag1[d1] = diag2[d2] = False
            board[row] = -1

    backtrack(0)
    return solutions


def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = "".join("Q " if solution[row] == col else ". " for col in range(n))
        print(line.rstrip())
    print()


if __name__ == "__main__":
    solutions = solve_n_queens(8)
    print(f"8皇后问题共有 {len(solutions)} 种解")
    assert len(solutions) == 92, "解的数量应为 92"
    for i, sol in enumerate(solutions[:3], 1):
        print(f"--- 解 {i}: {sol} ---")
        print_board(sol)
    print("测试通过: 92 种解全部求出")
