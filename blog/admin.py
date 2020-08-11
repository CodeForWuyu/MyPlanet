from django.contrib import admin

# Register your models here.
#注册模型,以便在后台管理模型
from blog.models import *

admin.site.register(Article)
admin.site.register(Type)
admin.site.register(Tag)