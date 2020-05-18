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
```

    * 如此基本路由配置完毕

---



2. 第二天：

    * 以不同方式请求页面：

      * 于views视图文件中，定义不同的函数视图

        ```python
        def register(request):
            if request.method == 'GET':
        	    return http.HttpReponse('GET请求返回的页面')
        	elif request.method == 'POST':
                return http.HttpResponse('POST请求返回的页面')
```

        说明：该方法可以实现根据不同的请求方法返回不同的页面，但代码量大，且代码复用性较小；所以通常使用类视图
    
    * 定义类视图：
    
      * 进入子应用中的view视图文件，定义类视图：
    
        ```python
        class RegisterView(View):
            def get(self,request):
                return http.HttpResponse('get请求返回的界面')
            def post(self,request):
                return http.HttpResponse('post请求返回的界面')
        ```


​        

      * 配置路由：进入子应用的urls.py文件，配置路由：
    
        ```python
        urlpatterns = [
            path('users/regitser/',views.RegisterView.as_view()),
        ]
        ```
    
      * 配置好路由之后即可通过get、post两种请求方式请求register页面，但若使用post请求页面，默认会报错，原因是django默认设置了csrf保护机制，在除了get请求之外的其他所有请求，django都会进行验证，所以在测试阶段可先关闭此功能:
    
        ```Python
        # 进入django项目的setting文件中，找到中间件列表中间的csrf中间件，将对应代码注释掉即可
        ```
    
    * 了解类视图的响应机制，as_view()：
    
      1. 首先将类视图转化为函数视图
      2. 接受类视图的参数并传递给函数视图
      3. 分发派遣不同的相应
    
    * 类视图的拓展类
    
      ```Python
      class RegisterMixin(object):
          def pp(self):
              print('这是一个功能扩展类的内容')
              
      class RegisterView(View,RegisterMixin):
          def get(self,request):
              self.pp()
              return http.HttpResponse('类视图get请求注册页面')
          def post(self,request):
              return http.HttpResponse('类视图post请求注册页面')
      ```

---



3. 第三天：路由
   * path

