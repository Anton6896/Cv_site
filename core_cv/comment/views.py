from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework import permissions
from accounts import my_permissions


# Create your views here.

class CommentCreateApi(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # comment for message or issue
    pass


class CommentListApi(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pass


class CommentDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, my_permissions.ObjOwner]
    pass
