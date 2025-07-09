# URL routing for the main PlotTogether App. Any request always first heads towards here.

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("/api/")),  # Redirect root URL to /api/
    path("api/", include("api.urls")),  # Include API routes for REST API
    path("admin/", admin.site.urls),  # Admin panel
]