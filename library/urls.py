from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('edit/<int:pk>/', views.BookUpdateView.as_view(), name='edit_book'),
    path('delete/<int:pk>', views.delete_book, name='delete_book'),
    path('register/', views.register, name='register'),
]
