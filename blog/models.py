from django.db import models

# Create your models here.
# 定义blog应用数据模型


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    tagName = models.CharField('标签名',max_length=10)

    def __str__(self):
        return self.tagName

class Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    typeName = models.CharField('类型名',max_length=10)

    def __str__(self):
        return self.typeName


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=10,verbose_name="作者",default="夏目")
    title = models.CharField(max_length=150,verbose_name='文章标题')
    summary = models.TextField('文章摘要',max_length=230,default='文章摘要务必填写')
    type = models.ForeignKey(Type,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    body = models.TextField(verbose_name='文章内容')
    img_link = models.CharField('图片地址',default="../static/image/timg.jpg",max_length=255)
    create_date = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    views = models.IntegerField('浏览量',default=0)
    is_top = models.BooleanField('置顶',default=False)

    def __str__(self):
        return self.title

