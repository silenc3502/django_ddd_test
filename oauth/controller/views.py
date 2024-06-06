from django.shortcuts import render

# oauth/views.py
import logging
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oauth.service.kakao_service_impl import KakaoServiceImpl

logger = logging.getLogger(__name__)

class OauthView(View):
    kakao_service = KakaoServiceImpl.getInstance()

    def get(self, request, *args, **kwargs):
        if request.path.endswith('/kakao'):
            return self.get_kakao_oauth_url(request)
        elif request.path.endswith('/kakao-check-exist'):
            return self.kakao_check_exist(request)
        elif request.path.endswith('/kakao-login'):
            return self.kakao_callback(request)
        else:
            return HttpResponse(status=404)

    def get_kakao_oauth_url(self, request):
        print("get_kakao_oauth_url()")
        url = self.kakao_service.kakao_login_address()
        print(f"Generated Kakao OAuth URL: {url}")
        return JsonResponse({"url": url})

    def kakao_check_exist(self, request):
        code = request.GET.get('code')
        response = self.kakao_service.check_duplicate_account(code)
        return JsonResponse({"result": response})

    def kakao_callback(self, request):
        logger.info("kakaoCallback()")
        response = self.kakao_service.get_account()
        return JsonResponse(response)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        if request.path.endswith('/kakao-new-login'):
            return self.kakao_callback_new_account(request)
        else:
            return HttpResponse(status=404)

    def kakao_callback_new_account(self, request):
        import json
        request_data = json.loads(request.body)
        response = self.kakao_service.get_new_account(request_data)
        return JsonResponse(response)
