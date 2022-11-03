blocked_path = "There's a piece in the path."
incorrect_path = "This piece does not move in this pattern."


def check_knight(color, board, pos):
    """
    Check if there is a knight of the opposite `color` at
    position `pos` on board `board`. 

    color : bool
        True if white

    board : Board
        Representation of the current chess board

    pos : tup
        Indices to check if there's is a knight

    Precondition `pos` is a valid position on the board.
    """
    piece = board.board[pos[0]][pos[1]]
    if piece != None and piece.color != color and piece.name == 'N':
        return False
    return True


def check_diag_castle(color, board, start, to): 
    """
    Checks the diagonal path from `start` (non-inclusive) to `to` (inclusive)
    on board `board` for any threats from the opposite `color`

    color : bool
        True if white

    board : Board
        Representation of the current chess board

    start : tup
        Starting point of the diagonal path

    to : tup
        Ending point of the diagonal path

    Precondition: `start` and `to` are valid positions on the board
    """
    
    if abs(start[0] - to[0]) != abs(start[1] - to[1]):
        print(incorrect_path)
        return False

    x_pos =  1 if to[0] - start[0] > 0 else -1
    y_pos = 1 if to[1] - start[1] > 0 else -1

    i = start[0] + x_pos
    j = start[1] + y_pos
    
    exists_piece = board.board[i][j] != None
    if exists_piece and (board.board[i][j].name == 'P' or board.board[i][j].name == 'K') and \
        board.board[i][j].color != color:
        return False

    while (i <= to[0] if x_pos==1 else i >= to[0]):
        if exists_piece and board.board[i][j].color != color:
            if board.board[i][j].name in ['B', 'Q']: 
                return False
            else:
                return True
        if exists_piece and board.board[i][j].color == color:
            return True
        i += x_pos
        j += y_pos
        exists_piece = board.board[i][j] != None

    return True


def check_diag(board, start, to):
    """
    Checks if there are no pieces along the diagonal path from
    `start` (non-inclusive) to `to` (non-inclusive). 

    board : Board
        Representation of the current board

    start : tup
        Start location of diagonal path

    to : tup
        End location of diagonal path
    """

    if abs(start[0] - to[0]) != abs(start[1] - to[1]):
        print(incorrect_path)
        return False

    x_pos =  1 if to[0] - start[0] > 0 else -1
    y_pos = 1 if to[1] - start[1] > 0 else -1

    i = start[0] + x_pos
    j = start[1] + y_pos
    while (i < to[0] if x_pos==1 else i > to[0]):
        if board.board[i][j] != None:
            print(blocked_path)
            print("At: " + str((i, j)))
            return False
        i += x_pos
        j += y_pos
    return True


def check_updown_castle(color, board, start, to):
    """
    Checks if there are any threats from the opposite `color` from `start` (non-inclusive)
    to `to` (inclusive) on board `board`.

    color : bool
        True if white's turn
    
    board : Board
        Representation of the current board

    start : tup
        Start location of vertical path

    to : tup
        End location of vertical path
    """
    
    x_pos = 1 if to[0] - start[0] > 0 else -1
    i = start[0] + x_pos

    front_piece = board[i][start[1]]
    if front_piece != None and front_piece.name == 'K' and front_piece.color != color:
        return False

    while (i <= to[0] if x_pos == 1 else i >= to[0]):
        if board.board[i][start[1]] != None and board.board[i][start[1]].color != color:
            if board.board[i][start[1]].name in ['R', 'Q']:
                return False
            else:
                return True
        if board.board[i][start[1]] != None and board.board[i][start[1]].color == color:
            return True
        
    return True

def check_updown(board, start, to):
    """
    Checks if there are no pieces along the vertical or horizontal path
    from `start` (non-inclusive) to `to` (non-inclusive). 

    board : Board
        Representation of the current board

    start : tup
        Start location of diagonal path

    to : tup
        End location of diagonal path
    """
    if start[0] == to[0]:
        smaller_y = start[1] if start[1] < to[1] else to[1]
        bigger_y = start[1] if start[1] > to[1] else to[1]

        for i in range(smaller_y + 1, bigger_y):
            if board.board[start[0]][i] != None:
                print(blocked_path)
                print("At: " + str(start[0], i))
                return False
        return True
    else:
        smaller_x = start[0] if start[0] < to[0] else to[0]
        bigger_x = start[0] if start[0] > to[0] else to[0]

        for i in range(smaller_x + 1, bigger_x):
            if board.board[i][start[1]] != None:
                print(blocked_path)
                return False
        return True



class Piece():
    """
    A class to represent a piece in chess
    
    ...

    Attributes:
    -----------
    name : str
        Represents the name of a piece as following - 
        Pawn -> P
        Rook -> R
        Knight -> N
        Bishop -> B
        Queen -> Q
        King -> K

    color : bool
        True if piece is white

    Methods:
    --------
    is_valid_move(board, start, to) -> bool
        Returns True if moving the piece at `start` to `to` is a legal
        move on board `board`
        Precondition: [start] and [to] are valid coordinates on the board.board
    is_white() -> bool
        Return True if piece is white

    """
    def __init__(self, color):
        self.name = ""
        self.color = color

    def is_valid_move(self, board, start, to):
        return False

    def is_white(self):
        return self.color

    def __str__(self):
        return self.name

class Rook(Piece):
    def __init__(self, color, first_move = True):
        super().__init__(color)
        self.name = "♜" if color else '♖'
        self.first_move = first_move 

    def is_valid_move(self, board, start, to):
        if start[0] == to[0] or start[1] == to[1]:
            return check_updown(board, start, to)
        print(incorrect_path)
        return False

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "♞" if color else '♘'

    def is_valid_move(self, board, start, to):
        if abs(start[0] - to[0]) == 2 and abs(start[1] - to[1]) == 1:
            return True
        if abs(start[0] - to[0]) == 1 and abs(start[1] - to[1]) == 2:
            return True
        print(incorrect_path)
        return False

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "♝" if color else '♗'

    def is_valid_move(self, board, start, to):
        return check_diag(board, start, to)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "♛" if color else '♕'

    def is_valid_move(self, board, start, to):
        # diagonal
        if abs(start[0] - to[0]) == abs(start[1] - to[1]):
            return check_diag(board, start, to)

        # up/down
        elif start[0] == to[0] or start[1] == to[1]:
            return check_updown(board, start, to)
        print(incorrect_path)
        return False

class King(Piece):
    def __init__(self, color, first_move = True):
        super().__init__(color)
        self.name = "♚" if color else '♔'
        self.first_move = first_move 

    def is_valid_move(self, board, start, to):
        if abs(start[0] - to[0]) == 1 or start[0] - to[0] == 0:
            if start[1] - to[1] == 0 or abs(start[1] - to[1]) == 1:
                self.first_move = False
                return True
        return False

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.name = "♟" if color else '♙'
        self.first_move = True

    def is_valid_move(self, board, start, to):
        if self.color:
            # diagonal move
            if start[0] == to[0] + 1 and (start[1] == to[1] + 1 or start[1] == to[1] - 1):
                if board.board[to[0]][to[1]] != None:
                    self.first_move = False
                    return True
                print("Cannot move diagonally unless taking.")
                return False

            # vertical move
            if start[1] == to[1]:
                if (start[0] - to[0] == 2 and self.first_move) or (start[0] - to[0] == 1):
                    for i in range(start[0] - 1, to[0] - 1, -1):
                        if board.board[i][start[1]] != None:
                            print(blocked_path)
                            return False
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False

        else:
            if start[0] == to[0] - 1 and (start[1] == to[1] - 1 or start[1] == to[1] + 1):
                if board.board[to[0]][to[1]] != None:
                    self.first_move = False
                    return True
                print(blocked_path)
                return False
            if start[1] == to[1]:
                if (to[0] - start[0] == 2 and self.first_move) or (to[0] - start[0] == 1):
                    for i in range(start[0] + 1, to[0] + 1):
                        if board.board[i][start[1]] != None:
                            print(blocked_path)
                            return False
                    self.first_move = False
                    return True
                print("Invalid move" + " or " + "Cannot move forward twice if not first move.")
                return False
            print(incorrect_path)
            return False