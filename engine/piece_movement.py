from engine.possible_moves import PossibleMoves


class PieceMovement:
    possible_moves_for_piece = None

    def __init__(self, board):
        self.clicks = []
        self.piece_to_move = ""
        self.board = board

    def handle_board_click(
        self, xAxis, yAxis, board, modify_board, white_turn, set_highlighted_squeres
    ):
        clicked_squere = board[yAxis][xAxis]

        if len(self.clicks) == 0:
            if self.init_click_validation(clicked_squere, white_turn):
                self.clicks.append((xAxis, yAxis))
                self.piece_to_move = clicked_squere
                set_highlighted_squeres(self.get_possible_moves(xAxis, yAxis))
                return

        if len(self.clicks) == 1:
            self.clicks.append((xAxis, yAxis))
            modify_board(self.clicks, self.piece_to_move)
            set_highlighted_squeres([])

    def init_click_validation(self, clicked_squere, white_turn):
        if clicked_squere != "--":
            if white_turn and "w" in clicked_squere:
                return True

            if white_turn == False and "b" in clicked_squere:
                return True

        return False

    def get_possible_moves(self, xAxis, yAxis):
        possible_moves = PossibleMoves(
            self.piece_to_move, xAxis, yAxis, self.clicks[0], self.board
        )
        return possible_moves.get_possible_moves()

    def __str__(self):
        return f"Clicks: {self.clicks}"
