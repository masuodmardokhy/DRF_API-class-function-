from django.urls import path
from user import views


urlpatterns = [
    path('post_user', views.create_user),
    path('profil', views.profile),

]