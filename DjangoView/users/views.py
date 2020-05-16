from django.shortcuts import render
from django import http
from django.views import View
# Create your views here.

class RegisterView(View):
    def get(self,request):
        return http.HttpResponse('GET请求得到的画面')

    def post(self,request):
        return http.HttpResponse('POST请求得到的画面')


# def register(request):
# 	return http.HttpResponse('这是一个注册页面')




