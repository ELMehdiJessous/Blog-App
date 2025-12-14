from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_post/<str:id_post>',views.delete_post,name="delete_post"),
    path('change_name',views.change_name,name="change_name"),
    path('add_like/<str:id_post>',views.add_like,name="add_like"),
]