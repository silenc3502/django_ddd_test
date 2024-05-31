from abc import ABC, abstractmethod


class BoardService(ABC):

    @abstractmethod
    def get_all_boards(self):
        pass

    @abstractmethod
    def get_board_by_id(self, board_id):
        pass

    @abstractmethod
    def create_board(self, data):
        pass

    @abstractmethod
    def update_board(self, board_id, data):
        pass

    @abstractmethod
    def delete_board(self, board_id):
        pass
    