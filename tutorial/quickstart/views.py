from django.contrib.auth.models import Group, User
from django.db.models import QuerySet
from rest_framework import generics, permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


class UserList(generics.ListAPIView):
    """
    API endpoint
    """
    queryset: QuerySet = User.objects.all().order_by('-date_joined')
    serializer_class: UserSerializer = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
