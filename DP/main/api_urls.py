from django.urls import path

from .api_views import (
    api_camera_detail,
    api_camera_list,
    api_camera_start,
    api_camera_status,
    api_camera_stop,
    api_motion_events,
)

urlpatterns = [
    path("cameras/", api_camera_list, name="api_camera_list"),
    path("cameras/<int:pk>/", api_camera_detail, name="api_camera_detail"),
    path("cameras/<int:pk>/status/", api_camera_status, name="api_camera_status"),
    path("cameras/<int:pk>/start/", api_camera_start, name="api_camera_start"),
    path("cameras/<int:pk>/stop/", api_camera_stop, name="api_camera_stop"),
    path("events/", api_motion_events, name="api_motion_events"),
]