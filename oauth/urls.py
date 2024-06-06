from django.urls import path
from oauth.controller.views import OauthView

urlpatterns = [
    path('kakao', OauthView.as_view()),
    path('kakao-check-exist', OauthView.as_view()),
    path('kakao-login', OauthView.as_view()),
    path('kakao-new-login', OauthView.as_view()),
]
