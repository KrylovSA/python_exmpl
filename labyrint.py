import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

#  возможный следующий ход , с учетом ранее открытых точек
def next_step(col, row: int, direction: str, is_not_explored_only: bool) -> [int, int, bool]:
    col_moved = col
    row_moved = row
    moved = False
    global maze
    if direction == 'LEFT':
        if col > 0:
            if maze[row][col - 1] in available_pnt:
                col_moved = col - 1
                moved = True
    elif direction == 'UP':
        if row > 0:
            if maze[row - 1][col] in available_pnt:
                row_moved = row - 1
                moved = True
    elif direction == 'RIGHT':
        if col < (c - 1):
            if maze[row][col + 1] in available_pnt:
                col_moved = col + 1
                moved = True
    elif direction == 'DOWN':
        if row < (r - 1):
            if maze[row + 1][col] in available_pnt:
                row_moved = row + 1
                moved = True
    if is_not_explored_only:
        if [col_moved, row_moved] in explored:
            moved = False
            col_moved = col
            row_moved = row
    return [col_moved, row_moved, moved]


# Поиск командного центра (проход по точкам без конкретной цели , просто открываем лабиринт)
def explore_maze(col, row: int) -> str:
    moved: bool
    col_moved = col
    row_moved = row
    global prev_point
   
    for direction in directions:
        [col_moved, row_moved, moved] = next_step(col, row, direction, True)
        if moved:
            return direction
    for direction in directions:
        [col_moved, row_moved, moved] = next_step(col, row, direction, False)
        if moved and [col_moved, row_moved] != prev_point:
            prev_point = [col, row]    
            return direction


# Поиск пути к заданой точке (target_col, target_row)
def find_path(col, row, target_col, target_row: int, path: [], moves_directions: [], lvl) -> bool:
    moved: bool
    ret: bool = False
    global way_directions
    global path_lenght
    col_moved = col
    row_moved = row
    lvl += 1
    if (col == target_col) and (row == target_row):
        if (len(path) < path_lenght) or (path_lenght == -1):  # нашли более краткий путь к target
            way_directions = moves_directions  # последовательность шагов
            path_lenght = len(path)
        return True
    for direction in directions:
        [col_moved, row_moved, moved] = next_step(col, row, direction, False)
        if moved:
            if [col_moved,row_moved] in path:
                continue
            else:
                _path = path.copy()
                _path.append([col_moved, row_moved])
                _moves_directions = moves_directions.copy()
                _moves_directions.append(direction)
                ret = ret or find_path(col_moved, row_moved, target_col, target_row, _path, _moves_directions, lvl)
    return ret


# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]
command_col: int = -1
command_row: int = -1
start_col: int = -1
start_row: int = -1
kr: int
kc: int
maze = []
explored = []
phase: int = 0  # 0 - ищем КЦ , 1 - идем к КЦ, 2 - идем к исходной точке
directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
way_directions = []
path_lenght: int
n_step: int = 0
way_found: bool = False
available_pnt = ['.', 'C', 'T']
prev_point = [-1,-1]

# game loop
while True:
    # kr: row where Rick is located.
    # kc: column where Rick is located.
    kr, kc = [int(i) for i in input().split()]
    if start_col == -1:        
        start_col = kc
        start_row = kr
    if not [kc, kr] in explored:
        explored.append([kc, kr])
    maze = []
    for i in range(r):
        line = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        maze.append(list(line))
        if phase == 0:
            if line.find('C') >= 0:  # Если нашли контрольный центр, сохраняем координаты
                command_col = line.find('C')
                command_row = i
                phase = 1
                way_found = False

    if phase == 1:
        if (kr == command_row) and (kc == command_col):  # Пришли в контрольный центр , идем обратно
            phase = 2
            way_found = False

    if phase == 0:
        print(explore_maze(kc, kr))
    elif phase == 1:
        if not way_found:
            path_lenght = -1
            way_found = find_path(kc, kr, command_col, command_row, [[kc, kr]], [], 0)
            n_step = 0
        print(way_directions[n_step])
        n_step += 1
    else:
        if not way_found:
            path_lenght = -1
            way_found = find_path(kc, kr, start_col, start_row, [[kc, kr]], [], 0)
            n_step = 0
        print(way_directions[n_step])
        n_step += 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Rick's next move (UP DOWN LEFT or RIGHT).
