# Conway's Game of Life

A Python implementation of Conway's Game of Life, a cellular automaton devised by John Conway. This project features an interactive visualizer built with Pygame, allowing users to simulate and manipulate grid-based cellular evolution. It demonstrates proficiency in 2D grid algorithms, state management with sets, file I/O, unit testing, and GUI development, making it a showcase piece for computational thinking and software design.

## Features

- **Interactive Pygame GUI**: Displays a grid where live cells are blue squares, with a gray grid on a black background.
- **Command-Line Arguments**: Customize grid size and speed with `--width` (default: 60), `--height` (default: 30), and `--fps` (default: 10).
- **Keyboard Controls**:
  - **Space**: Toggle play/pause for continuous simulation.
  - **N**: Advance one generation (single-step).
  - **C**: Clear the grid and reset generation count.
  - **R**: Randomly fill \~20% of cells.
  - **S**: Save the current pattern to `patterns.txt`.
  - **L**: Load a pattern from `patterns.txt`.
- **Pattern Persistence**: Save/load live cell coordinates to/from `patterns.txt` for reusable patterns like the Glider.
- **Polished UI**:
  - Status bar shows generation count, live cell count, and real-time FPS.
  - Displays control instructions: `Space: Play/Pause | N: Step | C: Clear | R: Random | S: Save | L: Load`.
  - Resizable window dynamically adjusts the grid while preserving valid cells.
  - Blue color scheme for live cells with smooth animations.
- **Unit Tests**: Tests for *Blinker* (period-2 oscillator) and *Glider* (diagonal movement) patterns using `pytest`.
- **Error Handling**: Gracefully handles invalid file inputs, out-of-bounds coordinates, and rapid user inputs.

## Installation

1. **Install Python**: Ensure Python 3.8+ is installed. Download from python.org if needed.
2. **Install Dependencies**: Run the following in your terminal:

   ```bash
   pip install pygame pytest
   ```
3. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/game-of-life.git
   cd game-of-life
   ```

## Usage

Run the game with default settings (60x30 grid, 10 FPS):

```bash
python life.py
```

Customize the grid and speed:

```bash
python life.py --width 80 --height 40 --fps 15
```

Run unit tests to verify the *Blinker* and *Glider* patterns:

```bash
pytest -q
```

### Controls

- **Space**: Play or pause the simulation.
- **N**: Step to the next generation.
- **C**: Clear all cells and reset generation to 0.
- **R**: Randomly populate \~20% of cells.
- **S**: Save the current pattern to `patterns.txt`.
- **L**: Load a pattern from `patterns.txt`.

## File Formats

- `patterns.txt`: Stores live cell coordinates (one per line, format: `x,y`). Example for a Glider:

  ```
  # Pattern: Glider
  1,0
  2,1
  0,2
  1,2
  2,2
  ```

## Demo

Watch the demo video *https://youtu.be/hakyxj8TJPM*

## Project Structure

- `life.py`: Core game logic, Pygame rendering, CLI parsing, and interactive controls.
- `test_life.py`: Unit tests for *Blinker* and *Glider* patterns using `pytest`.
- `README.md`: Project documentation.
- `patterns.txt`: Optional sample pattern file (generated when saving or provided manually).

## Challenges and Solutions

- **Performance**: Used a `set` of `(x, y)` coordinates for live cells instead of a 2D array, reducing memory usage and speeding up updates for sparse grids.
- **Window Resizing**: Implemented dynamic grid adjustment by recalculating dimensions and preserving valid cells, ensuring a seamless user experience.
- **Testing**: Added unit tests to validate the *Blinker* and *Glider* patterns, ensuring the core logic adheres to Game of Life rules.

## Future Enhancements

- **Mouse Interaction**: Allow users to toggle cells by clicking to create custom patterns.
- **Color Themes**: Support multiple color schemes for live cells and backgrounds.
- **Zoom and Pan**: Enable zooming and panning for large grids to explore complex patterns.

## Author

Built by \[G.Yeshwanth Reddy\] for Module 2 Capstone, May 2025.