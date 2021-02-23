from typing import List

from django.contrib.auth.models import Group, User
from rest_framework import serializers

from tutorial.snippets.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model: User = User
        fields: List[str] = [
            'url',
            'username',
            'email',
            'groups',
            'snippets',
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Group = Group
        fields: List[str] = [
            'url',
            'name',
        ]
