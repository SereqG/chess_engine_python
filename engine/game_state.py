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

    def modify_board(self, clicks, piece):
        self.board[clicks[0][1]][clicks[0][0]] = "--"
        self.board[clicks[1][1]][clicks[1][0]] = piece

    def handle_movement(self, xAxis, yAxis):
        if self.current_move is None:

            self.current_move = PieceMovement()
            self.current_move.handle_board_click(
                xAxis, yAxis, self.board, self.modify_board
            )

        else:
            self.current_move.handle_board_click(
                xAxis, yAxis, self.board, self.modify_board
            )
            self.move_logs.append(self.current_move)
            self.current_move = None
