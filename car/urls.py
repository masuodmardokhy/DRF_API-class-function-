from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from car import views


router = routers.DefaultRouter()   # url for class base view
router.register('person', views.PersonViwSet),
router.register('car', views.CarViewSet),



app_name = "car"
urlpatterns = [       # url for function base view
    path('get_post_person', views.person_view),
    path('get_post_car', views.car_view),
]
urlpatterns += router.urls
