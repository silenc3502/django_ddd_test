import uuid

from account.entity.account import Account
from account.entity.account_login_type import AccountLoginType
from account.entity.account_role_type import AccountRoleType
from account.entity.profile import Profile
from oauth.service.kakao_service import KakaoService
from django.conf import settings
import requests


class KakaoServiceImpl(KakaoService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.login_url = settings.KAKAO['LOGIN_URL']
            cls.__instance.client_id = settings.KAKAO['CLIENT_ID']
            cls.__instance.redirect_uri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.client_secret = settings.KAKAO['CLIENT_SECRET']
            cls.__instance.token_request_url = settings.KAKAO['TOKEN_REQUEST_URL']
            cls.__instance.userinfo_request_url = settings.KAKAO['USERINFO_REQUEST_URL']
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def kakao_login_address(self):
        return f"{self.login_url}/oauth/authorize?client_id={self.client_id}&redirect_uri={self.redirect_uri}&response_type=code"

    def get_access_token(self, code):
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'code': code,
            'client_secret': self.client_secret
        }
        response = requests.post(self.token_request_url, data=data)
        return response.json()

    def get_user_info(self, access_token):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(self.userinfo_request_url, headers=headers)
        return response.json()

    def check_duplicate_account(self, code):
        token_data = self.get_access_token(code)
        user_info = self.get_user_info(token_data['access_token'])
        email = user_info['kakao_account']['email']
        login_type = AccountLoginType.objects.get(login_type='KAKAO')

        if Profile.objects.filter(email=email, account__login_type=login_type).exists():
            return 'EXIST'
        return 'NEW'

    def save_user_info(self, user_info, nickname, profile_image_name):
        login_type = AccountLoginType.objects.get(login_type='KAKAO')
        role_type = AccountRoleType.objects.get(role_type='NORMAL')
        account = Account.objects.create(login_type=login_type, role_type=role_type)
        Profile.objects.create(nickname=nickname, email=user_info['kakao_account']['email'], profile_image_name=profile_image_name, account=account)
        return account

    def get_new_account(self, request_data):
        token_data = self.get_access_token(request_data['code'])
        user_info = self.get_user_info(token_data['access_token'])
        account = self.save_user_info(user_info, request_data['nickname'], request_data['profile_image_name'])

        user_token = str(uuid.uuid4())
        # cache.set(user_token, account.id)

        profile = Profile.objects.get(account=account)
        return {
            'nickname': profile.nickname,
            'user_token': user_token,
            'profile_image_name': profile.profile_image_name
        }

    def get_account(self, access_token):
        user_info = self.get_user_info(access_token)
        email = user_info['kakao_account']['email']
        login_type = AccountLoginType.objects.get(login_type='KAKAO')
        profile = Profile.objects.get(email=email, account__login_type=login_type)
        return {
            'nickname': profile.nickname,
            'email': email,
            'profile_image_name': profile.profile_image_name
        }
