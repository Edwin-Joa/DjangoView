from django.shortcuts import render
from django import http
from django.views import View
import json
# Create your views here.

class QRParamsView(View):
    def get(self,request):
        name = request.GET.get('name')
        age = request.GET.get('age')
        return http.HttpResponse(f'取得的字符串数据为：name: {name}, age: {age}。')

class FormParamsView(View):
    def post(self,request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        return http.HttpResponse(f'取得的表单数据为：name: {name}, age: {age}。')


class JsonParamsView(View):
    def post(self,request):
        json_str = request.body
        django_dict = json.loads(json_str)
        name = django_dict.get('name')
        age = django_dict.get('age')
        return http.HttpResponse(f'取得的json数据为：name: {name}, age: {age}。')

class UrlParamView(View):
    def get(self,request,age):
        return http.HttpResponse(f'取得的url数据为：Age: {age}。')

class PhoneParamView(View):
    def get(self,request,phone_num):
        return http.HttpResponse(f'取得的url数据为：Tel: {phone_num}。')

class RequestHeaderParamView(View):
    def get(self,request):
        ret = request.META.get('CONTENT_TYPE')
        return http.HttpResponse(f'{ret}')
