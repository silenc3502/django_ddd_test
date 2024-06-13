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
        print(f"findByEmail called: {email}")
        try:
            profile = Profile.objects.get(email=email)
            print(f"Profile found: {profile}")
            return profile
        except Profile.DoesNotExist:
            print(f"No profile found with email: {email}")
            return None
        except Exception as e:
            print(f"An error occurred while fetching profile by email: {e}")
            return None
