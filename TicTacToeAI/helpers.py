# program generates three list of board rows
# that way it's easier to insert symbols for given coordinates
def make_coord_cells(cells=list(" "*9)):
	return (cells[:3], cells[3:6], cells[6:])
	
	
# returns list of empty cell coordinates on the board
def empty_cell_coords(board):
	free_cells = []
	for x, row in enumerate(board):
		for y, cell in enumerate(row):
			if cell == " ":
				free_cells.append((x, y))
	return free_cells
	

def get_linear_board(board):
	return "".join([cell for row in board for cell in row])

# program generates every possible triplet that determines game outcome
# icnluding rows, columns and diagonals 
def generate_triplets(linear_board):
	return (linear_board[:3], linear_board[3:6], linear_board[6:],
			linear_board[::3], linear_board[1::3], linear_board[2::3],
			linear_board[::4], linear_board[2:8:2])


def game_finished(board):
	linear_board = get_linear_board(board)
	triplets = generate_triplets(linear_board)
	has_empty_cell = " " in linear_board
	
	if "XXX" in triplets:
		return "X wins!"
	elif "OOO" in triplets:
		return "O wins!"
	elif not has_empty_cell:
		return "Draw!"
	return None
