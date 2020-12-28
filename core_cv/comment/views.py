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


# =========================   Children comments

# class ChildCommentCreateApi(CreateAPIView):
#     # comment for comment
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = serializers.CreateChildSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class ChildListCreateApi(CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
