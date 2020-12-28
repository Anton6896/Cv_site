from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from accounts.my_permissions import IsCommettee, CommentAuthor
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from . import serializers


# =========================   Parent comments

class CreateCommentApi(CreateAPIView):
    # comment for message
    serializer_class = serializers.CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListCommentApi(ListAPIView):
    # list of all PARENT comments
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ListCommentSerializer

    def get_queryset(self):
        qs = Comment.objects.all()  # all() overridden in model
        # can attach here all search data that you like as in message section
        return qs


class DetailCommentApi(RetrieveUpdateDestroyAPIView):
    # edit / delete comment
    permission_classes = [permissions.IsAuthenticated, CommentAuthor, permissions.IsAdminUser]
    queryset = Comment.objects.all()
    serializer_class = serializers.DetailCommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateFunctionComment(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        # POST /api/comment_function_create/?type=mesage&pk=12
        # POST /api/comment_function_create/?type=mesage&pk=12&parent_pk=36
        model_type = self.request.GET.get('type')
        pk = self.request.GET.get('pk')
        parent_pk = self.request.GET.get('parent_pk', None)

        return serializers.comment_create_serializer(
            model_type=model_type,
            pk=pk,
            parent_pk=parent_pk,
            user=self.request.user
        )


