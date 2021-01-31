from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name='main_page'),
]
