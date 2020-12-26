from rest_framework import serializers
from .models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    pass


class ListCommentSerializer(serializers.ModelSerializer):
    pass


class DetailCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    pass
