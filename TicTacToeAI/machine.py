import random
from TicTacToeAI.helpers import *


# chooses coordinates randomly from available coordinates on board
def easy_mode_coords(board):
	empty_cells = empty_cell_coords(board)
	x, y = random.choice(empty_cells)
	return x, y


# if a triplet is one symbol away from being completed, this method returns
# that third space's coordinates
# else returns random valid coordinates
def medium_mode_coords(board, x_turn):
	triplets = generate_triplets(get_linear_board(board))
	symbols = ("X", "O") if x_turn else ("O", "X")	
	# order matters here, since we would want machine to prioritize winning
	# over not loosing
	for symbol in symbols:
		# rows, columns and diagonals need different type of handling
		# index ('i' here), hints how to handle each triplet
		# first three are rows, next three are columns and last two diagonals
		for i, triplet in enumerate(triplets):
			if " " in triplet and triplet.count(symbol) == 2:
				if i < 3:
					x = i
					y = triplet.index(' ')
					return x, y
				elif i < 6:
					x = triplet.index(' ')
					y = i - 3
					return x, y
				elif i == 6:
					x = y = triplet.index(' ')
					return x, y
				elif i == 7:
					x = triplet.index(' ')
					y = 2 - x
					return x, y
	return easy_mode_coords(board)


# go throught each possible move and evaluate best score for machine
# using minimax algorithm
def minimax(board, max_player, depth=6):
	finished = game_finished(board)
	if finished or not depth:
		if finished:
			if "X" in finished:
				return 1
			elif "O" in finished:
				return -1
		return 0
	
	free_positions = empty_cell_coords(board)
	symbol = "X" if max_player else "O"
	
	if max_player:
		max_score = -5
		for position in free_positions:
			x, y = position
			board[x][y] = symbol
			score = minimax(board, False, depth-1)
			board[x][y] = " "
			max_score = max(score, max_score)
		return max_score
	
	else:
		min_score = 5
		for position in free_positions:
			x, y = position
			board[x][y] = symbol
			score = minimax(board, True, depth-1)
			board[x][y] = " "
			min_score = min(score, min_score)
		return min_score
	
	
def hard_mode_coords(board, x_turn):
	best_move = None
	best_score = float('-inf') if x_turn else float('inf')
	symbol = "X" if x_turn else "O"
	empty_cells = empty_cell_coords(board)
	
	for cell in empty_cells:
		x, y = cell
		board[x][y] = symbol
		position_evaluated = minimax(board, not x_turn)
		board[x][y] = " "
		
		if x_turn:
			if position_evaluated > best_score:
				best_score = position_evaluated
				best_move = cell
		else:
			if position_evaluated < best_score:
				best_score = position_evaluated
				best_move = cell	
				
	return best_move
			
				
def valid_coords(board, x_turn, difficulty):
	if difficulty == "easy":
		x, y = easy_mode_coords(board)
	elif difficulty == "medium":
		x, y = medium_mode_coords(board, x_turn)
	elif difficulty == "hard":
		x, y = hard_mode_coords(board, x_turn)
	return x, y
