from django.urls import path
from employee import views

urlpatterns= [
    path('post_employee/', views.post_employee),
    path('get_employee/', views.get_employee),
    path('get_update_delete_employee/<int:pk>', views.get_update_delete_employee),
    path('search_employee', views.search_employee),

]