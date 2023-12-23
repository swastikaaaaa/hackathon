from django.contrib import admin
from django.urls import path
from .views import hitmoleView

urlpatterns = [
   
    path('hacks',hitmoleView.as_view())

    


]
