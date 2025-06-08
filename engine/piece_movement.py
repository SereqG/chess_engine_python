class PieceMovement:
    def __init__(self):
        self.clicks = []
        self.piece_to_move = ""

    def handle_board_click(self, xAxis, yAxis, board, modify_board):

        self.clicks.append((xAxis, yAxis))
        clicked_squere = board[yAxis][xAxis]

        print(self.clicks)

        if len(self.clicks) == 1:
            self.piece_to_move = clicked_squere
        if len(self.clicks) == 2:
            modify_board(self.clicks, self.piece_to_move)
