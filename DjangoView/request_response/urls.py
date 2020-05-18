from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('query_string/',views.QRParamsView.as_view()),
    path('formatData/',views.FormParamsView.as_view()),
    path('json/',views.JsonParamsView.as_view()),
    path('url_param1/<int:age>/',views.UrlParamView.as_view()),
    path('url_param2/<mobile:phone_num>/',views.PhoneParamView.as_view()),
    re_path(r'^url_param3/(?P<phone_num>1[3-9]\d{9})/$',views.PhoneParamView.as_view()),
    path('request_header/',views.RequestHeaderParamView.as_view())
]
