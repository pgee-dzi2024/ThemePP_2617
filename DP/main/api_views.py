from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import CameraSource, MotionEvent
from .serializers import CameraSourceSerializer, MotionEventSerializer
from .services import CameraStreamService


@api_view(["GET"])
def api_camera_list(request):
    cameras = CameraSource.objects.all().order_by("-created_at")
    serializer = CameraSourceSerializer(cameras, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def api_camera_detail(request, pk):
    try:
        camera = CameraSource.objects.get(pk=pk)
    except CameraSource.DoesNotExist:
        return Response({"detail": "Camera not found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = CameraSourceSerializer(camera)
    return Response(serializer.data)


@api_view(["GET"])
def api_motion_events(request):
    camera_id = request.query_params.get("camera")
    events = MotionEvent.objects.select_related("camera").all()

    if camera_id:
        events = events.filter(camera_id=camera_id)

    events = events[:50]
    serializer = MotionEventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def api_camera_status(request, pk):
    try:
        camera = CameraSource.objects.get(pk=pk)
    except CameraSource.DoesNotExist:
        return Response({"detail": "Camera not found."}, status=status.HTTP_404_NOT_FOUND)

    service = CameraStreamService(camera)
    status_data = service.get_status()

    return Response(
        {
            "camera_id": camera.id,
            "camera_name": camera.name,
            "connected": status_data.connected,
            "error": status_data.error,
            "fps": status_data.fps,
            "latency_ms": status_data.latency_ms,
            "is_active": camera.is_active,
        }
    )


@api_view(["POST"])
def api_camera_start(request, pk):
    try:
        camera = CameraSource.objects.get(pk=pk)
    except CameraSource.DoesNotExist:
        return Response({"detail": "Camera not found."}, status=status.HTTP_404_NOT_FOUND)

    camera.is_active = True
    camera.save(update_fields=["is_active", "updated_at"])

    return Response(
        {
            "detail": f"Camera '{camera.name}' started.",
            "camera_id": camera.id,
            "is_active": camera.is_active,
        }
    )


@api_view(["POST"])
def api_camera_stop(request, pk):
    try:
        camera = CameraSource.objects.get(pk=pk)
    except CameraSource.DoesNotExist:
        return Response({"detail": "Camera not found."}, status=status.HTTP_404_NOT_FOUND)

    camera.is_active = False
    camera.save(update_fields=["is_active", "updated_at"])

    return Response(
        {
            "detail": f"Camera '{camera.name}' stopped.",
            "camera_id": camera.id,
            "is_active": camera.is_active,
        }
    )
