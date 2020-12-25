from rest_framework import serializers
from .models import Mesage


class CreateMessageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(required=True, max_length=200)
    tag = serializers.ChoiceField(choices=Mesage.TAG_CHOICES,
                                  default='message')
    status = serializers.ChoiceField(choices=Mesage.STATUS_CHOICES,
                                     default='working_on')

    class Meta:
        model = Mesage
        fields = (
            'author',
            'title',
            'image',
            'content',
            'priority',
            'tag',
            'status',
        )


class EditMessageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(required=True, max_length=200)
    tag = serializers.ChoiceField(choices=Mesage.TAG_CHOICES,
                                  default='message')
    status = serializers.ChoiceField(choices=Mesage.STATUS_CHOICES,
                                     default='working_on')
    pk = serializers.IntegerField(read_only=True)

    class Meta:
        model = Mesage
        exclude = ('timestamp', 'created_at', )


class ListMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesage
        fields = (
            'author',
            'title',
            'image',
            'content',
            'priority',
        )


class ListIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesage
        fields = (
            'author',
            'title',
            'image',
            'content',
            'priority',
            'status',
        )
