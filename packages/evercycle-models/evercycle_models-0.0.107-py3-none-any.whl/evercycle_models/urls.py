from django.urls import path
from .views import health_check

urlpatterns = [
    # ... other URL patterns ...
    path('health/', health_check, name='health_check'),
]
