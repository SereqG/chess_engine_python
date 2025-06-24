from engine.piece_movement import PieceMovement


class GameState:
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.current_move = None
        self.move_logs = []
        self.white_turn = True
        self.highlighted_squeres = []

    def modify_board(self, clicks, piece):
        self.board[clicks[0][1]][clicks[0][0]] = "--"
        self.board[clicks[1][1]][clicks[1][0]] = piece

    def set_highlighted_squeres(self, squeres):
        self.highlighted_squeres = squeres

    def prepare_new_state(self):
        self.move_logs.append(self.current_move)
        self.current_move = None
        self.white_turn = not self.white_turn

    def handle_movement(self, xAxis, yAxis):
        if self.current_move is None:
            self.current_move = PieceMovement(self.board)

        self.current_move.handle_board_click(
            xAxis,
            yAxis,
            self.board,
            self.modify_board,
            self.white_turn,
            self.set_highlighted_squeres,
            self.prepare_new_state,
        )
