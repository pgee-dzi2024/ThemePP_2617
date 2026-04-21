from django.db import models


class CameraSource(models.Model):
    """
    Видео източник за наблюдение.
    Може да е локална камера или IP камера/stream URL.
    """

    SOURCE_TYPES = (
        ("local", "Local camera"),
        ("ip", "IP camera / Stream URL"),
    )

    name = models.CharField(max_length=120, verbose_name="Име")
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES, default="local")
    stream_url = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Stream URL",
        help_text="Поддържа rtsp://, http:// или https:// адрес.",
    )
    device_index = models.PositiveIntegerField(
        default=0,
        verbose_name="Device index",
        help_text="0 = default webcam",
    )
    is_active = models.BooleanField(default=False, verbose_name="Активна")
    sensitivity_threshold = models.PositiveIntegerField(
        default=25,
        verbose_name="Праг на чувствителност",
        help_text="Колкото е по-ниско, толкова по-чувствителна е детекцията.",
    )
    min_area = models.PositiveIntegerField(
        default=500,
        verbose_name="Минимална площ",
        help_text="Филтър срещу шум и дребни промени.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Видео източник"
        verbose_name_plural = "Видео източници"

    def __str__(self):
        return self.name


class MotionEvent(models.Model):
    """
    Лог на събития при засечено движение.
    """

    camera = models.ForeignKey(CameraSource, on_delete=models.CASCADE, related_name="motion_events")
    detected_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255, default="Движение засечено")
    frame_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Събитие при движение"
        verbose_name_plural = "Събития при движение"
        ordering = ["-detected_at"]

    def __str__(self):
        return f"{self.camera.name} - {self.detected_at:%Y-%m-%d %H:%M:%S}"