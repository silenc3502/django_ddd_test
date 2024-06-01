from rest_framework import viewsets, status
from rest_framework.response import Response
from board.serializers import BoardSerializer
from board.entity.models import Board
from board.service.board_service_impl import BoardServiceImpl


class BoardViewSet(viewsets.ViewSet):
    queryset = Board.objects.all()  # This line allows the router to infer the basename
    board_service = BoardServiceImpl.getInstance()

    def list(self, request):
        boards = self.board_service.get_all_boards()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        board = self.board_service.get_board_by_id(pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data)

    def create(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            board = self.board_service.create_board(serializer.validated_data)
            return Response(BoardSerializer(board).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        board = self.board_service.get_board_by_id(pk)
        serializer = BoardSerializer(board, data=request.data, partial=True)
        if serializer.is_valid():
            updated_board = self.board_service.update_board(pk, serializer.validated_data)
            return Response(BoardSerializer(updated_board).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        self.board_service.delete_board(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
