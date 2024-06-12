# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.serializer.account_serializer import AccountSerializer
from account.service.account_service_impl import AccountServiceImpl


class AccountViewSet(viewsets.ViewSet):
    account_service = AccountServiceImpl.getInstance()

    def create(self, request):
        try:
            nickname = request.data.get('nickname')
            email = request.data.get('email')

            account = self.account_service.create_account_with_default_roles(
                login_type='KAKAO',
                role_type='NORMAL',
                nickname=nickname,
                email=email
            )

            serializer = AccountSerializer(account)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print('Error occurred during account creation:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkNicknameDuplication(self, request):
        try:
            nickname = request.data.get('nickname')
            is_duplicate = self.account_service.check_nickname_duplication(nickname)

            if is_duplicate:
                return Response({'message': 'Nickname is already in use'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Nickname is available'}, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error occurred during nickname duplication check:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def checkEmailDuplication(self, request):
        try:
            email = request.data.get('email')
            is_duplicate = self.account_service.check_email_duplication(email)

            if is_duplicate:
                return Response({'message': 'Email is already in use'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Email is available'}, status=status.HTTP_200_OK)

        except Exception as e:
            print('Error occurred during email duplication check:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
