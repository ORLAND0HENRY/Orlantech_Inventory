# sales_inventory_system/sales_inventory_system/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # <-- ADD THIS LINE for authentication
    path('', include('core.urls')),
]