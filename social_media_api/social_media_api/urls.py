from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),  # Include user app URLs
    path('api/', include('posts.urls')),
]