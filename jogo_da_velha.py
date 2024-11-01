import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Velha")
        master.configure(bg="#f0e68c")  
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

        self.buttons = []
        for i in range(9):
            button = tk.Button(master, text=" ", font=("Arial", 30), width=5, height=2,
                               command=lambda i=i: self.play(i), bg="#fff", activebackground="#c0e0f0")
            button.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self.buttons.append(button)

        self.restart_button = tk.Button(master, text="Reiniciar", font=("Arial", 16),
                                         command=self.reset_game, bg="#ffcc00", activebackground="#ff9900")
        self.restart_button.grid(row=3, columnspan=3, pady=20)

    def play(self, index):
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]              
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
                return True
        return False

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ", bg="#fff")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
