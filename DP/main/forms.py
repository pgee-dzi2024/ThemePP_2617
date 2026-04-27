from django import forms
from .models import CameraSource


class CameraSourceForm(forms.ModelForm):
    class Meta:
        model = CameraSource
        fields = [
            "name",
            "source_type",
            "stream_url",
            "device_index",
            "is_active",
            "sensitivity_threshold",
            "min_area",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "source_type": forms.Select(attrs={"class": "form-select"}),
            "stream_url": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "rtsp://user:pass@192.168.100.110:554/...",
                }
            ),
            "device_index": forms.NumberInput(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "sensitivity_threshold": forms.NumberInput(attrs={"class": "form-control"}),
            "min_area": forms.NumberInput(attrs={"class": "form-control"}),
        }