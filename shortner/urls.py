from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("create", views.create, name='create'),
    path("/<str:pk>",views.show_created_url,name='go')

]
