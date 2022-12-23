from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.book_list, name='book_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/remove/', views.remove_book, name='remove_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),

    path('author', views.author_list, name='author_list'),
    path('author/add/', views.add_author, name='add_author'),
    path('author_select/', views.author_select, name='author_select'),
    path('author/<int:pk>/remove/', views.remove_author, name='remove_author'),
    ]