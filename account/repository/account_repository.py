from abc import ABC, abstractmethod


class AccountRepository(ABC):
    @abstractmethod
    def create_account_with_default_roles(self, login_type, role_type):
        pass
