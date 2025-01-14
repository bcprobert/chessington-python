"""
A module providing a representation of a chess board. The rules of chess are not implemented - 
this is just a "dumb" board that will let you move pieces around as you like.
"""

from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Knight, Bishop, Rook, Queen, King
from tkinter import *

BOARD_SIZE = 8


class Board:
    """
    A representation of the chess board, and the pieces on it.
    """

    def __init__(self, player, board_state):
        self.current_player = Player.WHITE
        self.board = board_state
        self.en_passant_state = None

    @staticmethod
    def empty():
        return Board(Player.WHITE, Board._create_empty_board())

    @staticmethod
    def at_starting_position():
        return Board(Player.WHITE, Board._create_starting_board())

    @staticmethod
    def _create_empty_board():
        return [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    @staticmethod
    def _create_starting_board():

        # Create an empty board
        board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Setup the rows of pawns
        board[1] = [Pawn(Player.WHITE) for _ in range(BOARD_SIZE)]
        board[6] = [Pawn(Player.BLACK) for _ in range(BOARD_SIZE)]

        # Setup the rows of pieces
        piece_row = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        board[0] = list(map(lambda piece: piece(Player.WHITE), piece_row))
        board[7] = list(map(lambda piece: piece(Player.BLACK), piece_row))

        return board

    def set_piece(self, square, piece):
        """
        Places the piece at the given position on the board.
        """
        self.board[square.row][square.col] = piece

    def get_piece(self, square):
        """
        Retrieves the piece from the given square of the board.
        """
        return self.board[square.row][square.col]

    def is_square_empty(self, square):
        """
        Checks if a square is empty.
        """
        return self.get_piece(square) is None

    def find_piece(self, piece_to_find):
        """
        Searches for the given piece on the board and returns its square.
        """
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is piece_to_find:
                    return Square.at(row, col)
        raise Exception('The supplied piece is not on the board')

    def move_piece(self, from_square, to_square):
        """
        Moves the piece from the given starting square to the given destination square. Also checks for pawn promotion.
        """
        moving_piece = self.get_piece(from_square)
        if moving_piece is not None and moving_piece.player == self.current_player:
            if isinstance(moving_piece, Pawn) and (to_square.row == 0 or to_square.row == 7):
                moving_piece = Queen(self.current_player)  # Pawn promotion mechanic. Automatically promotes to Queen.
            self.set_piece(to_square, moving_piece)
            self.set_piece(from_square, None)
            self.en_passant_deletion(moving_piece, to_square)
            self.set_en_passant_state(to_square, from_square, moving_piece)
            self.current_player = self.current_player.opponent()

    def en_passant_deletion(self, moving_piece, to_square):
        if not isinstance(moving_piece, Pawn):
            return
        if moving_piece.enpassant_truefalse(self, to_square):
            self.set_piece(self.en_passant_state, None)

    def set_en_passant_state(self, to_square, from_square, moving_piece):
        if not isinstance(moving_piece, Pawn):
            self.en_passant_state = None
            return
        if abs(to_square.row - from_square.row) == 2:
            self.en_passant_state = to_square
            return
        self.en_passant_state = None

    def capture_possible(self, current_position, candidate_position):
        """
        Checks if a piece is on the opposition team.
        """
        if self.get_piece(current_position).player != self.get_piece(candidate_position).player:
            return True
        return False
