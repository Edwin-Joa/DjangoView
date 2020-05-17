from django.urls import path,re_path
from django.conf.urls import url
from . import views


urlpatterns = [
	# path('users/register/',views.RegisterView.as_view()),
	re_path(r'^users/register/$',views.RegisterView.as_view()),
	url(r'^users/login/$',views.LoginView.as_view()),
]


