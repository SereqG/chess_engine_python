class PieceMovement:
    def __init__(self):
        self.clicks = []
        self.piece_to_move = ""

    def handle_board_click(self, xAxis, yAxis, board, modify_board, white_turn):
        clicked_squere = board[yAxis][xAxis]

        if len(self.clicks) == 0:
            if self.init_click_validation(clicked_squere, white_turn):
                self.clicks.append((xAxis, yAxis))
                self.piece_to_move = clicked_squere
                return

        if len(self.clicks) == 1:
            print(self.clicks)
            self.clicks.append((xAxis, yAxis))
            modify_board(self.clicks, self.piece_to_move)

    def init_click_validation(self, clicked_squere, white_turn):
        if clicked_squere != "--":
            if white_turn and "w" in clicked_squere:
                return True
            if white_turn == False and "b" in clicked_squere:
                return True
        return False

    def __str__(self):
        return f"Clicks: {self.clicks}"
