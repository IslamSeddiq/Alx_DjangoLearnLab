from django.contrib import admin
from django.urls import path
from .views import HelloView, book_list, BookDetailView

urlpatterns = [
    path('admin/', admin.site.urls),  # admin site
    path('hello/', HelloView.as_view(), name='hello'),
    path('books/', book_list, name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]


