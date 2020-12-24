from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Mesage
from django.db.models import Q


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


class MessageQueryListApi(CreateAPIView):
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
