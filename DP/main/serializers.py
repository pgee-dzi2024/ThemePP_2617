from rest_framework import serializers

from .models import CameraSource, MotionEvent


class CameraSourceSerializer(serializers.ModelSerializer):
    source_type_display = serializers.CharField(source="get_source_type_display", read_only=True)

    class Meta:
        model = CameraSource
        fields = [
            "id",
            "name",
            "source_type",
            "source_type_display",
            "stream_url",
            "device_index",
            "is_active",
            "sensitivity_threshold",
            "min_area",
            "created_at",
            "updated_at",
        ]


class MotionEventSerializer(serializers.ModelSerializer):
    camera_name = serializers.CharField(source="camera.name", read_only=True)

    class Meta:
        model = MotionEvent
        fields = [
            "id",
            "camera",
            "camera_name",
            "detected_at",
            "message",
            "frame_path",
        ]