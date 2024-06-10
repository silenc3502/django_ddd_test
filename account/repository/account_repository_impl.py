from account.entity.account import Account
from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType
from account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
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

    def create_account_with_default_roles(self, login_type, role_type):
        login_type_obj, _ = AccountLoginType.objects.get_or_create(login_type=login_type)
        role_type_obj, _ = AccountRoleType.objects.get_or_create(role_type=role_type)

        account = Account.objects.create(login_type=login_type_obj, role_type=role_type_obj)
        return account


