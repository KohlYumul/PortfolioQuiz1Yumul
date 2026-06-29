from django.contrib import admin
from django.urls import path, include # <--- Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')), # <--- Points to your app's urls.py
]