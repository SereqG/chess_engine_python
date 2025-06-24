class PossibleMoves:
    def __init__(self, piece, xAxis, yAxis, initial_position, boardState):
        self.piece = piece
        self.x = xAxis
        self.y = yAxis
        self.initial_position = initial_position
        self.board = boardState

    def get_possible_moves(self):
        move_funcs = {
            "P": self.pawn_moves,
            "R": self.rook_moves,
            "N": self.knight_moves,
            "B": self.bishop_moves,
            "Q": self.queen_moves,
            "K": self.king_moves,
        }
        return move_funcs.get(self.piece[1], lambda: [])()

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

    def rook_moves(self):
        moves = []
        # Directions for rook movement: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        own_color = self.piece[0]

        for dx, dy in directions:
            nx, ny = self.x, self.y
            while True:
                nx += dx
                ny += dy
                # Stop if out of board bounds
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    break
                target = self.board[ny][nx]
                if target == "--":
                    # Empty square, rook can move here
                    moves.append((nx, ny))
                elif target[0] != own_color:
                    # Opponent's piece, rook can capture and stop
                    moves.append((nx, ny))
                    break
                else:
                    # Own piece, cannot move further in this direction
                    break
        return moves

    def knight_moves(self):
        # All 8 possible L-shaped moves for a knight
        offsets = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]
        moves = []
        own_color = self.piece[0]

        for dx, dy in offsets:
            nx, ny = self.x + dx, self.y + dy
            # Check if move is on the board
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = self.board[ny][nx]
                # Add move if square is empty or has opponent's piece
                if target == "--" or target[0] != own_color:
                    moves.append((nx, ny))
        return moves

    def bishop_moves(self):
        moves = []
        # Directions for bishop movement: diagonals
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        own_color = self.piece[0]

        for dx, dy in directions:
            nx, ny = self.x, self.y
            while True:
                nx += dx
                ny += dy
                # Stop if out of board bounds
                if not (0 <= nx < 8 and 0 <= ny < 8):
                    break
                target = self.board[ny][nx]
                if target == "--":
                    # Empty square, bishop can move here
                    moves.append((nx, ny))
                elif target[0] != own_color:
                    # Opponent's piece, bishop can capture and stop
                    moves.append((nx, ny))
                    break
                else:
                    # Own piece, cannot move further in this direction
                    break
        return moves

    def queen_moves(self):
        # Queen combines rook and bishop moves

        return self.rook_moves() + self.bishop_moves()

    def king_moves(self):
        moves = []
        # All 8 possible moves for a king
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        own_color = self.piece[0]

        for dx, dy in offsets:
            nx, ny = self.x + dx, self.y + dy
            # Check if move is on the board
            if 0 <= nx < 8 and 0 <= ny < 8:
                target = self.board[ny][nx]
                # Add move if square is empty or has opponent's piece
                if target == "--" or target[0] != own_color:
                    moves.append((nx, ny))
        return moves
