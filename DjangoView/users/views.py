from django.shortcuts import render,redirect,reverse
from django import http
from django.views import View
# Create your views here.

class RegisterMixin(object):
    def pri(self):
        print('这是一个拓展功能类的功能')

class RegisterView(View,RegisterMixin):
    def get(self,request):
        self.pri()
        return http.HttpResponse('GET请求得到的画面')

    def post(self,request):
        return http.HttpResponse('POST请求得到的画面')

class LoginView(View):
    def get(self,request):
        return http.HttpResponse('GET得到的登录界面')

    def post(self,request):
        return http.HttpResponse('POST得到的登录界面')

class ResponseT(View):
    def get(self,request):
        return http.HttpResponse(content='测试响应代码',content_type='text/html',status='200')



class JsonDResponse(View):
    def get(self,request):
        json_dict = {
            "name":"mike",
            "age":19,
        }
        return http.JsonResponse(json_dict)


class IndexView(View):
    def get(self,request):
        return http.HttpResponse('首页')


class RedirectRes(View):
    def post(self,request):
        # return redirect('https://www.bilibili.com/')
        ret_url = reverse('users:index')
        return redirect(ret_url)


# def register(request):
# 	return http.HttpResponse('这是一个注册页面')



