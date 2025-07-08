from django.urls import path
from . import views
from .views import handleCRUD, get_data_points

urlpatterns = [
    path('crud/', handleCRUD, name='handleCRUD'),
    path('get-data-points/', get_data_points, name='get_data_points'),
    path('get-analysis', views.get_analysis, name='get_analysis'),
    ]