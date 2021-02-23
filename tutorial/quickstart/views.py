from typing import List

from django.contrib.auth.models import Group, User
from django.db.models import QuerySet
from rest_framework import permissions, viewsets
from rest_framework.permissions import BasePermission

from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset: QuerySet = User.objects.all().order_by('-date_joined')
    serializer_class: UserSerializer = UserSerializer
    permission_classes: List[BasePermission] = [
        permissions.IsAuthenticated
    ]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
