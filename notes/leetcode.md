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



### 📌 Interview Cheat Sheet: Clone Graph (LeetCode 133)

---

### 🧠 Core Concept & Strategy

* **The Problem:** Given a reference to a node in a connected, undirected graph, return a **deep copy** (clone) of the graph. Each node contains a value (`int`) and a list of its neighbors (`List[Node]`).
* **The Blueprint:** A deep copy means creating entirely new memory addresses for every single node and replicating their structural connections perfectly.
* **The Hash Map Anchor:** Graphs often contain **cycles** (e.g., Node 1 connects to Node 2, which connects back to Node 1). To avoid infinite loops and duplicate node allocations, maintain a hash map mapping: `Original Node -> Cloned Node`.

---

### 💻 Production-Grade Implementation (Iterative BFS)

```python
from collections import deque
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 1. Edge Case Guard Clause: Handle empty inputs safely
        if not node:
            return None
            
        # 2. Tracking Map: Key = Original Node Object, Value = Cloned Node Object
        clones = {}
        
        # Initialize BFS Queue with the root original node
        que = deque([node])
        
        # Clone the root node and register it in the tracking map
        clones[node] = Node(node.val)
        
        # 3. BFS Traversal Loop
        while que:
            curr = que.popleft()
            
            # Explore all neighbors of the current original node
            for neighbor in curr.neighbors:
                
                # If this neighbor has never been seen before, clone its shell
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    que.append(neighbor)
                
                # Critical Line: Link the cloned current node to the cloned neighbor node
                clones[curr].neighbors.append(clones[neighbor])
                
        return clones[node]

```

---

### 📊 Complexity Analysis

* **Time Complexity:** $\mathcal{O}(V + E)$
* *Why:* $V$ represents the number of vertices (nodes) and $E$ represents the number of edges. The BFS queue guarantees we visit every individual node exactly once, and the inner loop processes every structural edge connection exactly once.


* **Space Complexity:** $\mathcal{O}(V)$
* *Why:* The `clones` hash map scales linearly, storing exactly $V$ key-value pairs. Additionally, the BFS queue holds at most $V$ elements in the worst-case scenario (such as a fully connected or star-graph layout).



---

### ⚠️ Top 4 Interview Pitfalls to Memorize

1. **The `NoneType` Crash:** Forgetting an explicit `if not node: return None` check at the start. If an empty graph `[]` is given, trying to access `node.val` immediately causes a production crash.
2. **The "Shallow Copy" Shortcut:** Accidentally typing `clones[curr].neighbors = curr.neighbors`. This forces your new graph to look directly at the *old* graph's memory addresses, failing the core interview requirement of a structural deep copy.
3. **Passing Arrays into Constructors:** Writing `Node(neighbor.neighbors)` or `Node(node)` inside the object initialization. The `Node` constructor expects a primitive **integer** (`val`), not a collection layout. Passing a list breaks internal serializations with a `TypeError: unhashable type: 'list'`.
4. **Premature Queue Insertion:** Appending items to the BFS queue *outside* of the `if neighbor not in clones` condition block. If you do this, you will process the same node multiple times, drastically reducing performance and risking cycle loops.

---

### 🚀 Follow-Up Scenarios (The FAANG Level-Up)

* **Q: Why use BFS over recursive DFS for this production problem?**
* *A:* "While DFS yields an identical time complexity, a deep or highly linear graph structure can easily run out of system call-stack space. Switching to an iterative BFS safely shifts memory allocation overhead onto the heap via a manual data structure (`deque`), making it resilient against `StackOverflowError` exceptions."


* **Q: How does the map prevent duplicate node clones when multi-connected nodes appear?**
* *A:* "The hash map acts as a source of truth. If Node A and Node B both share an edge with Node C, the first node to discover Node C will allocate it in `clones`. When the second node encounters it, the lookup condition `if neighbor not in clones` evaluates to `False`, preventing a redundant object instantiation."
