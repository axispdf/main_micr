from django.urls import path
import django
from . import views
from .views import index


app_name = 'polls'

urlpatterns = [
    path('', views.index ,name = 'index'),
]