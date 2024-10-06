from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("task.urls")),
    # api urls
    path("task/api/", include("task.api.urls")),
]
