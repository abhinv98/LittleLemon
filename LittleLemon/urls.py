from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reservation.views import BookingViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]
