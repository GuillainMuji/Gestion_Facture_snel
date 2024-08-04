from django.contrib import admin
from django.urls import path, include
from Users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
]