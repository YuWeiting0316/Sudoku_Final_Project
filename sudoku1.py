import random
import tkinter as tk
from tkinter import messagebox



def is_valid(board, row, col, val):
    """
    Checks if a value is valid at a specific position on the Sudoku board.

    Args:
        board (list[list[int]]): The Sudoku board.
        row (int): Row index.
        col (int): Column index.
        val (int): The value to check.

    Returns:
        bool: True if the value is valid, False otherwise.
    """
    # check val is valid for location board[row][col] or not
    for i in range(9):
        # check if val exist in row or col
        if board[row][i] == val or board[i][col] == val:
            return False
    # check val exist in 3*3 box or not
    rx = 3 * (row // 3)
    cx = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[rx + i][cx + j] == val:
                return False
    return True

def generate_sudoku_solution():
    """
    Generates a complete Sudoku solution.

    Returns:
        list[list[int]]: A 9x9 completed Sudoku board.
    """
    #generate sudoku solution
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    return board

def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using Depth-First Search (DFS).

    Args:
        board (list[list[int]]): A 9x9 Sudoku board.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    # use dfs to solve sudoku
    for row in range(9):
        for col in range(9):
            # if board[row][col] is not filled
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for val in numbers:
                    if is_valid(board, row, col, val):
                        board[row][col] = val
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                # can not find solution
                return False
    return True

def generate_challenge(board, visible):
    """
    generate game challenge
    :param board: 9*9 game board
    :param visible: integer which is the number of visible cells in the game board
    :return: incomplete board
    """
    challenge = [x[:] for x in board]
    locations = [(x, y) for x in range(9) for y in range(9)]
    random.shuffle(locations)
    for i in range(81 - visible):
        x, y = locations.pop()
        # set location (x, y) to not visible
        challenge[x][y] = 0
    return challenge


class SudokuGame:
    """
    A class representing the Sudoku game with a GUI interface.
    """
    def __init__(self, root):
        """
        Initializes the Sudoku game GUI and its logic.

        Args:
            root (tk.Tk): The root window for the GUI.
        """
        self.root = root
        self.root.title("Sudoku Game")
        # init visible cell number in the game board
        self.visible = 30
        self.complete_board = generate_sudoku_solution()
        self.incomplete_board = generate_challenge(self.complete_board, self.visible)
        # init tkinter entry for game board
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.initGame()

    def initGame(self):
        """
        Sets up the Sudoku game GUI.
        """
        for x in range(9):
            for y in range(9):
                entry = tk.Entry(self.root, font=('Arial', 16), width=2,  justify='center')
                entry.grid(row=x, column=y, padx=5, pady=5)
                # if this cell is visible
                if self.incomplete_board[x][y] != 0:
                    entry.insert(0, str(self.incomplete_board[x][y]))
                    # set the entry to disabled, the value can not be modified
                    entry.config(state='disabled', disabledbackground="lightgrey", disabledforeground="black")
                self.entries[x][y] = entry

        solveButton = tk.Button(self.root, text="SOLVE", command=self.solve, font=("Arial", 14), width=10)
        solveButton.grid(row=9, column=0, columnspan=3, pady=10)

        resetButton = tk.Button(self.root, text="RESET", command=self.reset, font=("Arial", 14), width=10)
        resetButton.grid(row=9, column=3, columnspan=3, pady=10)

        validateButton = tk.Button(self.root, text="VALIDATE", command=self.validate, font=("Arial", 14), width=10)
        validateButton.grid(row=9, column=6, columnspan=3, pady=10)

    def solve(self):
        # show solution
        solution = self.complete_board
        for x in range(9):
            for y in range(9):
                self.entries[x][y].config(state='normal')
                self.entries[x][y].delete(0, tk.END)
                if solution[x][y] != 0:
                    self.entries[x][y].insert(0, str(solution[x][y]))
                    self.entries[x][y].config(state='disabled', disabledbackground="lightgrey", disabledforeground="black")


    def reset(self):
        # new sudoku game
        self.complete_board = generate_sudoku_solution()
        self.incomplete_board = generate_challenge(self.complete_board, self.visible)
        for x in range(9):
            for y in range(9):
                entry = self.entries[x][y]
                entry.config(state='normal')
                entry.delete(0, tk.END)
                if self.incomplete_board[x][y] != 0:
                    entry.insert(0, str(self.incomplete_board[x][y]))
                    entry.config(state='disabled', disabledbackground="lightgrey", disabledforeground="black")

    def validate(self):
        """
        Validates the user-provided solution against the complete Sudoku board.
        """
        # validate sudoku
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        for x in range(9):
            for y in range(9):
                val = self.entries[x][y].get()
                self.board[x][y] = int(val) if val.isdigit() else 0
        if self.board == self.complete_board:
            messagebox.showinfo("Congratulation", "Your solution is correct!")
        else:
            messagebox.showerror("ERROR", "Your solution has error, try again!")




if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()
