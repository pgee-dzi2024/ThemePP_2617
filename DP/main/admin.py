from django.contrib import admin
from .models import CameraSource, MotionEvent


@admin.register(CameraSource)
class CameraSourceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "source_type",
        "stream_url",
        "device_index",
        "is_active",
        "sensitivity_threshold",
        "min_area",
        "created_at",
    )
    list_filter = ("source_type", "is_active", "created_at")
    search_fields = ("name", "stream_url")
    ordering = ("-created_at",)


@admin.register(MotionEvent)
class MotionEventAdmin(admin.ModelAdmin):
    list_display = ("camera", "detected_at", "message", "frame_path")
    list_filter = ("detected_at", "camera")
    search_fields = ("camera__name", "message")
    ordering = ("-detected_at",)