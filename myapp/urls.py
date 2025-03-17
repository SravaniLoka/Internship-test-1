from django.urls import path
from .views import htop_view
from . import views

urlpatterns = [
    path('htop/', htop_view),
]