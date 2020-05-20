from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo
from django import http

# Create your views here.


class TestModel1(View):
    def get(self,request):

        # 测试create()方法
        BookInfo.objects.create(
            btitle= '三国演义',
            bpub_date= '2020-5-21',
            bread= 100,
            bcomment= 200
        )



        # 测试save()方法
        book = BookInfo()
        book.btitle = '西游记'
        book.bpub_date = '2020-5-20'
        book.bread = 30
        book.bcomment = 20
        # 注意：一般逻辑删除在数据创建时不需要定义
        book.save()

        return http.HttpResponse('测试增、删、改')