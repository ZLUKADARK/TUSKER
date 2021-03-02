from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('lists.api.urls', namespace='lists')),
    path('api/', include('dashboard.api.urls', namespace='api')),
]