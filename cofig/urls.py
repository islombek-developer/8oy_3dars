from django.contrib import admin
from django.urls import path
from travel.views import TravelViev,HotelViev,KlassViev


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/nevs/',TravelViev.as_view()),
    path('api/v1/nevs/<int:pk>/',TravelViev.as_view()),
    path('api/v2/nevs/',HotelViev.as_view()),
    path('api/v2/nevs/<int:pk>/',HotelViev.as_view()),
    path('api/v3/nevs/',KlassViev.as_view()),
    path('api/v3/nevs/<int:pk>/',KlassViev.as_view()),

]
