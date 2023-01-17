from django.urls import path 
from . import views 
app_name = "Landing_Page"
urlpatterns = [
    path('', views.title, name='title'),
    path('Introduction', views.introduction, name='intro'),
    path('Classes', views.classes, name= 'Classes')
]