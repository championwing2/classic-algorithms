"""
深度优先搜索 (DFS) — 递归与迭代两种经典实现

示例图 (无向图):
    A -- B -- D
    |    |    |
    C -- E -- F

运行: python3 dfs.py
"""

from collections import deque


# 邻接表表示的图
GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["B", "C", "F"],
    "F": ["D", "E"],
}


def dfs_recursive(graph, start, visited=None):
    """递归 DFS, 返回访问顺序."""
    if visited is None:
        visited = set()
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)

    _dfs(start)
    return order


def dfs_iterative(graph, start):
    """迭代 DFS (显式栈), 返回访问顺序."""
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        # 逆序压栈, 使弹出顺序与邻接表顺序一致
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return order


def dfs_path(graph, start, goal):
    """DFS 找一条从 start 到 goal 的路径, 找不到返回 None."""
    visited = set()
    path = []

    def _dfs(node):
        visited.add(node)
        path.append(node)
        if node == goal:
            return True
        for neighbor in graph.get(node, []):
            if neighbor not in visited and _dfs(neighbor):
                return True
        path.pop()
        return False

    return path if _dfs(start) else None


if __name__ == "__main__":
    recursive_order = dfs_recursive(GRAPH, "A")
    iterative_order = dfs_iterative(GRAPH, "A")
    path = dfs_path(GRAPH, "A", "F")

    print(f"递归 DFS 从 A 出发: {recursive_order}")
    print(f"迭代 DFS 从 A 出发: {iterative_order}")
    print(f"DFS 从 A 到 F 的路径: {path}")

    assert set(recursive_order) == set(GRAPH), "递归 DFS 应访问全部节点"
    assert set(iterative_order) == set(GRAPH), "迭代 DFS 应访问全部节点"
    assert path is not None and path[0] == "A" and path[-1] == "F", "应找到 A->F 路径"
    print("测试通过: 递归/迭代 DFS 均访问全部 6 个节点, 路径查找正常")
