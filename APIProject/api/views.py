# from crypt import methods
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import parsers

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

def article_list(request):

    # get all article
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data =  parsers().parse(request)
        serializer = ArticleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)

