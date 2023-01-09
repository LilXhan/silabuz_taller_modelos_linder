from django.urls import path 
from . import views

urlpatterns = [
    path('', views.AdministrationClassroomView.as_view() , name='index'),
    path('add-classroom/', views.CreateClassroomView.as_view(), name='add-classroom'),
    path('delete-classroom/<int:id>', views.delete_classroom, name='delete-classroom')
]