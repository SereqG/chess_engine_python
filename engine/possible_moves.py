class PossibleMoves:
    BOARD_SIZE = 8
    EMPTY = "--"

    # Directions for each piece type
    ROOK_DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    BISHOP_DIRS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    KNIGHT_OFFSETS = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]
    KING_OFFSETS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]

    def __init__(self, piece, x, y, initial_position, board):
        self.piece = piece
        self.x = x
        self.y = y
        self.initial_position = initial_position
        self.board = board
        self.color = piece[0]
        self.type = piece[1]

    def get_possible_moves(self):
        move_funcs = {
            "P": self._pawn_moves,
            "R": self._linear_moves,
            "N": self._knight_moves,
            "B": self._diagonal_moves,
            "Q": self._queen_moves,
            "K": self._king_moves,
        }
        return move_funcs.get(self.type, lambda: [])()

    def _on_board(self, x, y):
        return 0 <= x < self.BOARD_SIZE and 0 <= y < self.BOARD_SIZE

    def _is_opponent(self, target):
        return target != self.EMPTY and target[0] != self.color

    def _linear_moves(self):
        return self._sliding_moves(self.ROOK_DIRS)

    def _diagonal_moves(self):
        return self._sliding_moves(self.BISHOP_DIRS)

    def _sliding_moves(self, directions):
        moves = []
        for dx, dy in directions:
            nx, ny = self.x, self.y
            while True:
                nx += dx
                ny += dy
                if not self._on_board(nx, ny):
                    break
                target = self.board[ny][nx]
                if target == self.EMPTY:
                    moves.append((nx, ny))
                elif self._is_opponent(target):
                    moves.append((nx, ny))
                    break
                else:
                    break
        return moves

    def _knight_moves(self):
        moves = []
        for dx, dy in self.KNIGHT_OFFSETS:
            nx, ny = self.x + dx, self.y + dy
            if self._on_board(nx, ny):
                target = self.board[ny][nx]
                if target == self.EMPTY or self._is_opponent(target):
                    moves.append((nx, ny))
        return moves

    def _king_moves(self):
        moves = []
        for dx, dy in self.KING_OFFSETS:
            nx, ny = self.x + dx, self.y + dy
            if self._on_board(nx, ny):
                target = self.board[ny][nx]
                if target == self.EMPTY or self._is_opponent(target):
                    moves.append((nx, ny))
        return moves

    def _queen_moves(self):
        return self._linear_moves() + self._diagonal_moves()

    def _pawn_moves(self):
        moves = []
        direction = -1 if self.color == "w" else 1
        opponent_color = "b" if self.color == "w" else "w"
        start_row = 6 if self.color == "w" else 1

        # Captures
        for dx in (-1, 1):
            nx, ny = self.x + dx, self.y + direction
            if self._on_board(nx, ny):
                target = self.board[ny][nx]
                if target != self.EMPTY and target[0] == opponent_color:
                    moves.append((nx, ny))

        # Forward move
        nx, ny = self.x, self.y + direction
        if self._on_board(nx, ny) and self.board[ny][nx] == self.EMPTY:
            moves.append((nx, ny))
            # Double move from start
            if self.y == start_row:
                ny2 = self.y + 2 * direction
                if self._on_board(nx, ny2) and self.board[ny2][nx] == self.EMPTY:
                    moves.append((nx, ny2))
        return moves
