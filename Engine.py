

#Define piece indexs
KING = 1 
QUEEN = 2
BISHOP = 3
KNIGHT = 4
ROOK = 5
PAWN = 6
#Define colour
WHITE = 1
BLACK = 0

class Piece:

    def __init__(self,x,y,type,color):
        self.x,self.y = x,y
        self.type = type
        self.color = color

class Board:

    def __init__(self):
        self.board = self.get_empty_board() #create an empty 8x8 board
        self.pieces = []
        self.succes = False

        self.set_default_board_state()
        print(self.board)

    def move(self,piece,x,y):
        self.succes = True

    def get_empty_board(self):
        return [[0 for x in range(8)] for y in range(8)]

    def add_piece(self,piece):
        self.pieces.append(piece)
        self.board[piece.x][piece.y] = len(self.pieces)

    def set_default_board_state(self):
        self.board = self.get_empty_board() #create an empty 8x8 board
        self.pieces = []

        for x in range(8):
            self.add_piece(Piece(x,1,PAWN,WHITE))
            self.add_piece(Piece(x,6,PAWN,BLACK))

        for i in range(2):
            dx = i * 5
            self.add_piece(Piece(0+dx,0,ROOK,WHITE))
            self.add_piece(Piece(0+dx,7,ROOK,BLACK))
            self.add_piece(Piece(1+dx,0,KNIGHT,WHITE))
            self.add_piece(Piece(1+dx,7,KNIGHT,BLACK))
            self.add_piece(Piece(2+dx,0,BISHOP,WHITE))
            self.add_piece(Piece(2+dx,7,BISHOP,BLACK))
        self.add_piece(Piece(3,0,QUEEN,WHITE))
        self.add_piece(Piece(3,7,QUEEN,BLACK))
        self.add_piece(Piece(4,0,KING,WHITE))
        self.add_piece(Piece(4,7,KING,BLACK))