# Classic Algorithms — 经典算法

两个经典算法的 Python 实现, 均可直接运行并自带断言测试。

## 目录结构

```
.
├── eight_queens/
│   └── eight_queens.py   # 八皇后问题 (回溯法, 全部 92 种解)
└── dfs/
    └── dfs.py            # 深度优先搜索 (递归 + 迭代 + 路径查找)
```

## 运行与测试

```bash
python3 eight_queens/eight_queens.py
python3 dfs/dfs.py
```

- `eight_queens.py` 输出 92 种解, 并打印前 3 种棋盘。
- `dfs.py` 输出递归 / 迭代 DFS 的访问顺序, 以及 A 到 F 的一条路径。
