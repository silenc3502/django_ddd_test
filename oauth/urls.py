from django.urls import path, include
from rest_framework.routers import DefaultRouter

from oauth.controller.views import OauthView

# urlpatterns = [
#     path('kakao', OauthView.as_view()),
#     # path('kakao-check-exist', OauthView.as_view()),
#     # path('kakao-login', OauthView.as_view()),
#     # path('kakao-new-login', OauthView.as_view()),
#     path('authentication/kakao/oauth-code', get_github_user_info, name='get_github_user_info'),
# ]

router = DefaultRouter()
router.register(r'oauth', OauthView, basename='oauth')

urlpatterns = [
    path('kakao/', OauthView.as_view({'get': 'get_kakao_oauth_url'}), name='request-kakao-oauth-code'),
    path('kakao/oauth-code', OauthView.as_view({'post': 'get_access_token'}), name='request-kakao-oauth-access-token'),
    path('kakao/user-info', OauthView.as_view({'post': 'get_kakao_user_info'}), name='request-kakao-user-info'),
    path('', include(router.urls)),
]