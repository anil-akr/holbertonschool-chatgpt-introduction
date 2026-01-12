#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines_count = mines
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue  # ne pas compter la case elle-même
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # coordonnées invalides
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # on ne perd pas juste parce qu'on s'est trompé

        # déjà révélée
        if self.revealed[y][x]:
            return True

        # mine -> perdu
        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        # flood fill si 0 mine autour
        if self.count_mines_nearby(x, y) == 0:
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)

        return True

    def has_won(self):
        # Victoire si toutes les cases non-minées sont révélées
        revealed_count = sum(1 for row in self.revealed for cell in row if cell)
        safe_cells = (self.width * self.height) - self.mines_count
        return revealed_count == safe_cells

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Out of bounds. Try again.")
                    input("Press Enter to continue...")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.has_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()