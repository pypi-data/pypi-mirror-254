from django import forms
from django_json_widget.widgets import JSONEditorWidget

from omni_pro_oms.models import Operation


class OperationAdminForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = "__all__"
        widgets = {
            "headers": JSONEditorWidget,
        }
