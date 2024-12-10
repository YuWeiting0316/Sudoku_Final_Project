# Interactive Sudoku Solver and Validator


## Project Overview
This Python-based project provides an interactive Sudoku application, allowing users to:

- Solve puzzles interactively.
- Validate their solutions.
- Automatically generate and solve Sudoku puzzles.

The application is implemented with Tkinter for GUI and depth-first search (DFS) for generating solutions.


## Features
1.Puzzle Generation:Puzzle Generation:

- Generates random, solvable 9x9 Sudoku puzzles using DFS.

2.Interactive GUI:

- Intuitive Tkinter-based grid for user interaction.
- Buttons for solving, resetting, and validating solutions.

3.Solution Validation:

- Verifies the correctness of user-provided solutions.

4.Automatic Solving:

- Automatically solves puzzles with a single button click.

## Installation

PrerequisitesPrerequisites
- Python 3.x- Python 3.x
- Tkinter (bundled with most Python installations).

## Usage

1.Run the program:

python sudoku.py

Use the GUI to:
- Solve puzzles by filling in the grid.
- Validate your solution using the "Validate" button.
- Generate a new puzzle with "Reset".
- Get a complete solution using "Solve".

## How It Works
- Grid Interaction: Users can fill cells directly by clicking on them. Disabled cells contain pre-filled values.

- Validation: The "Validate" button checks if the user's solution matches the correct solution.

- Puzzle Reset: The "Reset" button generates a new random puzzle with a predefined number of visible cells.

## Code Structure

- sudoku.py: Main file containing the logic and GUI implementation.

## Acknowledgments

- Sudoku logic inspired by puzzle-solving algorithms.
- GUI framework provided by Python’s Tkinter library.




  
