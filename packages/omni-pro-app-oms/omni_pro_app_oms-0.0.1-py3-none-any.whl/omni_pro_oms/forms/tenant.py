from django import forms

from omni_pro_oms.models import Tenant


class TenantAdminForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = "__all__"
