from django.urls import path

from .views import sync_data, clear_data, get_report

urlpatterns = [
    path("sync/", sync_data),
    path("clear/", clear_data),
    path("report/", get_report),
]
