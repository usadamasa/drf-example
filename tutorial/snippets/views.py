from typing import List

from django.http import Http404
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorial.snippets.models import Snippet
from tutorial.snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    def get(self, request, format=None) -> Response:
        snippets: List[Snippet] = Snippet.objects.all()
        serializer: SnippetSerializer = SnippetSerializer(instance=snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None) -> Response:
        data = JSONParser().parse(request)
        serializer: SnippetSerializer = SnippetSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SnippetDetail(APIView):

    def _get_object(self, pk: int) -> Snippet:
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk: int, format=None):
        snippet: Snippet = self._get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk: int, format=None):
        snippet: Snippet = self._get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk: int, format=None):
        snippet: Snippet = self._get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
