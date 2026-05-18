### 📌 Interview Cheat Sheet: Number of Islands (LeetCode 200)

---

### 🧠 Core Concept & Strategy

* **The Problem:** Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the number of distinct islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.
* **The Blueprint:** Treat the 2D grid as an **unweighted graph** where each cell is a node, and edges exist between horizontally/vertically adjacent `'1'`s. An island is a **Connected Component**.
* **The "Sink the Island" Technique:**
1. Scan the grid using a nested loop.
2. When you hit a `'1'`, increment your `island_count`.
3. Immediately launch a **Depth-First Search (DFS)** from that cell.
4. During DFS, mutate the visited land from `'1'` to `'0'` (sinking it) so it isn't evaluated again.



---

### 💻 Production-Grade Implementation (Python)

```python
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: Empty grid
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        # Scan the entire matrix
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    # Start DFS to clear out this specific connected island
                    self._sink_island_dfs(grid, r, c, rows, cols)
                    
        return island_count

    def _sink_island_dfs(self, grid: List[List[str]], r: int, c: int, rows: int, cols: int) -> None:
        # Base Case: Out of bounds OR hitting water ('0')
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return
            
        # Action: "Sink" the land to eliminate the need for a separate 'visited' set
        grid[r][c] = "0"
        
        # Recursive Step: Explore all 4 cardinal directions
        self._sink_island_dfs(grid, r + 1, c, rows, cols)  # Down
        self._sink_island_dfs(grid, r - 1, c, rows, cols)  # Up
        self._sink_island_dfs(grid, r, c + 1, rows, cols)  # Right
        self._sink_island_dfs(grid, r, c - 1, rows, cols)  # Left

```

---

### 📊 Complexity Analysis

* **Time Complexity:** $\mathcal{O}(M \times N)$
* *Why:* $M$ is rows, $N$ is columns. We scan every cell using the nested loop. The DFS visits each land cell exactly once because it drops to `'0'` immediately. Total work per cell is constant $\mathcal{O}(1)$.


* **Space Complexity:** $\mathcal{O}(M \times N)$
* *Why:* In the absolute worst-case scenario (e.g., the entire grid consists of land), the implicit recursion stack of the DFS can grow to the total number of cells, resulting in $\mathcal{O}(M \times N)$ memory.



---

### ⚠️ Top 4 Interview Pitfalls to Memorize

1. **The "String" Gotcha:** The input matrix contains strings (`"1"` and `"0"`), **not** integers (`1` and `0`). Comparing `grid[r][c] == 1` will break silently.
2. **Boundary Evaluation Order:** In your base case condition, you *must* check if `r` and `c` are out of bounds **before** attempting to read `grid[r][c]`. Swapping the order results in an `IndexOutOfBoundsException`.
3. **Premature Recursion:** Always alter `grid[r][c] = "0"` *before* invoking the 4 recursive directions. If you recurse first, the algorithm will instantly fall into a cycle and cause a stack overflow.
4. **Redundant Object Overhead:** Do not call `len(grid)` inside the recursive helper function. Calculate `rows` and `cols` once in the primary function and pass them down. This shows a micro-optimization mindset expected at L4/L5 levels.

---

### 🚀 Follow-Up Scenarios (The FAANG Level-Up)

* **Q: What if the grid is immutable / read-only?**
* *A:* "If mutating the input is prohibited due to threading or data integrity constraints, I would introduce a 2D boolean array or a hash set named `visited` to store coordinates `(r, c)`. The time complexity stays $\mathcal{O}(M \times N)$, and space complexity remains explicitly $\mathcal{O}(M \times N)$."


* **Q: Why choose DFS over BFS here?**
* *A:* "Both yield identical asymptotic time complexities. However, DFS is cleaner to write under interview conditions since it relies on the execution stack rather than explicitly managing an external queue (`collections.deque`), reducing the risk of syntax bugs."
