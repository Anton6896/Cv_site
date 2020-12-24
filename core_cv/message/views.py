from django.shortcuts import render
from rest_framework.generics import CreateAPIView


class MessageCreateApi(CreateAPIView):
    # create
    pass


class CommentCreateApi(CreateAPIView):
    # comment for message or issue
    pass


class MessageDetailApi(CreateAPIView):
    # update, delete message/issue
    pass


class CommentDetailApi(CreateAPIView):
    # update, delete message
    pass


class CommentListApi(CreateAPIView):
    # List of all available comments for specific message by pk
    pass


class MessageListApi(CreateAPIView):
    # List of all available messages
    pass


class IssueMessageListApi(CreateAPIView):
    # list of all issues (message tag)
    pass
