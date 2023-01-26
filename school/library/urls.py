from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.Library.as_view(), name='library'),
    path('query/', views.LibraryQuery.as_view(), name='library-querys'),
    path('book/<int:id>', views.select_view, name='oneBook'),
    path('book/edit/<pk>', views.UpdateBook.as_view(), name='editBook'),
    path('listbooks/', views.BookListView.as_view(), name='listbooks')
]