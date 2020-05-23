from django.shortcuts import render
from django.views import View
from booktest.models import BookInfo,HeroInfo
from django import http
from datetime import date
from django.db.models import F,Q,Avg


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
        book = BookInfo()
        book.btitle = '西游记'
        book.bpub_date = '2020-5-20'
        # book.bread = 30
        # book.bcomment = 20
        # 注意：一般逻辑删除在数据创建时不需要定义
        book.save()

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
        # BookInfo.objects.filter(id=6).delete()

        # 测试查询数据-------------------------------------------

        return http.HttpResponse('测试增、删、改')

class TestModel2(View):
    def get(self,request):

        # ##################################基本查询###################################################
        # get()查询特定数据，查询无果会报错
        # hero = HeroInfo.objects.get(id=1)
        # print(hero)

        # all()查询所有数据
        # heros = HeroInfo.objects.all()
        # print(heros)

        # count()计数查询结果数量
        # print(heros.count())
        # count = HeroInfo.objects.filter(is_delete=False).count()
        # print('未被删除：',count)

        # ##################################过滤查询###################################################
        # 三种方法：   1.filter()——过滤得到指定条件的数据    2.exclude()——排除指定条件的数据    3.get()——过滤单一结果
        # 以上三种方法使用方式相同，只是功能不同，下面采用filter()方法测试

        '''等于查询'''

        # 测试exact:表示相等
        # book = BookInfo.objects.filter(id__exact=4)
        # print(book)

        '''模糊查询'''
        # 测试contain:表示包含（如果要包含‘%’,无需转义，直接写即可）
        # book = BookInfo.objects.filter(btitle__contains='传')
        # print(book)

        # 测试startswith、endswith:以……开头、结尾
        # book = BookInfo.objects.filter(btitle__startswith='雪')
        # print(book)
        # book = BookInfo.objects.filter(btitle__endswith='传')
        # print(book)

        '''空查询'''
        # 测试isnull：是否为空
        # book = BookInfo.objects.filter(bread__isnull=False)
        # print(book)

        '''范围查询'''
        # 测试in：在……内查询
        # book = BookInfo.objects.filter(id__in=[1,3,5])
        # print(book)

        '''比较查询'''
        # 测试gt：大于
        # book = BookInfo.objects.filter(id__gt=3)
        # print(book)

        # 测试gte：大于等于
        # book = BookInfo.objects.filter(id__gte=3)
        # print(book)

        # 测试lt：小于
        # book = BookInfo.objects.filter(id__lt=3)
        # print(book)

        # 测试lte：小于等于
        # book = BookInfo.objects.filter(id__lte=3)
        # print(book)

        '''不等于'''
        # 不等于使用：exclude()
        # book = BookInfo.objects.exclude(id=3)
        # print(book)

        '''日期查询'''
        # year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
        # 测试时间等于：
        # book = BookInfo.objects.filter(bpub_date__year=2020)
        # print(book)

        # 测试时间大于：
        # book = BookInfo.objects.filter(bpub_date__gte='1995-1-1')
        # book = BookInfo.objects.filter(bpub_date__gte=date(1995,1,1))
        # print(book)

        '''F查询和Q查询'''
        # 测试F查询
        # book = BookInfo.objects.filter(bread__gt=F('bcomment'))
        # print(book)

        # book = BookInfo.objects.filter(bread__gt=F('bcomment')*2)
        # print(book)

        '''测试Q查询:逻辑或、逻辑非、逻辑与'''
        # 逻辑与：filter()条件之间用逗号隔开即可
        # book = BookInfo.objects.filter(bread__gt=20,bpub_date__gt='1980-1-1')
        # print(book)

        # 逻辑或：filter( Q() | Q() )
        # book = BookInfo.objects.filter(Q(bread__gt=10) | Q(id__lt='3'))
        # print(book)

        # 逻辑非：~Q()
        # book = BookInfo.objects.filter(~Q(id=7))
        # print(book)

        '''聚合查询:Avg、Sum、Max、Min、Count'''
        # 测试聚合平均：其他方法同Avg    注意：使用前要从django.db.models导包
        # book = BookInfo.objects.aggregate(Avg('bread'))
        # print(book['bread__avg'])

        '''排序查询'''
        # 语法：filter().order_by()
        # book = BookInfo.objects.filter(btitle__isnull=False).order_by('bread')
        # book = BookInfo.objects.filter(btitle__isnull=False).order_by('-bread')
        # print(book)

        '''关联查询'''


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
        # response.set_cookie('name','mike',max_age=3600)
        request.session['name'] = 'mike'

        return response

class TestSessionView(View):
    def get(self,request):
        # 使用cookie辨别身份
        # 辨别逻辑：代码封装在AuthenticationMiddleware里
        # user = 用户模型类.object.get(name=name)
        # if user:
        # 已登录用户的页面
        # else：
        # 未登录用户

        # 读取session_date
        name = request.session.get('name')
        print(name)
        return http.HttpResponse('测试session')

class TestCookieView(View):
    '''测试cookie'''
    def get(self,request):
        # 读取cookie
        request.COOKIES.get('name')

        # 使用cookie辨别身份
        # 辨别逻辑：代码封装在AuthenticationMiddleware里
        # user = 用户模型类.object.get(name=name)
        # if user:
        # 已登录用户的页面
        # else：
        # 未登录用户

        return http.HttpResponse('测试cookie')