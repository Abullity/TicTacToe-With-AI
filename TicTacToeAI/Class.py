import os
from TicTacToeAI import user, machine
from TicTacToeAI.helpers import *


class TicTacToeAI:
	
	def __init__(self):
		self.x_turn = True
		self.coord_cells = None
		self.players = {}
	
	
	def game_mode(self):
		modes = ("user", "easy", "medium", "hard")
		while True:
			print("Usage: start [playerX] [playerO]")
			print("Choose players from the list: ", end="")
			print(*modes, sep=", ")
			print("Input 'exit' to quit", end="\n\n")
			cmd = input("Input command: ").strip().lower()
			
			if cmd == "exit":
				return False
			cmd = cmd.split()
			if len(cmd) == 3 and cmd[0] == "start" and cmd[1] in modes and cmd[2] in modes:
				self.players["X"] = cmd[1]
				self.players["O"] = cmd[2]
				return True
			os.system('clear')
	
	
	def display_board(self):
		os.system('clear')
		print(f"Player X: {self.players['X']}", " " * 4, end="")
		print(f"Player O: {self.players['O']}", end="\n\n")
		print(9 * '-')
		for i in range(3):
			print("| {} {} {} |".format(*self.coord_cells[i]))
		print(9 * '-', end="\n\n")
	
	
	def make_move(self, player):
		if player == "user":
			x, y = user.valid_coords(self.coord_cells, self.x_turn)
		else:
			x, y = machine.valid_coords(self.coord_cells, self.x_turn, player)
			
		symbol = "X" if self.x_turn else "O"	
		self.coord_cells[x][y] = symbol
		self.x_turn = not self.x_turn
					
					
	def play(self):
		os.system('clear')
		while self.game_mode():
			self.coord_cells = make_coord_cells()
			while True:
				self.display_board()
				game_state = game_finished(self.coord_cells)
				if game_state:
					print(game_state)
					break
				player = self.players["X"] if self.x_turn else self.players["O"]
				self.make_move(player)
			print(sep="\n\n")
			self.x_turn = True;
