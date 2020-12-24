from django.shortcuts import render


class MessageCreateApi():
    # create
    pass


class CommentCreateApi():
    # comment for message or issue
    pass


class MessageDetailApi():
    # update, delete message/issue
    pass


class CommentDetailApi():
    # update, delete message
    pass


class CommentListApi():
    # List of all available comments for specific message by pk
    pass


class MessageListApi():
    # List of all available messages
    pass


class IssueMessageListApi():
    # list of all issues (message tag)
    pass
