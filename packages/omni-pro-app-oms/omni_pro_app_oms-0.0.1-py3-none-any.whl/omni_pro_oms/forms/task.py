from django import forms
from django_json_widget.widgets import JSONEditorWidget

from omni_pro_oms.models import Task


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "body_src": JSONEditorWidget,
            "headers_src": JSONEditorWidget,
            "params_src": JSONEditorWidget,
            "response_src": JSONEditorWidget,
            "body_dst": JSONEditorWidget,
            "headers_dst": JSONEditorWidget,
            "params_dst": JSONEditorWidget,
            "response_dst": JSONEditorWidget,
        }
