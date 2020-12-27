from rest_framework import serializers
from .models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            "user",
            "parent",
            "content",
            "content_type",
            "object_pk",
        )


class ListCommentSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='comments:detail',
        lookup_field='pk'
    )
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return str(obj.user.username)

    class Meta:
        model = Comment
        fields = (
            'detail_url',
            'id',
            "user",
            "parent",
            "content",
            "content_type",
            "object_pk",
        )


class DetailCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            'id',
            "user",
            "parent",
            "content",
            "content_type",
            "object_pk",
        )
