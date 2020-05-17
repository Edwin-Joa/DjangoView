from django.shortcuts import render
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



# def register(request):
# 	return http.HttpResponse('这是一个注册页面')



