from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from accounts import my_permissions
from django.contrib.contenttypes.models import ContentType
from .models import Comment


# Create your views here.

class CommentCreateApi(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # comment for message or issue



class ParentCommentCreateApi(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # comment for comment


class CommentListApi(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]


class CommentDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, my_permissions.ObjOwner]