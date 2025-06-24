from engine.possible_moves import PossibleMoves


class PieceMovement:
    def __init__(self, board):
        self.board = board
        self.reset()

    def reset(self):
        self.clicks = []
        self.piece_to_move = None

    def handle_board_click(
        self,
        x,
        y,
        board,
        modify_board,
        white_turn,
        set_highlighted_squares,
        prepare_new_state,
        get_highlighted_squares,
    ):
        clicked_square = board[y][x]

        if not self.clicks:
            if self._is_own_piece(clicked_square, white_turn):
                self._select_piece(x, y, clicked_square, set_highlighted_squares)
            return

        if (x, y) == self.clicks[0]:
            self._cancel_selection(set_highlighted_squares)
            return

        self._move_piece(
            (x, y), modify_board, set_highlighted_squares, prepare_new_state
        )

    def _is_own_piece(self, square, white_turn):
        if square == "--":
            return False
        return (white_turn and square.startswith("w")) or (
            not white_turn and square.startswith("b")
        )

    def _select_piece(self, x, y, piece, set_highlighted_squares):
        self.clicks.append((x, y))
        self.piece_to_move = piece
        set_highlighted_squares(self.get_possible_moves(x, y))

    def _cancel_selection(self, set_highlighted_squares):
        self.reset()
        set_highlighted_squares([])

    def _move_piece(
        self, to_pos, modify_board, set_highlighted_squares, prepare_new_state
    ):
        isCorrectMove = False
        for move in self.get_possible_moves(*self.clicks[0]):
            if move[0] == to_pos[0] and move[1] == to_pos[1]:
                isCorrectMove = True
                break

        if not self.piece_to_move:
            return

        if not isCorrectMove:
            print("Invalid move")
            self.reset()
            set_highlighted_squares([])
            return
        self.clicks.append(to_pos)
        modify_board(self.clicks, self.piece_to_move)
        set_highlighted_squares([])
        prepare_new_state()
        self.reset()

    def get_possible_moves(self, x, y):
        return PossibleMoves(
            self.piece_to_move, x, y, (x, y), self.board
        ).get_possible_moves()

    def __str__(self):
        return f"Clicks: {self.clicks}"
