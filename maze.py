import pygame as pg
import sys

sys.setrecursionlimit(5000)
pg.init()
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption('Visual Maze Solver')
clock = pg.time.Clock()

size = 40
print(size)
# --- CUSTOMIZE YOUR MAZE HERE ---
# 's' = Start, 'e' = Exit, 'b' = Wall, '.' = Path
scr = [
    "bsbbbbbbbbbbbbbbbb",
    "b...b...b....bb..b",
    "b.b...b...b.bb.b.b",
    "b.b.b.bb.bbbb..b.b",
    "bb..b.......b.b..b",
    "bb..bbbbbbb...b.bb",
    "b...b.....b.b....b",
    "b.b...bbb.b.b.b.bb",
    "b.bbbbb.b.bbbbb..b",
    "b.......b.....b.bb",
    "bbbbbbbbbbbbbebbbb"
]

h = len(scr)
w = len(scr[0])
aa = []
start = (0, 0)
end = (0, 0)

for r in range(h):
    for c in range(w):
        if scr[r][c] == 's':
            start = (c, r)
        elif scr[r][c] == 'e':
            end = (c, r)
print(start,end)

def maze():
    for i in range(h):
        for j in range(w):
            cc = scr[i][j]
            x2 = j
            y2 = i
            rect = (x2 * size, y2 * size, size, size)
            if cc == 'b':
                pg.draw.rect(screen, 'Blue', rect)
            elif cc == 'e':
                pg.draw.rect(screen, 'Purple', rect)
            else:
                pg.draw.rect(screen, 'White', rect)

def grid():
    for y in range(h):
        for x in range(w):
            pg.draw.rect(screen, 'Black', (x * size, y * size, size, size), 1)

def walk(x, y):
    if 0 <= x < w and 0 <= y < h and (scr[y][x] == '.' or scr[y][x] == 'e' or scr[y][x] == 's'):
        if x == end[0] and y == end[1]:
            aa.append([x, y, 'finish'])
        else:
            cc = list(scr[y])
            cc[x]='r'
            scr[y] = "".join(cc)
            aa.append([x, y, scr[y][x]])
            walk(x+1,y)
            walk(x,y+1)
            walk(x-1,y)
            walk(x,y-1)
            
            cc[x]='.'
            scr[y]="".join(cc)
            aa.append([x, y, scr[y][x]])

walk(start[0], start[1])

co = 0
bb = 0
for i in range(len(aa)):
    if aa[i][2] == 'finish':
        co = i
        break

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
        else :
            pg.draw.rect(screen, 'Red', (x3 * size, y3 * size, size, size))
    bb += 1
    grid()
    pg.display.update()
    clock.tick(20)
