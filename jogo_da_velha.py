import tkinter as tk
from tkinter import messagebox, colorchooser
import random

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.master.configure(background="#f0f0f0")

        self.tabuleiro_size = 3  # Tamanho padrão do tabuleiro
        self.tabuleiro = [[" " for _ in range(self.tabuleiro_size)] for _ in range(self.tabuleiro_size)]
        self.current_player = "X"
        self.game_over = False
        self.board_color = self.choose_board_color()
        self.game_mode = tk.StringVar()
        self.game_mode.set("Jogador vs. Computador")

        self.buttons = []
        for i in range(self.tabuleiro_size):
            for j in range(self.tabuleiro_size):
                button = tk.Button(master, text=" ", font=("Arial", 24, "bold"), width=8, height=3,
                                   command=lambda i=i, j=j: self.fazer_jogada(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                button.config(bg=self.board_color)
                self.buttons.append(button)

        self.reset_button = tk.Button(master, text="Reiniciar", font=("Arial", 14, "bold"),
                                      command=self.reset_game, bg="#ffcccc", fg="#000000")
        self.reset_button.grid(row=self.tabuleiro_size, column=0, columnspan=self.tabuleiro_size // 2, padx=5, pady=5)

        self.mode_label = tk.Label(master, text="Modo de Jogo:", font=("Arial", 12), bg="#f0f0f0")
        self.mode_label.grid(row=self.tabuleiro_size + 1, column=0, padx=5, pady=5)

        self.player_vs_player_button = tk.Radiobutton(master, text="Jogador vs. Jogador", variable=self.game_mode,
                                                      value="Jogador vs. Jogador", font=("Arial", 12), bg="#f0f0f0", selectcolor="#f0f0f0",
                                                      command=self.start_game)
        self.player_vs_player_button.grid(row=self.tabuleiro_size + 1, column=1, padx=5, pady=5)

        self.player_vs_computer_button = tk.Radiobutton(master, text="Jogador vs. Computador", variable=self.game_mode,
                                                        value="Jogador vs. Computador", font=("Arial", 12), bg="#f0f0f0", selectcolor="#f0f0f0",
                                                        command=self.start_game)
        self.player_vs_computer_button.grid(row=self.tabuleiro_size + 1, column=2, padx=5, pady=5)

    def start_game(self):
        """Inicia o jogo automaticamente quando o modo de jogo é alterado."""
        if self.game_mode.get() == "Jogador vs. Computador" and self.current_player == "O":
            self.ai_move()

    def fazer_jogada(self, row, col):
        """Faz uma jogada."""
        if not self.game_over and self.tabuleiro[row][col] == " ":
            self.tabuleiro[row][col] = self.current_player
            self.buttons[row * self.tabuleiro_size + col].config(text=self.current_player, state="disabled")
            if self.check_win(self.current_player):
                messagebox.showinfo("Fim do Jogo", f"{self.current_player} venceu!")
                self.game_over = True
            elif self.check_tie():
                messagebox.showinfo("Fim do Jogo", "O jogo terminou em empate!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O" and self.game_mode.get() == "Jogador vs. Computador":
                    self.ai_move()

    def ai_move(self):
        """Faz uma jogada da IA."""
        free_positions = [(i, j) for i in range(self.tabuleiro_size) for j in range(self.tabuleiro_size)
                          if self.tabuleiro[i][j] == " "]
        move = random.choice(free_positions)
        self.tabuleiro[move[0]][move[1]] = self.current_player
        self.buttons[move[0] * self.tabuleiro_size + move[1]].config(text=self.current_player, state="disabled")
        if self.check_win(self.current_player):
            messagebox.showinfo("Fim do Jogo", f"{self.current_player} venceu!")
            self.game_over = True
        elif self.check_tie():
            messagebox.showinfo("Fim do Jogo", "O jogo terminou em empate!")
            self.game_over = True
        else:
            self.current_player = "X"

    def reset_game(self):
        """Reinicia o jogo."""
        self.tabuleiro = [[" " for _ in range(self.tabuleiro_size)] for _ in range(self.tabuleiro_size)]
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ", state="normal")

    def check_win(self, player):
        """Verifica se um jogador venceu."""
        # Verifica linhas e colunas
        for i in range(self.tabuleiro_size):
            if all(self.tabuleiro[i][j] == player for j in range(self.tabuleiro_size)) \
                    or all(self.tabuleiro[j][i] == player for j in range(self.tabuleiro_size)):
                return True
        # Verifica diagonais
        if all(self.tabuleiro[i][i] == player for i in range(self.tabuleiro_size)) \
                or all(self.tabuleiro[i][self.tabuleiro_size - i - 1] == player for i in range(self.tabuleiro_size)):
            return True
        return False

    def check_tie(self):
        """Verifica se o jogo terminou em empate."""
        return all(cell != " " for row in self.tabuleiro for cell in row)

    def choose_board_color(self):
        """Permite ao jogador escolher a cor do tabuleiro."""
        _, color = colorchooser.askcolor(title="Escolha a Cor do Tabuleiro", initialcolor="#ffffff")
        return color

def main():
    root = tk.Tk()
    jogo_da_velha = JogoDaVelha(root)
    root.mainloop()

if __name__ == "__main__":
    main()
