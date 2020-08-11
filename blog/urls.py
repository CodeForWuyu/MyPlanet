'''
定义路由
'''

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from blog import views
from MyPlanet import urls

urlpatterns = [
    url("testRequest/",views.testRequest),
    url("addArticle",views.addArticle),
    url("showArticles",views.showArticles)
]