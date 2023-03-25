from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home),
    path('office/',views.office),
    path('index/',views.index)
]
