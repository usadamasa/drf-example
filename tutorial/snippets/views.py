from typing import List

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from tutorial.snippets.models import Snippet
from tutorial.snippets.serializers import SnippetSerializer


class SnippetList(APIView):
    def get(self, request, format=None) -> HttpResponse:
        snippets: List[Snippet] = Snippet.objects.all()
        serializer: SnippetSerializer = SnippetSerializer(instance=snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None) -> HttpResponse:
        data = JSONParser().parse(request)
        serializer: SnippetSerializer = SnippetSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


# @api_view(['GET', 'POST'])
# @csrf_exempt
# def snippet_list(request, format=None) -> HttpResponse:
#     if request.method == 'POST':


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def snippet_detail(request, pk: int, format=None) -> HttpResponse:
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
