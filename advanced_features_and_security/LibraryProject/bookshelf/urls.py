from django.contrib import admin
from django.urls import path
from .views import HelloView, book_list, BookDetailView
from . import views
from .views import example_form_view

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('books/', book_list, name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', views.home, name='home'),
    path("example-form/", example_form_view, name="example_form"),
]






