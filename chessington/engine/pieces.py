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

    def capture_enemies(self, current_square, direction, board, valid_moves):
        if current_square.col in range(1, 7) and 7 > current_square.row > 0:
            enemy_square_left = Square.at(current_square.row + direction, current_square.col - abs(direction))
            enemy_square_right = Square.at(current_square.row + direction, current_square.col + abs(direction))

            enemy_piece_left = board.get_piece(enemy_square_left)
            enemy_piece_right = board.get_piece(enemy_square_right)

            if enemy_piece_left is not None:
                enemy_colour_left = enemy_piece_left.player
                if enemy_colour_left != self.player:
                    valid_moves.append(enemy_square_left)

            if enemy_piece_right is not None:
                enemy_colour_right = enemy_piece_right.player
                if enemy_colour_right != self.player:
                    valid_moves.append(enemy_square_right)

    def get_available_moves(self, board):
        valid_moves = []
        current_square = self.position(board)
        direction = 1 if self.player == Player.WHITE else -1
        next_square = Square.at(current_square.row + direction, current_square.col)

        self.capture_enemies(current_square, direction, board, valid_moves)

        if self.is_at_starting_position(board):
            double_step_square = Square.at(current_square.row + 2 * direction, current_square.col)
            if board.is_square_empty(double_step_square):
                valid_moves.append(double_step_square)

        if self.is_at_edge_of_board(board):
            return []

        if board.is_square_empty(next_square):
            valid_moves.append(next_square)
        else:
            return []

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
        valid_moves = []
        current_square = self.position(board)
        direction = 1 if self.player == Player.WHITE else -1

        if board.is_in_bounds(current_square):
            for i in range(current_square.row, 7):
                next_square_up = Square.at(current_square.row + i * direction, current_square.col)
                next_square_down = Square.at(current_square.row - i * direction, current_square.col)
                next_square_left = Square.at(current_square.row, current_square.col - i * direction)
                next_square_right = Square.at(current_square.row, current_square.col + i * direction)

                if board.is_square_empty(next_square_up) and board.is_in_bounds(next_square_up):
                    valid_moves.append(next_square_up)
                if board.is_square_empty(next_square_down) and board.is_in_bounds(next_square_down):
                    valid_moves.append(next_square_down)
                if board.is_square_empty(next_square_left) and board.is_in_bounds(next_square_left):
                    valid_moves.append(next_square_left)
                if board.is_square_empty(next_square_right) and board.is_in_bounds(next_square_right):
                    valid_moves.append(next_square_right)
                else:
                    return []
        return valid_moves


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
