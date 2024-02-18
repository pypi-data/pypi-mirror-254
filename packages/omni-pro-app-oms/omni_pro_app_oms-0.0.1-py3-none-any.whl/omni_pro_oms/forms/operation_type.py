from django import forms

from omni_pro_oms.models import OperationType


class OperationTypeAdminForm(forms.ModelForm):
    class Meta:
        model = OperationType
        fields = "__all__"
