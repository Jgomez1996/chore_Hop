from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name ='home'),
    path('user_dash', views.user_dash),
    path('driver_dash', views.driver_dash),
    path('driver_chore', views.driver_chore),
    path('user_chore', views.user_chore)
]