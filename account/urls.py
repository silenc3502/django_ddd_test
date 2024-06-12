from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.views import AccountViewSet
from oauth.controller.views import OauthView

router = DefaultRouter()
router.register(r'account', AccountViewSet, basename='account')

urlpatterns = [
    path('register/', AccountViewSet.as_view({'post': 'create'}), name='request-account-register'),
    path('check-nickname', AccountViewSet.as_view({'post': 'checkNicknameDuplication'}), name='request-account-nickname-duplication'),
    path('check-email-duplication', AccountViewSet.as_view({'post': 'checkEmailDuplication'}), name='request-email-duplication'),
    path('', include(router.urls)),
]