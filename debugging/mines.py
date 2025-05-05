#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mine_positions = set(random.sample(range(self.total_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_revealed = 0
        self.mines = mines

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2} ', end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    idx = y * self.width + x
                    if idx in self.mine_positions:
                        print(' *', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f' {count}' if count > 0 else '  ', end='')
                else:
                    print(' .', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    idx = ny * self.width + nx
                    if idx in self.mine_positions:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # Ignore clicks outside board

        if self.revealed[y][x]:
            return True  # Already revealed

        idx = y * self.width + x
        if idx in self.mine_positions:
            return False

        self.revealed[y][x] = True
        self.total_revealed += 1

        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    self.reveal(x + dx, y + dy)

        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("💣 Game Over! You hit a mine.")
                    break
                if self.total_revealed == self.total_cells - self.mines:
                    self.print_board(reveal=True)
                    print("🎉 Congratulations! You won!")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
