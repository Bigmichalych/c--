import pygame
import random
from queue import PriorityQueue

pygame.init()

# Константы для 10x10 стартового окна
START_GRID_SIZE = 10
START_WIDTH = 600
START_CELL_SIZE = START_WIDTH // START_GRID_SIZE

# Константы для 30x30 окна после Reset
LARGE_GRID_SIZE = 30
LARGE_WIDTH = 600
LARGE_CELL_SIZE = LARGE_WIDTH // LARGE_GRID_SIZE

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
GREY = (128, 128, 128)

class Cell:
    def __init__(self, row, col, cell_size):
        self.row = row
        self.col = col
        self.cell_size = cell_size
        self.x = col * cell_size
        self.y = row * cell_size
        self.color = WHITE
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_open(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.cell_size, self.cell_size))

    def update_neighbors(self, grid, grid_size):
        self.neighbors = []
        if self.row < grid_size - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < grid_size - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

def h(p1, p2):
    # Манхэттенское расстояние
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        if not current.is_start():
            current.make_path()
        draw()

def a_star_algorithm(draw, grid, start, end, grid_size):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {cell: float("inf") for row in grid for cell in row}
    g_score[start] = 0

    f_score = {cell: float("inf") for row in grid for cell in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False

def make_grid(grid_size, cell_size):
    grid = []
    for i in range(grid_size):
        grid.append([])
        for j in range(grid_size):
            cell = Cell(i, j, cell_size)
            grid[i].append(cell)
    return grid

def draw_grid_lines(win, grid_size, cell_size):
    for i in range(grid_size):
        pygame.draw.line(win, GREY, (0, i * cell_size), (grid_size * cell_size, i * cell_size))
        pygame.draw.line(win, GREY, (i * cell_size, 0), (i * cell_size, grid_size * cell_size))

def draw(win, grid, grid_size, cell_size):
    win.fill(WHITE)
    for row in grid:
        for cell in row:
            cell.draw(win)
    draw_grid_lines(win, grid_size, cell_size)
    pygame.display.update()

def generate_fixed_10x10_grid(grid):
    fixed_layout = [
        "1010011100",
        "0100001101",
        "1111101000",
        "0000100100",
        "1100000100",
        "1010011100",
        "0000000010",
        "0100010011",
        "0000100001",
        "1100000001",
    ]

    for row in grid:
        for cell in row:
            cell.reset()

    for r in range(len(fixed_layout)):
        for c in range(len(fixed_layout[r])):
            if fixed_layout[r][c] == "1":
                grid[r][c].make_barrier()

    start = grid[6][0]
    end = grid[9][8]

    start.make_start()
    end.make_end()

    return start, end

def generate_random_grid(grid, grid_size):
    for row in grid:
        for cell in row:
            cell.reset()

    start_row, start_col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
    end_row, end_col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
    while (start_row, start_col) == (end_row, end_col):
        end_row, end_col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)

    start = grid[start_row][start_col]
    end = grid[end_row][end_col]

    start.make_start()
    end.make_end()

    for _ in range(int(grid_size * grid_size * 0.2)):
        r, c = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        cell = grid[r][c]
        if not cell.is_start() and not cell.is_end():
            cell.make_barrier()

    return start, end

def main():
    grid_size = START_GRID_SIZE
    cell_size = START_CELL_SIZE
    win = pygame.display.set_mode((START_WIDTH, START_WIDTH))
    pygame.display.set_caption("A*")

    grid = make_grid(grid_size, cell_size)
    start, end = generate_fixed_10x10_grid(grid)
    for row in grid:
        for cell in row:
            cell.update_neighbors(grid, grid_size)

    started = False
    running = True

    while running:
        draw(win, grid, grid_size, cell_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid_size = LARGE_GRID_SIZE
                    cell_size = LARGE_CELL_SIZE
                    win = pygame.display.set_mode((LARGE_WIDTH, LARGE_WIDTH))
                    pygame.display.set_caption("A*")

                    grid = make_grid(grid_size, cell_size)
                    start, end = generate_random_grid(grid, grid_size)
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid, grid_size)

                    started = False

                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for cell in row:
                            cell.update_neighbors(grid, grid_size)
                    started = True
                    a_star_algorithm(lambda: draw(win, grid, grid_size, cell_size), grid, start, end, grid_size)

    pygame.quit()

if __name__ == "__main__":
    main()
