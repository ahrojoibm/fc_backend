from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all),
    path('<str:project_id>/', views.detail)
]