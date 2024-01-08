import tkinter as tk

def create_winner_window(winner):
    winner_window = tk.Toplevel()
    winner_window.title("Game Over")
    if winner:
        winner_label = tk.Label(winner_window, text=f"{winner} wins!", font=("Arial", 20))
    else:
        winner_label = tk.Label(winner_window, text="It's a tie!", font=("Arial", 20))
    winner_label.pack(padx=20, pady=20)
    close_button = tk.Button(winner_window, text="Close", command=winner_window.destroy)
    close_button.pack(pady=10)

window = tk.Tk()
window.resizable(False, False)
window.title("TIC TAC TOE")

tk.Label(window, text="TIC TAC TOE", font=("Arial", 25)).pack()
status_label = tk.Label(window, text="X's turn ", font=("Arial", 15), bg="green", fg='snow')
status_label.pack(fill=tk.X)

def play_again():
    global current_chr
    current_chr = "X"
    for point in XO_points:
        point.button.configure(state=tk.NORMAL)
        point.reset()
    status_label.configure(text="X's turn")
    play_again_button.pack_forget()

play_again_button = tk.Button(window, text="Play Again", command=play_again)
play_again_button.pack()

play_area = tk.Frame(window, width=300, height=300, bg="white")
current_chr = "X"
XO_points = []
X_points = []
O_points = []

class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_chr
        if not self.value:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.value = current_chr
            if current_chr == "X":
                X_points.append(self)
                current_chr = "O"
                status_label.configure(text="O's turn")
            elif current_chr == "O":
                O_points.append(self)
                current_chr = "X"
                status_label.configure(text="X's turn")
            check_winner()

    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            X_points.remove(self)
        elif self.value == "O":
            O_points.remove(self)
        self.value = None

def check_winner():
    winning_combinations = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],
        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],
        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)],
    ]

    for combination in winning_combinations:
        values = [XO_points[x - 1 + (y - 1) * 3].value for x, y in combination]
        if all(v == "X" for v in values):
            show_winner("X")
            return
        elif all(v == "O" for v in values):
            show_winner("O")
            return

    # Check for a tie
    if all(point.value for point in XO_points):
        show_winner(None)

def show_winner(winner):
    status_label.configure(text=f"{winner} wins!" if winner else "It's a tie!")

    for point in XO_points:
        point.button.configure(state=tk.DISABLED)

    play_again_button.pack()

for x in range(1, 4):
    for y in range(1, 4):
        XO_points.append(XOPoint(x, y))
play_area.pack(pady=10, padx=10)
window.mainloop()
