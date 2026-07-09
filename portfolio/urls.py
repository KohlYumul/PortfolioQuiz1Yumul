from django.urls import path
from . import views

urlpatterns = [
    # Static pages 
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list_view, name='projects'),
    path('project/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
]
