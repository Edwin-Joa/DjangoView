# DjangoView
Make a Django function View and push it.



---

1. 第一天：

  * 新建django项目：
    * 使用虚拟环境：workon Django
    * 在虚拟环境下新建项目：django-admin startproject 项目名
  * 配置项目、注册子应用：
    * 进入项目，打开setting.py文件，在该文件中可以更改时区，语言，以及注册子应用
    * 新建子应用users：django-admin startapp users
    * 在setting文件中，注册子应用：找到installed app列表，添加子应用名：users
  * 新建函数视图：
    * 注册完子应用即可于子应用的view文件中定义函数视图了
    ```python
from django import http
def register(request):
    	return http.Response('函数视图get请求得到的注册页面')
    ```
  
    * 配置路由，首先在子应用中创建路由文件：touch urls.py
    * 配置路由：
    ```python
from django.url import path
from . import views
urlpatterns = [
    	path('users/register/',views.register),
]
    ```
    
    * 在django项目主目录的主路由文件中配置路由，在urlpatterns列表中添加子应用路由：
    ```python
from django.urls import path,include
urlpatterns = [
	path('',include('users.urls')),
]
    ```
    * 如此基本路由配置完毕



---



2. 第二天：
    * 以不同方式请求页面：
      
      * 于views视图文件中，定义不同的函数视图
      
        ```python
        def RegisterView(request):
            if request.method == 'GET':
                return http.HttpResponse('get返回的界面')
            else:
                return http.HttpResponse('post返回的界面')
        ```
    
       
  
     说明：该方法可以实现根据不同的请求方法返回不同的页面，但代码量大，且代码复用性较小；所以通常使用类视图
     
   * 定义类视图：
     
     * 进入子应用中的view视图文件，定义类视图：
   
   * 配置路由：进入子应用的urls.py文件，配置路由：
   
      * 配置好路由之后即可通过get、post两种请求方式请求register页面，但若使用post请求页面，默认会报错，原因是django默认设置了csrf保护机制，在除了get请求之外的其他所有请求，django都会进行验证，所以在测试阶段可先关闭此功能:
    * 了解类视图的响应机制，as_view()：
   
      1. 首先将类视图转化为函数视图
      2. 接受类视图的参数并传递给函数视图
      3. 分发派遣不同的相应
   
    * 类视图的拓展类
   
---



3. 第三天：路由——根据用户的请求，返回对应的响应页面
   
   * path
   
   * re_path:
   
     ```python
     # 注册子路由也可以用：re_path()
     from django.urls import re_path
     
     urlpatterns = [
         re_path(r'^request_response/re_path/$',views.RePathView.as_view()),
     ]
     ```
   
   * url:
   
     ```python
     # url()方法同re_path()方法
     from django.urls import re_path
     
     urlpatterns = [
         url(r'^request_response/url/$',views.UrlView.as_view()),
     ]
     ```
   
   * 三种方法，url是属于之前版本，比较原始的方法，需要对路径定义严格的正则表达式，而path可以不用定义正则表达式，因为已经封装好了，而re_path方法是新旧版本之间的过度方法，其用法同url方法。

---



4. 第四天——获取request请求参数：

   * 获取请求中的字符串数据

     **主要方法：request.GET**

     ```python
     # 1.注册子路由
     urlpatterns = [
         path('query_string/',views.QSParamView.as_view()),
     ]
     # 2.定义相应类视图
     class QSParamView(View):
         def get(self,request):
             name = request.GET.get('name')
             age = request.GET.get('age')
             return http.HttpResponse(f'接收到的字符串数据为：Name: {name}, Age: {age}')
     ```

     

   * 获取请求体中的数据

     * 获取表单数据

       **主要方法：request.POST**

       ```python
       # 1.注册子路由
       urlpatterns = [
           path('form_data/',views.FDParamView.as_view()),
       ]
       # 2.定义对应视图
       class FDParamView(View):
           def post(self,request):
               username = request.POST.get('username')
               password = request.POST.get('password')
               return http.HttpResponse(f'接收到的表单数据为：Username: {username}, Password: {password}')
           
       ```

       

     * 获取json数据

       **主要方法：request.body** 

       ```python
       # 1.注册子路由
       urlpatterns = [
           path('json_data/',views.JsonParamView.as_view()),
       ]
       # 2.定义视图
       import json
       class JsonParamView(View):
           def post(self,request):
               json_str = request.body
               json_dict = json.loads(json_str)
               name = json_dict.get('name')
               age = json_dict.get('age')
               return http.HttpResponse(f'接收到的json数据为：Name: {name}, Age: {age}')
       ```

       

   * 获取url路径中的数据

     **django内置转换器：**

     ```python
     DEFAULT_CONVERTERS = {
         'int': IntConverter(),            # 匹配正整数，包含0
         'path': PathConverter(),     # 匹配任何非空字符串，包含了路径分隔符
         'slug': SlugConverter(),      # 匹配字母、数字以及横杠、下划线组成的字符串
         'str': StringConverter(),      # 匹配除了路径分隔符（/）之外的非空字符串，这是默认的形式
         'uuid': UUIDConverter(),   # 匹配格式化的uuid，如 075194d3-6885-417e-a8a8-6c931e272f00
     }
     ```

     * 获取内置转换器数据

       ```python
       # 1. 注册子路由
       urlpatterns = [
           path('url_path/<int:age>/',views.UrlCParamView.as_view()),
       ]
       # 2. 定义视图
       class UrlCParamView(View):
           def get(self,request,age):
               return http.HttpResponse(f'接收到的url路径数据为： Age: {age}')
       ```

       

     * 获取无内置转换器数据

       * 方法一：自定义路由转换器

         ```python
         # 1.在根目录下创建转换器文件
         touch converters.py
         
         # 2. 在转换器文件中定义转换器
         class MobileConverter:
             # 定义正则表达式
             regex = '1[3-9]\d{9}'
             def to_python(self,value):
                 return int(value)
             def to_url(self,value):
                 return str(value)
             
         # 3. 注册转换器：进入主路由文件
         from django.urls import register_converter
         from converters import MobileConverter
         register_converter(MobileConverter,'mobile')
         
         # 4.利用自定义的路由转换器注册子路由
         urlpatterns = [
             path('url_param/<mobile:phone_num>/',views.UrlParamView.as_view()),
         ]
         
         # 5.定义视图
         class UrlParamView(View):
             def get(self,request,phone_num):
                 return http.HttpResponse(f'接收到的url路径数据为： Tel: {phone_num}')
         ```

         

       * 方法二：re_path()或url()

         re_path()和url()方法不需要定义转换器，但是需要定义严格的正则表达式

         ```python
         # 1.注册子路由
         from django.urls import re_path
         urlpatterns = [
             re_path(r'^url_param/(?P<phone_num>1[3-9]\d{9} )/$',views.UrlParamView.as_view()),
         ]
         # 2.定义视图
         class UrlParamView(View):
             def get(self,request,phone_num):
                 return http.HttpResponse(f'接收到的url路径数据为： Tel: {phone_num}')
         ```

       * path()、re_path()、url()三种方法如何做选择，视情况而定，一般有内置转换器，path()方法更方便，若没有内置转换器，用re_path()更简便。

   * 获取请求头数据

     **主要方法：request.META**

     request.META为字典型数据

     ```python
     # 1.注册子路由
     # 2. 定义视图
     class HeaderParamView(View):
         def get(self,request):
             re_dict = request.META
             ret = re_dict.get('CONTENT_TYPE')
             return   http.HttpResponse(f'接收到的header数据为： Content_type: {ret}')
     ```

   * 其他对象属性
   
   ---



5. 第五天：response响应



