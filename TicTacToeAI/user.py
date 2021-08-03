def valid_coords(board, x_turn):
	print("Input coordinates in range [1-3] [1-3]", end="\n\n")
	while True:
		inpt = input("X turn: " if x_turn else "O turn: ").strip().split()
		if len(inpt) != 2:
			print("You should input two coordinates!")
			continue
		try:
			x, y = [int(char) for char in inpt]
		except ValueError:
			print("You should enter numbers!")
			continue
		if x not in range(1, 4) or y not in range(1, 4):
			print("Coordinates should be from 1 to 3!")
			continue
		x, y = x - 1, y - 1
		if board[x][y] in ("X", "O"):
			print("This cell is occupied! Choose another one!")
			continue
		return x, y
