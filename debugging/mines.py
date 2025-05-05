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
        if mines >= self.total_cells:
            raise ValueError("Too many mines! Must be fewer than total cells.")
        self.mines = set(random.sample(range(self.total_cells), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('    ' + ' '.join(f"{i:2}" for i in range(self.width)))
        print('   ' + '--' * self.width)
        for y in range(self.height):
            print(f"{y:2} |", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('* ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f"{count if count > 0 else ' '} ", end='')
                else:
                    print('. ', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal_cell(self, x, y):
        if self.revealed[y][x]:
            return True  # Already revealed
        if (y * self.width + x) in self.mines:
            return False  # Hit a mine

        # Reveal this cell
        self.revealed[y][x] = True

        # If no adjacent mines, reveal surrounding cells
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal_cell(nx, ny)
        return True

    def check_win(self):
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0 to {self.width - 1}): "))
                y = int(input(f"Enter y coordinate (0 to {self.height - 1}): "))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Please try again.")
                    input("Press Enter to continue...")
                    continue

                if not self.reveal_cell(x, y):
                    self.print_board(reveal=True)
                    print("💥 Game Over! You hit a mine.")
                    break

                if self.check_win():
                    self.print_board(reveal=True)
                    print("🏆 Congratulations! You cleared the field!")
                    break

            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
