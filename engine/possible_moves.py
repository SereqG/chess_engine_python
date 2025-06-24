class PossibleMoves:
    def __init__(self, piece, xAxis, yAxis, initial_position, boardState):
        self.piece = piece
        self.x = xAxis
        self.y = yAxis
        self.initial_position = initial_position
        self.board = boardState

    def get_possible_moves(self):
        if self.piece in ("wP", "bP"):
            return self.pawn_moves()
        return []

    def pawn_moves(self):
        moves = []
        direction = -1 if self.piece == "wP" else 1
        opponent_color = "b" if self.piece == "wP" else "w"
        start_row = 6 if self.piece == "wP" else 1

        # Capture diagonally
        for dx in (-1, 1):

            # diagonal x
            nx = self.x + dx

            # diagonal y
            ny = self.y + direction

            # checks if nx and ny are in range of the board
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = self.board[ny][nx]
                if target != "--" and opponent_color in target:
                    moves.append((nx, ny))

        # Move forward
        one_step = (self.x, self.y + direction)
        if self.board[one_step[1]][one_step[0]] == "--":
            moves.append(one_step)

            # Move two steps from start position
            if self.y == start_row:
                two_step = (self.x, self.y + 2 * direction)
                if self.board[two_step[1]][two_step[0]] == "--":
                    moves.append(two_step)

        return moves
