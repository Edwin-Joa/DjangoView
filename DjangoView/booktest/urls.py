from django.urls import path
from . import views

urlpatterns = [
    path('data/',views.TestModel1.as_view()),
    path('data_query/',views.TestModel2.as_view()),
    path('temp/',views.TempView.as_view()),
    path('books/',views.BooksView.as_view()),
    path('cookies/',views.TestCookieView.as_view()),
    path('session/',views.TestSessionView.as_view()),
]