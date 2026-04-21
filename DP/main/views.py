from django.contrib import messages
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CameraSourceForm
from .models import CameraSource, MotionEvent
from .services import CameraStreamService


def index(request):
    camera = CameraSource.objects.filter(is_active=True).first()
    latest_events = MotionEvent.objects.select_related("camera").all()[:10]

    status = None
    if camera:
        service = CameraStreamService(camera)
        status = service.get_status()

    context = {
        "camera": camera,
        "latest_events": latest_events,
        "camera_count": CameraSource.objects.count(),
        "active_camera_count": CameraSource.objects.filter(is_active=True).count(),
        "status": status,
    }
    return render(request, "main/index.html", context)


def camera_list(request):
    cameras = CameraSource.objects.all().order_by("-created_at")
    return render(request, "main/camera_list.html", {"cameras": cameras})


def camera_create(request):
    if request.method == "POST":
        form = CameraSourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Видео източникът е записан успешно.")
            return redirect("camera_list")
    else:
        form = CameraSourceForm()

    return render(request, "main/camera_form.html", {"form": form})


def camera_edit(request, pk):
    camera = get_object_or_404(CameraSource, pk=pk)
    if request.method == "POST":
        form = CameraSourceForm(request.POST, instance=camera)
        if form.is_valid():
            form.save()
            messages.success(request, "Видео източникът е обновен успешно.")
            return redirect("camera_list")
    else:
        form = CameraSourceForm(instance=camera)

    return render(request, "main/camera_form.html", {"form": form, "camera": camera})


def camera_delete(request, pk):
    camera = get_object_or_404(CameraSource, pk=pk)
    if request.method == "POST":
        camera.delete()
        messages.success(request, "Видео източникът е изтрит.")
        return redirect("camera_list")

    return render(request, "main/camera_delete.html", {"camera": camera})


def stream_view(request, pk):
    camera = get_object_or_404(CameraSource, pk=pk)
    service = CameraStreamService(camera)

    try:
        return StreamingHttpResponse(
            service.generate_mjpeg(),
            content_type="multipart/x-mixed-replace; boundary=frame",
        )
    except RuntimeError as exc:
        return HttpResponse(f"Stream error: {exc}", status=400)


def camera_status(request, pk):
    camera = get_object_or_404(CameraSource, pk=pk)
    service = CameraStreamService(camera)
    status = service.get_status()

    return render(
        request,
        "main/camera_status.html",
        {
            "camera": camera,
            "status": status,
        },
    )


def camera_start(request, pk):
    camera = get_object_or_404(CameraSource, pk=pk)
    camera.is_active = True
    camera.save(update_fields=["is_active", "updated_at"])
    messages.success(request, f"Камера '{camera.name}' е стартирана.")
    return redirect("camera_status", pk=pk)


def camera_stop(request, pk):
    camera = get_object_or_404(CameraSource, pk=pk)
    camera.is_active = False
    camera.save(update_fields=["is_active", "updated_at"])
    messages.success(request, f"Камера '{camera.name}' е спряна.")
    return redirect("camera_status", pk=pk)


def motion_event_list(request):
    camera_id = request.GET.get("camera")
    events = MotionEvent.objects.select_related("camera").all()

    if camera_id:
        events = events.filter(camera_id=camera_id)

    events = events[:100]
    cameras = CameraSource.objects.all().order_by("name")

    return render(
        request,
        "main/motion_event_list.html",
        {
            "events": events,
            "cameras": cameras,
            "selected_camera_id": camera_id,
        },
    )


def api_motion_events_latest(request):
    camera_id = request.GET.get("camera")
    events = MotionEvent.objects.select_related("camera").all()

    if camera_id:
        events = events.filter(camera_id=camera_id)

    data = [
        {
            "id": event.id,
            "camera_id": event.camera_id,
            "camera_name": event.camera.name,
            "detected_at": event.detected_at,
            "message": event.message,
            "frame_path": event.frame_path,
        }
        for event in events[:50]
    ]
    return JsonResponse({"results": data})