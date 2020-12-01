from django.contrib import admin
from django.urls import path, include

from jobs import views

handler404 = views.custom_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),
]
