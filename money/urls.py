from django.urls import path
from .views import *

urlpatterns = [
    path('main/', main, name="main"),
    path('record/', record, name="record"),
]
