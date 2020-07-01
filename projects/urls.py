from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.AllProjects.as_view(), name='all_projects'),
    path('login/', views.Login.as_view(), name='login'),
    path('<str:project_id>/', views.SingleProject.as_view(), name='single_project'),
]