from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    camera_create,
    camera_delete,
    camera_edit,
    camera_list,
    camera_start,
    camera_status,
    camera_stop,
    index,
    motion_event_list,
    stream_view,
)

urlpatterns = [
    path("", index, name="home"),
    path("cameras/", camera_list, name="camera_list"),
    path("cameras/add/", camera_create, name="camera_create"),
    path("cameras/<int:pk>/edit/", camera_edit, name="camera_edit"),
    path("cameras/<int:pk>/delete/", camera_delete, name="camera_delete"),
    path("cameras/<int:pk>/status/", camera_status, name="camera_status"),
    path("cameras/<int:pk>/start/", camera_start, name="camera_start"),
    path("cameras/<int:pk>/stop/", camera_stop, name="camera_stop"),
    path("cameras/<int:pk>/stream/", stream_view, name="camera_stream"),
    path("events/", motion_event_list, name="motion_event_list"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)