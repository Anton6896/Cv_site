from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password


class CommitteeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('pk','username', 'password', 'email',
                  'building_community_name', 'full_address')

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(CommitteeSerializer, self).create(validated_data)


class TenantSerializer(serializers.ModelSerializer):
    # the committee member is creating users (tenants)

    class Meta:
        model = models.CustomUser
        fields = ('pk', 'username', 'password', 'email', 'apartment')

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(TenantSerializer, self).create(validated_data)


class ListTenantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('pk','username', 'email', 'apartment', 'role', 'pk')
