# profile_repository_impl.py
from account.entity.profile import Profile
from account.repository.profile_repository import ProfileRepository


class ProfileRepositoryImpl(ProfileRepository):
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

    def create_profile(self, nickname, email, account):
        profile = Profile.objects.create(nickname=nickname, email=email, account=account)
        return profile

    def findByNickname(self, nickname):
        try:
            return Profile.objects.get(nickname=nickname)
        except Profile.DoesNotExist:
            return False

    def findByEmail(self, email):
        try:
            return Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return False
