from engine.possible_moves import PossibleMoves


class PieceMovement:
    def __init__(self, board):
        self.board = board
        self.reset()

    def reset(self):
        self.clicks = []
        self.piece_to_move = ""

    def handle_board_click(
        self,
        x,
        y,
        board,
        modify_board,
        white_turn,
        set_highlighted_squares,
        prepare_new_state,
    ):
        clicked_square = board[y][x]

        if not self.clicks:
            if self._is_valid_first_click(clicked_square, white_turn):
                self.clicks.append((x, y))
                self.piece_to_move = clicked_square
                set_highlighted_squares(self.get_possible_moves(x, y))
            return

        self.clicks.append((x, y))
        if self.clicks[0] == self.clicks[1]:
            self.reset()
            set_highlighted_squares([])
            return
        modify_board(self.clicks, self.piece_to_move)
        set_highlighted_squares([])
        prepare_new_state()
        self.reset()

    def _is_valid_first_click(self, square, white_turn):
        if square == "--":
            return False
        return (white_turn and "w" in square) or (not white_turn and "b" in square)

    def get_possible_moves(self, x, y):
        return PossibleMoves(
            self.piece_to_move, x, y, (x, y), self.board
        ).get_possible_moves()

    def __str__(self):
        return f"Clicks: {self.clicks}"
