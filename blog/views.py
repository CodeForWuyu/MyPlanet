from django.shortcuts import render
# 接口写在这里
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from blog.models import Article,Tag,Type
from django.core import serializers
import json

@require_http_methods(["GET"])
def testRequest(request):
    response = {}

    response['msg'] = 'success'
    response['error_num'] = 0
    return JsonResponse(response)


@require_http_methods(["GET"])
def addArticle(request):
    response = {}
    try:
        article = Article(title=request.GET.get('title'))
        article.type = Type.objects.filter(id=1)[0]
        article.tag = Tag.objects.filter(id=1)[0]
        article.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] =str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def showArticles(request):
    response = {}
    try:
        articles = Article.objects.filter()
        response['list'] = json.loads(serializers.serialize('json',articles))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


