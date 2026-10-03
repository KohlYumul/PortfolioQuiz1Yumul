from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.project_list_view, name='projects'),
    path('project/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimonies_list'),
    path('testimonies/add/', views.add_testimony_view, name='add_testimony'),
    path('testimony/<int:pk>/', views.testimony_detail_view, name='testimony_detail'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-logout/', views.admin_logout_view, name='admin_logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/projects/create/', views.create_project_dashboard_view, name='create_project'),
    path('dashboard/projects/create/', views.create_project_dashboard_view, name='add_project'),
    path('dashboard/tech-stacks/create/', views.create_tech_stack_dashboard_view, name='create_tech_stack'),
]

