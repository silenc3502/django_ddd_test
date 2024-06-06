from abc import ABC, abstractmethod


class KakaoService(ABC):

    @abstractmethod
    def kakao_login_address(self):
        pass

    @abstractmethod
    def check_duplicate_account(self, code):
        pass

    @abstractmethod
    def get_account(self):
        pass

    @abstractmethod
    def get_new_account(self, request_data):
        pass
