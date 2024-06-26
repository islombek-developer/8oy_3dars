from django.contrib import admin
from django.urls import path
from travel.views import TravelViev


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/nevs/',TravelViev.as_view())
]
