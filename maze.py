import pygame as pg
import sys

# Increase recursion depth for deep maze exploration
sys.setrecursionlimit(5000)
pg.init()
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption('Visual Maze Solver')
clock = pg.time.Clock()

size = 40

# --- CUSTOMIZE YOUR MAZE HERE ---
# 's' = Start, 'e' = Exit, 'b' = Wall, '.' = Path
scr = [
    "bsbbbbbbbbbbbbbbbb",
    "b...b...b..b..b.bb",
    "b.b...b...b.b.b..b",
    "b.b.b.bb.bbbb.bb.b",
    "b...b.......b.b..b",
    "bb.bbbbbbbb...b.bb",
    "b...b.....b.bb...b",
    "b.b...bbb.b.b.b.bb",
    "b.bbbbb.b.bbbbb..b",
    "b.......b.....b.bb",
    "bbbbbbbbbbbbbebbbb"
]

h = len(scr)
w = len(scr[0])
aa = []
start_pos = (0, 0)
end_pos = (0, 0)

# Auto-scan for start and end positions
for r in range(h):
    for c in range(w):
        if scr[r][c] == 's':
            start_pos = (c, r)
        elif scr[r][c] == 'e':
            end_pos = (c, r)

def maze():
    for i in range(h):
        for j in range(w):
            char = scr[i][j]
            rect = (j * size, i * size, size, size)
            if char == 'b':
                pg.draw.rect(screen, 'Blue', rect)
            elif char == 's':
                pg.draw.rect(screen, 'Orange', rect)
            elif char == 'e':
                pg.draw.rect(screen, 'Purple', rect)
            else:
                pg.draw.rect(screen, 'White', rect)

def grid():
    for y in range(h):
        for x in range(w):
            pg.draw.rect(screen, 'Black', (x * size, y * size, size, size), 1)

def walk(x, y):
    if 0 <= x < w and 0 <= y < h:
        char = scr[y][x]
        if x == end_pos[0] and y == end_pos[1]:
            aa.append([x, y, 'finish'])
            return True
        if char == '.' or char == 's':
            temp_list = list(scr[y])
            temp_list[x] = 'r'
            scr[y] = "".join(temp_list)
            aa.append([x, y, 'r'])
            if (walk(x + 1, y) or walk(x - 1, y) or 
                walk(x, y + 1) or walk(x, y - 1)):
                return True
            # Backtracking: Mark as failed path
            temp_list = list(scr[y])
            temp_list[x] = '.' 
            scr[y] = "".join(temp_list)
            aa.append([x, y, '.'])
    return False

walk(start_pos[0], start_pos[1])

co = -1
for i in range(len(aa)):
    if aa[i][2] == 'finish':
        co = i
        break

bb = 0
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    maze() 
    if bb <= co and bb < len(aa):
        x3, y3, state = aa[bb][0], aa[bb][1], aa[bb][2]
        if state == 'r':
            pg.draw.rect(screen, 'Green', (x3 * size, y3 * size, size, size))
        elif state == '.':
            pg.draw.rect(screen, 'White', (x3 * size, y3 * size, size, size))
        elif state == 'finish':
            pg.draw.rect(screen, 'Red', (x3 * size, y3 * size, size, size))
        bb += 1
    grid()
    pg.display.update()
    clock.tick(20)