import argparse
import pygame
import sys
import random
import os
from typing import Set, Tuple
import time

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (50, 50, 200)
CELL_SIZE = 20
FONT_SIZE = 24

class GameOfLife:
    def __init__(self, width: int, height: int, fps: int):
        self.width = width
        self.height = height
        self.fps = fps
        self.live_cells: Set[Tuple[int, int]] = set()
        self.running = False
        self.generation = 0
        pygame.init()
        self.screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE + 50), pygame.RESIZABLE)
        pygame.display.set_caption("Conway's Game of Life")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)
        self.last_update = time.time()

    def count_neighbors(self, x: int, y: int) -> int:
        """Count live neighbors for a cell."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) in self.live_cells:
                    count += 1
        return count

    def next_gen(self) -> Set[Tuple[int, int]]:
        """Compute the next generation."""
        new_live_cells = set()
        # Check all live cells and their neighbors
        candidates = set(self.live_cells)
        for x, y in self.live_cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        candidates.add((nx, ny))

        for x, y in candidates:
            neighbors = self.count_neighbors(x, y)
            if (x, y) in self.live_cells:
                if neighbors in [2, 3]:
                    new_live_cells.add((x, y))
            else:
                if neighbors == 3:
                    new_live_cells.add((x, y))
        return new_live_cells

    def randomize(self):
        """Fill the board with random live cells (20% density)."""
        self.live_cells.clear()
        self.generation = 0
        for x in range(self.width):
            for y in range(self.height):
                if random.random() < 0.2:
                    self.live_cells.add((x, y))

    def clear(self):
        """Clear all live cells."""
        self.live_cells.clear()
        self.generation = 0
        self.running = False

    def save_pattern(self, filename: str = "patterns.txt"):
        """Save live cells to a file."""
        with open(filename, "w") as f:
            f.write("# Pattern: Custom\n")
            for x, y in sorted(self.live_cells):
                f.write(f"{x},{y}\n")

    def load_pattern(self, filename: str = "patterns.txt"):
        """Load live cells from a file."""
        self.live_cells.clear()
        self.generation = 0
        self.running = False
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    if line.startswith("#"):
                        continue
                    try:
                        x, y = map(int, line.strip().split(","))
                        if 0 <= x < self.width and 0 <= ny < self.height:
                            self.live_cells.add((x, y))
                    except ValueError:
                        continue

    def draw(self):
        """Draw the grid and UI."""
        self.screen.fill(BLACK)
        # Draw grid
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if (x, y) in self.live_cells:
                    pygame.draw.rect(self.screen, BLUE, rect)
                pygame.draw.rect(self.screen, GRAY, rect, 1)

        # Draw status bar
        status = f"Gen: {self.generation} | Live: {len(self.live_cells)} | FPS: {int(self.clock.get_fps())}"
        controls = "Space: Play/Pause | N: Step | C: Clear | R: Random | S: Save | L: Load"
        status_text = self.font.render(status, True, WHITE)
        controls_text = self.font.render(controls, True, WHITE)
        self.screen.blit(status_text, (10, self.height * CELL_SIZE + 10))
        self.screen.blit(controls_text, (10, self.height * CELL_SIZE + 30))
        pygame.display.flip()

    def handle_resize(self, event):
        """Handle window resize."""
        new_width = max(20, event.w // CELL_SIZE)
        new_height = max(20, (event.h - 50) // CELL_SIZE)
        self.width = new_width
        self.height = new_height
        self.screen = pygame.display.set_mode((self.width * CELL_SIZE, self.height * CELL_SIZE + 50), pygame.RESIZABLE)
        # Remove cells outside new bounds
        self.live_cells = {(x, y) for x, y in self.live_cells if 0 <= x < self.width and 0 <= y < self.height}

    def run(self):
        """Main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = not self.running
                    elif event.key == pygame.K_n:
                        self.live_cells = self.next_gen()
                        self.generation += 1
                    elif event.key == pygame.K_c:
                        self.clear()
                    elif event.key == pygame.K_r:
                        self.randomize()
                    elif event.key == pygame.K_s:
                        self.save_pattern()
                    elif event.key == pygame.K_l:
                        self.load_pattern()
                elif event.type == pygame.VIDEORESIZE:
                    self.handle_resize(event)

            if self.running and time.time() - self.last_update >= 1 / self.fps:
                self.live_cells = self.next_gen()
                self.generation += 1
                self.last_update = time.time()

            self.draw()
            self.clock.tick(self.fps)

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("--width", type=int, default=60, help="Grid width")
    parser.add_argument("--height", type=int, default=30, help="Grid height")
    parser.add_argument("--fps", type=int, default=10, help="Frames per second")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    game = GameOfLife(args.width, args.height, args.fps)
    game.run()