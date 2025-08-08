import tkinter as tk

ROWS = 6
COLS = 7
CELL_SIZE = 80
PLAYER_COLORS = {1: "red", 2: "yellow"}

class ConnectFour:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")
        self.current_player = 1
        self.board = [[0]*COLS for _ in range(ROWS)]
        self.canvas = tk.Canvas(master, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="blue")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_event)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x0, y0 = c*CELL_SIZE, r*CELL_SIZE
                color = PLAYER_COLORS.get(self.board[r][c], "white")
                self.canvas.create_oval(x0+5, y0+5, x0+CELL_SIZE-5, y0+CELL_SIZE-5, fill=color)

    def click_event(self, event):
        col = event.x // CELL_SIZE
        for row in reversed(range(ROWS)):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                self.draw_board()
                if self.check_win(row, col):
                    self.game_over(f"Player {self.current_player} wins!")
                elif all(self.board[0][c] != 0 for c in range(COLS)):
                    self.game_over("Draw!")
                else:
                    self.current_player = 2 if self.current_player == 1 else 1
                break

    def check_win(self, row, col):
        def count(delta_r, delta_c):
            r, c, cnt = row+delta_r, col+delta_c, 0
            while 0 <= r < ROWS and 0 <= c < COLS and self.board[r][c] == self.current_player:
                cnt += 1
                r += delta_r
                c += delta_c
            return cnt

        directions = [(1,0), (0,1), (1,1), (1,-1)]
        for dr, dc in directions:
            if count(dr, dc) + count(-dr, -dc) >= 3:
                return True
        return False

    def game_over(self, msg):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(COLS*CELL_SIZE//2, ROWS*CELL_SIZE//2, text=msg, fill="green", font=("Arial", 32))

if __name__ == "__main__":
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()
