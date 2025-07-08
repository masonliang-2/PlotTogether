"""
URL configuration for stormforge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

def api_root(request):
    return JsonResponse({"message": "Stormforge API root"})

def home_redirect(request):
    return redirect("/api/")

urlpatterns = [
    path("", home_redirect, name="home_redirect"),  # Redirect root URL to /api/
    path("api/", api_root),  # 👈 This handles `/api/` directly
    path("api/", include("api.urls")),  # Include API routes
    path("admin/", admin.site.urls),  # Admin panel
]