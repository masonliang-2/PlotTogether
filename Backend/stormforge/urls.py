from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

def api_root(request):
    return JsonResponse({"message": "Stormforge API root"})

def home_redirect(request):
    return redirect("/api/")

urlpatterns = [
    path("api/", api_root),  # Handles `/api/` root directly
    path("", home_redirect, name="home_redirect"),  # Redirect root URL to /api/
    path("api/", include("api.urls")),  # Include API routes
    path("admin/", admin.site.urls),  # Admin panel
]