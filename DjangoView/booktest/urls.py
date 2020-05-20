from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.TestModel1.as_view()),
]