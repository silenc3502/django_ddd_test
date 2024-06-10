from abc import ABC, abstractmethod


class ProfileRepository(ABC):
    @abstractmethod
    def create_profile(self, nickname, email, account):
        pass

    @abstractmethod
    def findByNickname(self, nickname):
        pass

