# Pygame Maze Solver - Recursive Backtracking Visualization

A Python-based visualization of the **Recursive Backtracking (Depth-First Search)** algorithm. This tool not only solves mazes but also allows users to **custom-design their own maze layouts** easily.

## 🌟 Key Features
- **Customizable Maze Design**: Create your own maze by simply editing a text-based grid.
- **Auto-Detection**: Automatically identifies the Start (`s`) and Exit (`e`) points.
- **Backtracking Visualization**: Watch the algorithm explore paths and "erase" its trail when it hits a dead end.

## 🛠 How to Customize Your Maze
You can decorate and design your own maze by modifying the `scr` list in `main.py`. Use the following symbols:
- `s` : **Start Point** (The beginning of the journey)
- `e` : **Exit Point** (The goal to reach)
- `b` : **Wall** (Impassable blue blocks)
- `.` : **Path** (White walkable spaces)

Example of a custom layout:
```python
scr = [
    "bbbbbbbbbb",
    "s........b",
    "b.bbbbbb.b",
    "b......b.e",
    "bbbbbbbbbb"
]
