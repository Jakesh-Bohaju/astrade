from django.urls import path
from .views import *
from DecorFront.views import BaseView

app_name = 'decorfront'

urlpatterns = [
    path('', HomePage.as_view(), name='index')
]

