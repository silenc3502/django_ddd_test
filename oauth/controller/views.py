from django.shortcuts import render

# oauth/views.py
import logging
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from oauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from oauth.serializer.kakao_usre_info_serializer import KakaoUserInfoSerializer
from oauth.service.kakao_service_impl import KakaoServiceImpl

logger = logging.getLogger(__name__)

class OauthView(ViewSet):
    kakao_service = KakaoServiceImpl.getInstance()

    def get_kakao_oauth_url(self, request):
        url = self.kakao_service.kakao_login_address()
        serializer = KakaoOauthUrlSerializer(data={'url': url})
        serializer.is_valid(raise_exception=True)
        print(f'validated_data: {serializer.validated_data}')
        return Response(serializer.validated_data)

    def get_access_token(self, request):
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            access_token = self.kakao_service.get_access_token(code)
            return JsonResponse({'access_token': access_token})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get_kakao_user_info(self, request):
        print(f"get_kakao_user_info()")
        print(f"Request data: {request.data}")

        access_token = request.data.get('access_token')
        if isinstance(access_token, str):
            # access_token이 문자열인 경우 처리합니다.
            print(f'access_token: {access_token}')
        else:
            return JsonResponse({'error': 'Invalid access token format'}, status=400)

        print(f'access_token: {access_token}')

        try:
            user_info = self.kakao_service.get_user_info(access_token)
            print("finish to request user info")
            print(f"user_info: {user_info}")
            # email = user_info['kakao_account']['email']
            return JsonResponse({'user_info': user_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # def get(self, request, *args, **kwargs):
    #     if request.path.endswith('/kakao'):
    #         return self.get_kakao_oauth_url(request)
    #     elif request.path.endswith('/kakao-check-exist'):
    #         return self.kakao_check_exist(request)
    #     elif request.path.endswith('/kakao-login'):
    #         return self.kakao_callback(request)
    #     else:
    #         return HttpResponse(status=404)
    #
    # def get_kakao_oauth_url(self, request):
    #     print("get_kakao_oauth_url()")
    #     url = self.kakao_service.kakao_login_address()
    #     print(f"Generated Kakao OAuth URL: {url}")
    #     return JsonResponse({"url": url})
    #
    # def kakao_check_exist(self, request):
    #     print("kakao_check_exist()")
    #     code = request.GET.get('code')
    #     response = self.kakao_service.check_duplicate_account(code)
    #     return JsonResponse({"result": response})
    #
    # def kakao_callback(self, request):
    #     print("kakao_callback()")
    #     response = self.kakao_service.get_account()
    #     return JsonResponse(response)
    #
    # @method_decorator(csrf_exempt)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)
    #
    # @method_decorator(csrf_exempt)
    # def post(self, request, *args, **kwargs):
    #     if request.path.endswith('/kakao-new-login'):
    #         return self.kakao_callback_new_account(request)
    #     else:
    #         return HttpResponse(status=404)
    #
    # def kakao_callback_new_account(self, request):
    #     print("kakao_callback_new_account()")
    #     import json
    #     request_data = json.loads(request.body)
    #     response = self.kakao_service.get_new_account(request_data)
    #     return JsonResponse(response)
