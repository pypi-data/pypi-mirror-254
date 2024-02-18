from django import forms
from django_json_widget.widgets import JSONEditorWidget

from omni_pro_oms.models import Config


class ConfigAdminForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = "__all__"
        widgets = {
            "auth": JSONEditorWidget,
            "token": JSONEditorWidget,
        }
