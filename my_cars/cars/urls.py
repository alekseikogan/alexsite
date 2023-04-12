from cars.views import AddCar, CarHome, MarkList, ShowCar, about, login, tech
from django.urls import path

from .views import RegisterUser, LoginUser

urlpatterns = [
    path('', CarHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addcar/', AddCar.as_view(), name='addcar'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('tech/', tech, name='tech'),
    path('cars/<slug:car_slug>/', ShowCar.as_view(), name='show_car'),
    path('mark/<slug:mark_slug>/', MarkList.as_view(), name='show_mark'),
]
