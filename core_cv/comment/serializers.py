from rest_framework import serializers
from .models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = (
            "user",
            'parent',
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
    content_type = serializers.SerializerMethodField()
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'detail_url',
            'replies_count',
            'id',
            'parent',
            "user",
            "timestamp",
            "content",
            "object_pk",
            "content_type",
        )

    def get_user(self, obj):
        return str(obj.user.username)

    def get_content_type(self, obj):
        return str(obj.content_type)

    def get_replies_count(self, obj):
        if obj.is_parent:
            return obj.is_child.count()
        return 0


class DetailCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    content_type = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    def get_content_type(self, obj):
        return str(obj.content_type)

    def get_replies(self, obj):
        if obj.is_parent:
            return ChildCommentSerializer(obj.is_child, many=True).data
        else:
            return None

    class Meta:
        model = Comment
        fields = (
            'id',
            "user",
            "parent",
            "content",
            "content_type",
            "object_pk",
            'replies',
        )


class ChildCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            "content",
            'timestamp',
        )
