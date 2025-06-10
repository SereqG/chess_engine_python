class PossibleMoves:

    def __init__(self, piece, xAxis, yAxis, initial_position, boardState):
        self.piece = piece
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.initial_position = initial_position
        self.boardState = boardState

        self.possible_moves = {
            "wP": self.pawn_possible_moves(),
            "bP": self.pawn_possible_moves(),
        }

    def pawn_possible_moves(self):
        possible_moves = []
        if self.piece == "wP":
            diagonally_possitions = [
                {
                    "possition": (self.xAxis - 1, self.yAxis - 1),
                    "oponent": self.boardState[self.yAxis - 1][self.xAxis - 1],
                },
                {
                    "possition": (self.xAxis + 1, self.yAxis - 1),
                    "oponent": self.boardState[self.yAxis - 1][self.xAxis + 1],
                },
            ]

            for i in diagonally_possitions:
                if i["oponent"] != "--" and "b" in i["oponent"]:
                    possible_moves.append(i["possition"])

            if self.initial_position[1] == 6:
                possible_moves.append(
                    (self.initial_position[0], self.initial_position[1] - 1)
                )
                possible_moves.append(
                    (self.initial_position[0], self.initial_position[1] - 2),
                )
            else:
                possible_moves.append(
                    (self.initial_position[0], self.initial_position[1] - 1)
                )

        else:
            diagonally_possitions = [
                {
                    "possition": (self.xAxis + 1, self.yAxis + 1),
                    "oponent": self.boardState[self.yAxis + 1][self.xAxis + 1],
                },
                {
                    "possition": (self.xAxis - 1, self.yAxis + 1),
                    "oponent": self.boardState[self.yAxis + 1][self.xAxis - 1],
                },
            ]

            for i in diagonally_possitions:
                if i["oponent"] != "--" and "w" in i["oponent"]:
                    possible_moves.append(i["possition"])

            if self.initial_position[1] == 1:
                possible_moves.append(
                    (self.initial_position[0], self.initial_position[1] + 1)
                )
                possible_moves.append(
                    (self.initial_position[0], self.initial_position[1] + 2),
                )
            else:
                possible_moves.append(
                    (self.initial_position[0], self.initial_position[1] + 1)
                )

        return possible_moves
