from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo,HeroInfo
from django import http

# Create your views here.


class TestModel1(View):
    def get(self,request):
        # 测试增加数据-------------------------------------------
        # 测试create()方法
        # HeroInfo.objects.create(
        #     hbook_id = 5,
        #     hname= '孙悟饭',
        #     hgender= 0,
        #     hcomment= '筋斗云'
        # )

        # 测试save()方法
        # book = BookInfo()
        # book.btitle = '西游记'
        # book.bpub_date = '2020-5-20'
        # book.bread = 30
        # book.bcomment = 20
        # # 注意：一般逻辑删除在数据创建时不需要定义
        # book.save()

        # 测试修改数据-------------------------------------------
        # 测试save()方法
        # hero = HeroInfo.objects.get(hname='猪八戒')
        # hero.hname = '猪悟能'
        # hero.save()

        # 测试update()方法
        # BookInfo.objects.filter(btitle='西游记').update(btitle='西游记后传')

        # 测试删除数据-------------------------------------------
        # 测试delete()     模型对象.delete()
        # hero = HeroInfo.objects.get(id=19)
        # hero.delete()

        # 测试filter(),加delete()方法     模型对象.filter().degete()
        # HeroInfo.objects.filter(hname='孙悟饭').delete()

        # 测试查询数据-------------------------------------------

        return http.HttpResponse('测试增、删、改')

class TestModel2(View):
    def get(self,request):

        # 基本查询###################################################
        # get()查询特定数据，查询无果会报错
        hero = HeroInfo.objects.get(id=1)
        print(hero)
        # all()查询所有数据
        heros = HeroInfo.objects.all()
        print(heros)
        # count()计数查询结果数量
        print(heros.count())
        count = HeroInfo.objects.filter(is_delete=False).count()
        print('未被删除：',count)

        # 过滤查询###################################################
        # 三种方法：   1.filter()——过滤得到指定条件的数据    2.exclude()——排除指定条件的数据    3.get()——过滤单一结果




        return http.HttpResponse('测试查询')


class TempView(View):
    def get(self,request):
        # 假装在处理逻辑。。。

        # 构造上下文字典：将上下文字典中的数据渲染到HTML模板文件
        context = {
            'subject':'人生苦短',
            'hot':'我用Python'
        }

        # 使用上下文字典渲染模板

        # 响应结果：模板（html文件）
        return render(request,'temp.html',context)

class BooksView(View):
    def get(self,request):
        # 查询数据库
        # 查询所有的图书信息
        books = BookInfo.objects.all()
        # 构造上下文字典
        context = {
            'books':books
        }
        # 使用上下文字典渲染模板，并响应

        response = render(request,'books.html',context)
        # 如果值为中文，编码时会出错,不能写中文
        response.set_cookie('name','mike',max_age=3600)
        return response


