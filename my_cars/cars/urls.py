from django.urls import path

from cars.views import index, about, addcar, login, tech, show_car, show_mark

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addcar/', addcar, name='addcar'),
    path('login/', login, name='login'),
    path('tech/', tech, name='tech'),
    path('cars/<int:car_id>/', show_car, name='show_car'),
    path('mark/<int:mark_id>/', show_mark, name='show_mark'),
]
