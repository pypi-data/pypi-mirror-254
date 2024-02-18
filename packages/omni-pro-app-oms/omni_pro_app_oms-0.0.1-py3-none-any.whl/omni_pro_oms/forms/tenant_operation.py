from django import forms

from omni_pro_oms.models import TenantOperation


class TenantOperationAdminForm(forms.ModelForm):
    class Meta:
        model = TenantOperation
        fields = "__all__"
