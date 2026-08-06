from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list_view, name='projects'),
    path('projects/add/', views.add_project_view, name='add_project'),
    path('project/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimonies_list'),
    path('testimonies/add/', views.add_testimony_view, name='add_testimony'),
    path('testimony/<int:pk>/', views.testimony_detail_view, name='testimony_detail'),
]
