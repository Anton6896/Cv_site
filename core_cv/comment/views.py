from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from accounts.my_permissions import IsCommettee, IsOwner
from django.contrib.contenttypes.models import ContentType
from .models import Comment


class CommentCreateApi(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # comment for message or issue


class ParentCommentCreateApi(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # comment for comment


class CommentListApi(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]


class CommentDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
