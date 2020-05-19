from django.urls import path,re_path
from django.conf.urls import url
from . import views

urlpatterns = [
	# path('users/register/',views.RegisterView.as_view()),
	re_path(r'^users/register/$',views.RegisterView.as_view()),
	url(r'^users/login/$',views.LoginView.as_view()),
	path('users/test/',views.ResponseT.as_view()),
	path('json_data/',views.JsonDResponse.as_view()),
	path('redirect_test/',views.RedirectRes.as_view()),
	path('index/',views.IndexView.as_view(),name='index'),
]


