class GameBoard:
    def __init__(self, game_pieces):
        self.game_pieces = game_pieces
        self.squares = {
            "A": [1, 2, 3, 4, 5, 6, 7, 8],
            "B": [1, 2, 3, 4, 5, 6, 7, 8],
            "C": [1, 2, 3, 4, 5, 6, 7, 8],
            "D": [1, 2, 3, 4, 5, 6, 7, 8],
            "E": [1, 2, 3, 4, 5, 6, 7, 8],
            "F": [1, 2, 3, 4, 5, 6, 7, 8],
            "G": [1, 2, 3, 4, 5, 6, 7, 8],
            "H": [1, 2, 3, 4, 5, 6, 7, 8],
        }
        print(self.squares["H"])


#
# Using above second method to create a
# 2D array
# rows, cols = (5, 5)
# arr=[]
# for i in range(rows):
#     col = []
#     for j in range(cols):
#         col.append(0)
#     arr.append(col)
# print(arr)
class Player:
    def __init__(self):
        pass


# class PieceType:
#     def __init__(self):
#         self.type = ["Queen", "King", "Bishop", "Knight", "Castle", "Pawn"]
#
#     def get_type_allowed_moves(self):
#         if self.type == "Queen":
#             allowed_moves =
#         elif self.type == "King":
#         elif self.type == "Bishop":
#         elif self.type == "Knight":
#         elif self.type == "Castle":
#         elif self.type =="Pawn":
#             allowed_moves = []




class ChessPiece:
    def __init__(self, piece_type, piece_location):
        self.piece_type = piece_type  # gong to be an enum
        self.piece_location = piece_location  # tuple
        pass

    def move_piece(self, new_location):
        self.piece_location = new_location

    def find_piece(self, location):
        if location is self.piece_location:
            return self

    def does_piece_take_hostage(self, end_location):
        if self.find_piece(end_location) is not None:
            return True
        return False

    def get_type_allowed_moves(self):
        vertical_spaces_end_of_board = 7 - self.piece_location[0]
        if self.piece_type == "Queen":
                allowed_vertical_movement =
        elif self.type == "King":
        elif self.type == "Bishop":
            allowed_vertical_movement = self.piece_location
        elif self.type == "Knight":
        elif self.type == "Castle":
        elif self.type =="Pawn":
            if(self.piece_location[1] + 1)
            allowed_vertical_spaces = self.piece_location[1] + 1
            allowed_horizontal_movement = self.piece_location[0] + 0
            allowed_new_location = self.piece_location[allowed_horizontal_movement, allowed_vertical_movement]
        return allowed_new_location


def main():
    board = GameBoard([])


if __name__ == '__main__':
    main()
