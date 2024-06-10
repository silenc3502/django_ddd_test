from abc import ABC, abstractmethod


class AccountService(ABC):
    @abstractmethod
    def create_account_with_default_roles(self, login_type, role_type, nickname, email):
        pass

    @abstractmethod
    def check_nickname_duplication(self, nickname):
        pass
