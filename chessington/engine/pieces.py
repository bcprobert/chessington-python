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
        """
        Finds the position of the piece on the board. The piece will now know where it is.
        """
        return board.find_piece(self)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def is_at_starting_position(self, board):
        """
        Checks if the pawn is at its starting position as other moves are available if it is.
        """
        start_positions = {Player.WHITE: 1, Player.BLACK: 6}
        return start_positions[self.player] == self.position(board).row

    @staticmethod
    def capture_enemies(current_square, candidate_square, direction, board):
        """
        Checks if the pawn can capture an enemy piece.
        """
        valid_moves = []

        if current_square.is_on_board() and candidate_square.is_on_board():
            if not board.is_square_empty(candidate_square):
                if board.capture_possible(current_square, candidate_square):
                    valid_moves.append(Square.at(candidate_square.row, candidate_square.col))

        return valid_moves

    def get_available_moves(self, board):
        """
        Finds moves available to the pawn
        """
        valid_moves = []
        current_square = self.position(board)
        direction = 1 if self.player == Player.WHITE else -1
        next_square = Square.at(current_square.row + direction, current_square.col)

        candidate_square = Square.at(current_square.row + direction, current_square.col - abs(direction))
        valid_moves += self.capture_enemies(current_square, candidate_square, direction, board)
        candidate_square = Square.at(current_square.row + direction, current_square.col + abs(direction))
        valid_moves += self.capture_enemies(current_square, candidate_square, direction, board)

        if current_square.is_on_board() and next_square.is_on_board():
            if self.is_at_starting_position(board):
                double_step_square = Square.at(current_square.row + 2 * direction, current_square.col)
                if board.is_square_empty(double_step_square):
                    valid_moves.append(double_step_square)

            if board.is_square_empty(next_square):
                valid_moves.append(next_square)

        return valid_moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        valid_moves = self.get_forward_horizontal_moves(board)
        valid_moves += self.get_backward_horizontal_moves(board)
        valid_moves += self.get_forward_vertical_moves(board)
        valid_moves += self. get_backward_vertical_moves(board)
        return valid_moves

    def get_forward_horizontal_moves(self, board):
        left = (1, -2)
        left_moves = self.get_moves_in_direction(board, left)
        right = (1, 2)
        right_moves = self.get_moves_in_direction(board, right)
        return left_moves + right_moves

    def get_backward_horizontal_moves(self, board):
        left = (-1, -2)
        left_moves = self.get_moves_in_direction(board, left)
        right = (-1, 2)
        right_moves = self.get_moves_in_direction(board, right)
        return left_moves + right_moves

    def get_forward_vertical_moves(self, board):
        left = (2, -1)
        left_moves = self.get_moves_in_direction(board, left)
        right = (2, 1)
        right_moves = self.get_moves_in_direction(board, right)
        return left_moves + right_moves

    def get_backward_vertical_moves(self, board):
        left = (-2, -1)
        left_moves = self.get_moves_in_direction(board, left)
        right = (-2, 1)
        right_moves = self.get_moves_in_direction(board, right)
        return left_moves + right_moves

    def get_moves_in_direction(self, board, direction):
        valid_moves = []
        distance = 1
        start_position = self.position(board)

        move_vector = (direction[0] * distance, direction[1] * distance)
        candidate_position = start_position.translate_by(move_vector)
        if candidate_position.is_on_board():
            if board.is_square_empty(candidate_position):
                valid_moves.append(candidate_position)
            elif board.capture_possible(start_position, candidate_position):
                valid_moves.append(candidate_position)

        return valid_moves


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        valid_moves = self.get_forward_moves(board)
        valid_moves += self.get_backward_moves(board)
        return valid_moves

    def get_forward_moves(self, board):
        left = (1, -1)
        left_moves = self.get_moves_in_direction(board, left)
        right = (1, 1)
        right_moves = self.get_moves_in_direction(board, right)
        return left_moves + right_moves

    def get_backward_moves(self, board):
        left = (-1, -1)
        left_moves = self.get_moves_in_direction(board, left)
        right = (-1, 1)
        right_moves = self.get_moves_in_direction(board, right)
        return left_moves + right_moves

    def get_moves_in_direction(self, board, direction):
        valid_moves = []
        distance = 1
        start_position = self.position(board)

        while True:
            move_vector = (direction[0] * distance, direction[1] * distance)
            candidate_position = start_position.translate_by(move_vector)
            if candidate_position.is_on_board():
                if board.is_square_empty(candidate_position):
                    valid_moves.append(candidate_position)
                    distance += 1
                elif board.capture_possible(start_position, candidate_position):
                    valid_moves.append(candidate_position)
                    break
                else:
                    break
            else:
                break
        return valid_moves


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        valid_moves = self.get_vertical_moves(board)
        valid_moves += self.get_horizontal_moves(board)
        return valid_moves

    def get_vertical_moves(self, board):
        up = (1, 0)
        up_moves = self.get_moves_in_direction(board, up)
        down = (-1, 0)
        down_moves = self.get_moves_in_direction(board, down)
        return up_moves + down_moves

    def get_horizontal_moves(self, board):
        right = (0, 1)
        up_moves = self.get_moves_in_direction(board, right)
        left = (0, -1)
        down_moves = self.get_moves_in_direction(board, left)
        return up_moves + down_moves

    def get_moves_in_direction(self, board, direction):
        valid_moves = []
        distance = 1
        start_position = self.position(board)

        while True:
            move_vector = (direction[0] * distance, direction[1] * distance)
            candidate_position = start_position.translate_by(move_vector)
            if candidate_position.is_on_board():
                if board.is_square_empty(candidate_position):
                    valid_moves.append(candidate_position)
                    distance += 1
                elif board.capture_possible(start_position, candidate_position):
                    valid_moves.append(candidate_position)
                    break
                else:
                    break
            else:
                break
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
