from board.repository.board_repository_impl import BoardRepositoryImpl
from board.service.board_service import BoardService


class BoardServiceImpl(BoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__boardRepository = BoardRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def get_all_boards(self):
        return self.__boardRepository.get_all_boards()

    def get_board_by_id(self, board_id):
        return self.__boardRepository.get_board_by_id(board_id)

    def create_board(self, data):
        return self.__boardRepository.create_board(data)

    def update_board(self, board_id, data):
        board = self.__boardRepository.get_board_by_id(board_id)
        return self.__boardRepository.update_board(board, data)

    def delete_board(self, board_id):
        board = self.__boardRepository.get_board_by_id(board_id)
        self.__boardRepository.delete_board(board)
