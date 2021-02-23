from typing import List

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from tutorial.snippets.models import Snippet
from tutorial.snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request) -> HttpResponse:
    """

    """
    if request.method == 'GET':
        snippets: List[Snippet] = Snippet.objects.all()
        serializer: SnippetSerializer = SnippetSerializer(instance=snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer: SnippetSerializer = SnippetSerializer(data=data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        serializer.save()
        return JsonResponse(serializer.data, status=201)


@csrf_exempt
def snippet_detail(request, pk) -> HttpResponse:
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
        serializer.save()
        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
