from account.repository.account_repository_impl import AccountRepositoryImpl
from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service import AccountService


class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__profileRepository = ProfileRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def create_account_with_default_roles(self, login_type, role_type, nickname, email):
        account = self.__accountRepository.create_account_with_default_roles(login_type, role_type)
        self.__profileRepository.create_profile(nickname, email, account)

    def check_nickname_duplication(self, nickname):
        try:
            profile = self.__profileRepository.findByNickname(nickname)
            if profile:
                return True  # 닉네임이 이미 사용 중임
            else:
                return False  # 닉네임이 사용 가능함
        except Exception as e:
            print('Error occurred during nickname duplication check:', e)
            return True

    def check_email_duplication(self, email):
        print(f"check_email_duplication: {email}")
        profile = self.__profileRepository.findByEmail(email)
        return profile is not None


