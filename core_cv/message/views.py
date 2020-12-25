from django.shortcuts import render
from rest_framework import permissions
from accounts import my_permissions  # ok
from .models import Mesage
from django.db.models import Q
from . import serializers
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
)


class MessageCreateApi(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.CreateMessageSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateApi(CreateAPIView):
    # comment for message or issue
    pass


class MessageDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, my_permissions.MessageOwner]
    serializer_class = serializers.EditMessageSerializer
    queryset = Mesage.objects.all()


class CommentDetailApi(CreateAPIView):
    # update, delete message
    pass


class CommentListApi(CreateAPIView):
    # List of all available comments for specific message by pk
    pass


class MessageListApi(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ListMessageSerializer
    queryset = Mesage.objects.filter(tag='message').filter(is_read=False).all()


class IssueMessageListApi(ListAPIView):
    # list of all issues (queryset -> issue tag, working_on, on_hold )
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.ListIssueSerializer
    queryset = Mesage.objects.filter(tag='issue').filter(status='working_on').all()


class MessageSearchFieldApi(CreateAPIView):
    # look thru the search field q , Q
    serializer_class = None
    permission_classes = None

    def get_queryset(self):
        if self.request.method == "GET":
            q = self.request.GET.get('q', None)
            if q is not None:
                # using Q library for multi queryset
                return Mesage.objects.filter(
                    Q(title__icontains=q) |
                    Q(author__username=q) |
                    Q(content__icontains=q)
                )
