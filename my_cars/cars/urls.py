from django.urls import path

from cars.views import (
    about, login, tech, CarHome, MarkList, ShowCar, AddCar
    )

urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addcar/', AddCar.as_view(), name='addcar'),
    path('login/', login, name='login'),
    path('tech/', tech, name='tech'),
    path('cars/<slug:car_slug>/', ShowCar.as_view(), name='show_car'),
    path('mark/<slug:mark_slug>/', MarkList.as_view(), name='show_mark'),
]
