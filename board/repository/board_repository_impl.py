from board.models import Board
from board.repository.board_repository import BoardRepository


class BoardRepositoryImpl(BoardRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def get_all_boards(self):
        return Board.objects.all().order_by('-regDate')

    def get_board_by_id(self, board_id):
        return Board.objects.get(boardId=board_id)

    def create_board(self, data):
        board = Board(**data)
        board.save()
        return board

    def update_board(self, board, data):
        for key, value in data.items():
            setattr(board, key, value)
        board.save()
        return board

    def delete_board(self, board):
        board.delete()
