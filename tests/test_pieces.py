from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Rook, Bishop, Queen, King, Knight


class TestPawns:

    @staticmethod
    def test_white_pawns_can_move_up_one_square():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_pawns_can_move_down_one_square():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(5, 4) in moves

    @staticmethod
    def test_white_pawn_can_move_up_two_squares_if_not_moved():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(1, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves

    @staticmethod
    def test_black_pawn_can_move_down_two_squares_if_not_moved():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(6, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves

    @staticmethod
    def test_white_pawn_cannot_move_up_two_squares_if_already_moved():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        starting_square = Square.at(1, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(2, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_down_two_squares_if_already_moved():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        starting_square = Square.at(6, 4)
        board.set_piece(starting_square, pawn)

        intermediate_square = Square.at(5, 4)
        pawn.move_to(board, intermediate_square)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_if_piece_in_front():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_if_piece_in_front():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(3, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_two_in_front():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(6, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_two_in_front():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(4, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert obstructing_square not in moves

    @staticmethod
    def test_white_pawn_cannot_move_two_squares_if_piece_one_in_front():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(1, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(2, 4)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) not in moves

    @staticmethod
    def test_black_pawn_cannot_move_two_squares_if_piece_one_in_front():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(6, 4)
        board.set_piece(pawn_square, pawn)

        obstructing_square = Square.at(5, 4)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square, obstruction)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) not in moves

    @staticmethod
    def test_white_pawn_cannot_move_at_top_of_board():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        square = Square.at(7, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_pawn_cannot_move_at_bottom_of_board():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        square = Square.at(0, 4)
        board.set_piece(square, pawn)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_pawns_can_capture_diagonally():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.BLACK)
        enemy1_square = Square.at(4, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.BLACK)
        enemy2_square = Square.at(4, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        enemy1 = Pawn(Player.WHITE)
        enemy1_square = Square.at(2, 5)
        board.set_piece(enemy1_square, enemy1)

        enemy2 = Pawn(Player.WHITE)
        enemy2_square = Square.at(2, 3)
        board.set_piece(enemy2_square, enemy2)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert enemy1_square in moves
        assert enemy2_square in moves

    @staticmethod
    def test_white_pawns_cannot_move_diagonally_except_to_capture():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.WHITE)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.WHITE)
        friendly_square = Square.at(4, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(4, 3) not in moves
        assert Square.at(4, 5) not in moves

    @staticmethod
    def test_black_pawns_can_capture_diagonally():
        # Arrange
        board = Board.empty()
        pawn = Pawn(Player.BLACK)
        pawn_square = Square.at(3, 4)
        board.set_piece(pawn_square, pawn)

        friendly = Pawn(Player.BLACK)
        friendly_square = Square.at(2, 5)
        board.set_piece(friendly_square, friendly)

        # Act
        moves = pawn.get_available_moves(board)

        # Assert
        assert Square.at(2, 3) not in moves
        assert Square.at(2, 5) not in moves


class TestRooks:
    @staticmethod
    def test_white_rook_can_move_vertically_and_horizontally():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(1, 3)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(1, 4) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(0, 3) in moves
        assert Square.at(1, 1) in moves

    @staticmethod
    def test_black_rook_can_move_vertically_and_horizontally():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(1, 5)
        board.set_piece(rook_square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(1, 4) in moves
        assert Square.at(4, 5) in moves
        assert Square.at(0, 5) in moves
        assert Square.at(1, 6) in moves

    @staticmethod
    def test_white_rook_cannot_move_if_friendly_piece_in_front_or_next_to():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        rook_square = Square.at(2, 2)
        board.set_piece(rook_square, rook)

        obstructing_square1 = Square.at(2, 1)
        obstructing_square2 = Square.at(1, 2)
        obstructing_square3 = Square.at(2, 3)
        obstructing_square4 = Square.at(3, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_rook_cannot_move_if_friendly_piece_in_front_or_next_to():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        rook_square = Square.at(2, 2)
        board.set_piece(rook_square, rook)

        obstructing_square1 = Square.at(2, 1)
        obstructing_square2 = Square.at(1, 2)
        obstructing_square3 = Square.at(2, 3)
        obstructing_square4 = Square.at(3, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_rook_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.WHITE)
        square = Square.at(0, 7)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(0, 8) not in moves

    @staticmethod
    def test_black_rook_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        rook = Rook(Player.BLACK)
        square = Square.at(0, 7)
        board.set_piece(square, rook)

        # Act
        moves = rook.get_available_moves(board)

        # Assert
        assert Square.at(0, 8) not in moves


class TestBishops:
    @staticmethod
    def test_white_bishop_can_move_diagonally():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(3, 3)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_bishop_can_move_diagonally():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(3, 3)
        board.set_piece(bishop_square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_white_bishop_cannot_move_if_friendly_piece_in_the_way():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        bishop_square = Square.at(2, 2)
        board.set_piece(bishop_square, bishop)

        obstructing_square1 = Square.at(1, 1)
        obstructing_square2 = Square.at(3, 3)
        obstructing_square3 = Square.at(1, 3)
        obstructing_square4 = Square.at(3, 1)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_bishop_cannot_move_if_friendly_piece_in_the_way():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.BLACK)
        bishop_square = Square.at(2, 2)
        board.set_piece(bishop_square, bishop)

        obstructing_square1 = Square.at(1, 1)
        obstructing_square2 = Square.at(3, 3)
        obstructing_square3 = Square.at(1, 3)
        obstructing_square4 = Square.at(3, 1)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_bishop_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(1, 7)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves
        assert Square.at(0, 8) not in moves

    @staticmethod
    def test_black_bishop_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        bishop = Bishop(Player.WHITE)
        square = Square.at(1, 7)
        board.set_piece(square, bishop)

        # Act
        moves = bishop.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves
        assert Square.at(0, 8) not in moves


class TestQueens:
    @staticmethod
    def test_white_queen_can_move_diagonally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(3, 3)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_queen_can_move_diagonally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(3, 3)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_white_queen_can_move_vertically_and_horizontally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(1, 3)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(1, 4) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(0, 3) in moves
        assert Square.at(1, 1) in moves

    @staticmethod
    def test_black_queen_can_move_vertically_and_horizontally():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(1, 3)
        board.set_piece(queen_square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(1, 4) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(0, 3) in moves
        assert Square.at(1, 1) in moves

    @staticmethod
    def test_white_queen_cannot_move_if_friendly_piece_in_the_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        queen_square = Square.at(2, 2)
        board.set_piece(queen_square, queen)

        obstructing_square1 = Square.at(1, 1)
        obstructing_square2 = Square.at(3, 3)
        obstructing_square3 = Square.at(1, 3)
        obstructing_square4 = Square.at(3, 1)
        obstructing_square5 = Square.at(2, 1)
        obstructing_square6 = Square.at(2, 3)
        obstructing_square7 = Square.at(1, 2)
        obstructing_square8 = Square.at(3, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)
        board.set_piece(obstructing_square5, obstruction)
        board.set_piece(obstructing_square6, obstruction)
        board.set_piece(obstructing_square7, obstruction)
        board.set_piece(obstructing_square8, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_queen_cannot_move_if_friendly_piece_in_the_way():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        queen_square = Square.at(2, 2)
        board.set_piece(queen_square, queen)

        obstructing_square1 = Square.at(1, 1)
        obstructing_square2 = Square.at(3, 3)
        obstructing_square3 = Square.at(1, 3)
        obstructing_square4 = Square.at(3, 1)
        obstructing_square5 = Square.at(2, 1)
        obstructing_square6 = Square.at(2, 3)
        obstructing_square7 = Square.at(1, 2)
        obstructing_square8 = Square.at(3, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)
        board.set_piece(obstructing_square5, obstruction)
        board.set_piece(obstructing_square6, obstruction)
        board.set_piece(obstructing_square7, obstruction)
        board.set_piece(obstructing_square8, obstruction)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_queen_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.WHITE)
        square = Square.at(1, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves
        assert Square.at(0, 8) not in moves
        assert Square.at(1, 8) not in moves

    @staticmethod
    def test_black_queen_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        queen = Queen(Player.BLACK)
        square = Square.at(1, 7)
        board.set_piece(square, queen)

        # Act
        moves = queen.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves
        assert Square.at(0, 8) not in moves
        assert Square.at(1, 8) not in moves


class TestKings:
    @staticmethod
    def test_white_king_can_move_diagonally():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(3, 3)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_black_king_can_move_diagonally():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(3, 3)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(4, 4) in moves
        assert Square.at(2, 2) in moves
        assert Square.at(4, 2) in moves
        assert Square.at(2, 4) in moves

    @staticmethod
    def test_white_king_can_move_vertically_and_horizontally():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(3, 3)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(2, 3) in moves

    @staticmethod
    def test_black_king_can_move_vertically_and_horizontally():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(3, 3)
        board.set_piece(king_square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(3, 4) in moves
        assert Square.at(4, 3) in moves
        assert Square.at(3, 2) in moves
        assert Square.at(2, 3) in moves

    @staticmethod
    def test_white_king_cannot_move_if_friendly_piece_in_the_way():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        king_square = Square.at(2, 2)
        board.set_piece(king_square, king)

        obstructing_square1 = Square.at(1, 1)
        obstructing_square2 = Square.at(3, 3)
        obstructing_square3 = Square.at(1, 3)
        obstructing_square4 = Square.at(3, 1)
        obstructing_square5 = Square.at(2, 1)
        obstructing_square6 = Square.at(2, 3)
        obstructing_square7 = Square.at(1, 2)
        obstructing_square8 = Square.at(3, 2)
        obstruction = Pawn(Player.WHITE)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)
        board.set_piece(obstructing_square5, obstruction)
        board.set_piece(obstructing_square6, obstruction)
        board.set_piece(obstructing_square7, obstruction)
        board.set_piece(obstructing_square8, obstruction)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_king_cannot_move_if_friendly_piece_in_the_way():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        king_square = Square.at(2, 2)
        board.set_piece(king_square, king)

        obstructing_square1 = Square.at(1, 1)
        obstructing_square2 = Square.at(3, 3)
        obstructing_square3 = Square.at(1, 3)
        obstructing_square4 = Square.at(3, 1)
        obstructing_square5 = Square.at(2, 1)
        obstructing_square6 = Square.at(2, 3)
        obstructing_square7 = Square.at(1, 2)
        obstructing_square8 = Square.at(3, 2)
        obstruction = Pawn(Player.BLACK)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)
        board.set_piece(obstructing_square5, obstruction)
        board.set_piece(obstructing_square6, obstruction)
        board.set_piece(obstructing_square7, obstruction)
        board.set_piece(obstructing_square8, obstruction)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_king_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        king = King(Player.WHITE)
        square = Square.at(1, 7)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves
        assert Square.at(0, 8) not in moves
        assert Square.at(1, 8) not in moves

    @staticmethod
    def test_black_king_cannot_move_off_top_of_board():
        # Arrange
        board = Board.empty()
        king = King(Player.BLACK)
        square = Square.at(1, 7)
        board.set_piece(square, king)

        # Act
        moves = king.get_available_moves(board)

        # Assert
        assert Square.at(2, 8) not in moves
        assert Square.at(0, 8) not in moves
        assert Square.at(1, 8) not in moves


class TestKnights:
    @staticmethod
    def test_white_knights_can_move_in_l_shape():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves
        assert Square.at(4, 1) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(2, 1) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves

    @staticmethod
    def test_black_knights_can_move_in_l_shape():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(4, 5) in moves
        assert Square.at(4, 1) in moves
        assert Square.at(5, 4) in moves
        assert Square.at(5, 2) in moves
        assert Square.at(2, 5) in moves
        assert Square.at(2, 1) in moves
        assert Square.at(1, 4) in moves
        assert Square.at(1, 2) in moves

    @staticmethod
    def test_white_knight_cannot_move_if_space_blocked_by_friendly_piece():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 3)
        board.set_piece(square, knight)

        obstructing_square1 = Square.at(4, 5)
        obstructing_square2 = Square.at(4, 1)
        obstructing_square3 = Square.at(5, 4)
        obstructing_square4 = Square.at(5, 2)
        obstructing_square5 = Square.at(2, 5)
        obstructing_square6 = Square.at(2, 1)
        obstructing_square7 = Square.at(1, 4)
        obstructing_square8 = Square.at(1, 2)
        obstruction = Knight(Player.WHITE)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)
        board.set_piece(obstructing_square5, obstruction)
        board.set_piece(obstructing_square6, obstruction)
        board.set_piece(obstructing_square7, obstruction)
        board.set_piece(obstructing_square8, obstruction)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_black_knight_cannot_move_if_space_blocked_by_friendly_piece():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(3, 3)
        board.set_piece(square, knight)

        obstructing_square1 = Square.at(4, 5)
        obstructing_square2 = Square.at(4, 1)
        obstructing_square3 = Square.at(5, 4)
        obstructing_square4 = Square.at(5, 2)
        obstructing_square5 = Square.at(2, 5)
        obstructing_square6 = Square.at(2, 1)
        obstructing_square7 = Square.at(1, 4)
        obstructing_square8 = Square.at(1, 2)
        obstruction = Knight(Player.BLACK)
        board.set_piece(obstructing_square1, obstruction)
        board.set_piece(obstructing_square2, obstruction)
        board.set_piece(obstructing_square3, obstruction)
        board.set_piece(obstructing_square4, obstruction)
        board.set_piece(obstructing_square5, obstruction)
        board.set_piece(obstructing_square6, obstruction)
        board.set_piece(obstructing_square7, obstruction)
        board.set_piece(obstructing_square8, obstruction)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert len(moves) == 0

    @staticmethod
    def test_white_knight_cannot_move_at_top_of_board():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.WHITE)
        square = Square.at(3, 7)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 9) not in moves
        assert Square.at(4, 9) not in moves
        assert Square.at(5, 8) not in moves
        assert Square.at(1, 8) not in moves

    @staticmethod
    def test_black_knight_cannot_move_at_top_of_board():
        # Arrange
        board = Board.empty()
        knight = Knight(Player.BLACK)
        square = Square.at(3, 7)
        board.set_piece(square, knight)

        # Act
        moves = knight.get_available_moves(board)

        # Assert
        assert Square.at(2, 9) not in moves
        assert Square.at(4, 9) not in moves
        assert Square.at(5, 8) not in moves
        assert Square.at(1, 8) not in moves
