from django.urls import path
from . import views
from .views import handleCRUD, get_data_points

def api_root(request):
    return JsonResponse({"message": "Plottogether API root"})

urlpatterns = [
    path("api/", api_root),  # Handles `/api/` root directly
    path('crud/', handleCRUD, name='handleCRUD'),
    path('get-data-points/', get_data_points, name='get_data_points'),
    path('get-analysis', views.get_analysis, name='get_analysis'),
    ]