# Visual Maze Solver

A Python-based visualization of the **Recursive Backtracking** algorithm. This tool demonstrates how a computer "thinks" while navigating through a maze and allows users to **custom-design their own layouts**.

## 🌟 Key Features
- **Algorithm Visualization**: Real-time display of path exploration and backtracking.
- **Customizable Maze Design**: Design your own maze by simply editing a text grid in the source code.
- **Auto-Detection**: Dynamically finds the Start (`s`) and Exit (`e`) points.

## 🛠 Prerequisites & Installation
Ensure you have **Python 3.x** installed. This project requires the `pygame` library for visualization.

### 1. Install Dependencies
Open your terminal or command prompt and run:
```bash
pip install pygame

#### 🛠 How to Customize Your Maze
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
