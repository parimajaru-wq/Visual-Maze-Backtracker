Visual Maze Solver
A Python-based visualization of the Recursive Backtracking (Depth-First Search) algorithm. This tool demonstrates how a computer "thinks" while navigating through a maze and allows users to custom-design their own layouts.

🌟 Key Features
Algorithm Visualization: Real-time display of path exploration and backtracking.

Customizable Maze Design: Design your own maze by simply editing a text grid in the source code.

Auto-Detection: Dynamically finds the Start (s) and Exit (e) points.

🛠 Prerequisites & Installation
Ensure you have Python 3.x installed. This project requires the pygame library.

1. Install Dependencies

Open your terminal and run:

pip install pygame
🚀 How to Run
Clone or download this repository to your local machine.

Ensure you have the main.py file in your project folder.

Run the application by typing the following command in your terminal:

python main.py
🎨 How to Customize Your Maze
You can decorate and design your own maze by modifying the scr list in main.py. Use the following symbols:

Design Symbols:

s : Start Point (Orange block)

e : Exit Point (Purple block)

b : Wall (Impassable blue blocks)

. : Path (White walkable spaces)

Example of a Custom Layout:

scr = [
    "bbbbbbbbbb",
    "s........b",
    "b.bbbbbb.b",
    "b......b.e",
    "bbbbbbbbbb"
]
