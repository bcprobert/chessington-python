"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square


class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)

    def position(self, board):
        return board.find_piece(self)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def is_at_starting_position(self, board):
        start_positions = {Player.WHITE: 1, Player.BLACK: 6}
        return start_positions[self.player] == self.position(board).row

    def is_at_edge_of_board(self, board):
        board_edges = {Player.WHITE: 7, Player.BLACK: 0}
        return board_edges[self.player] == self.position(board).row

    def get_available_moves(self, board):
        current_square = self.position(board)
        direction = 1 if self.player == Player.WHITE else -1

        valid_moves = []
        next_square = Square.at(current_square.row + direction, current_square.col)

        if self.is_at_edge_of_board(board):
            return []

        if board.is_square_empty(next_square):
            valid_moves.append(next_square)
        else:
            return []

        if self.is_at_starting_position(board):
            double_step_square = Square.at(current_square.row + 2 * direction, current_square.col)
            if board.is_square_empty(double_step_square):
                valid_moves.append(double_step_square)

        return valid_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []
