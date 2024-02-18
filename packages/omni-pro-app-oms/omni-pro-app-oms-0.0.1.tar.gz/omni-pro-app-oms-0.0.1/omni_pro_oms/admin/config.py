from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from omni_pro_base.admin import BaseAdmin

from omni_pro_oms.forms import ConfigAdminForm
from omni_pro_oms.models import Config


class ConfigAdmin(BaseAdmin):
    list_display = ("base_url", "auth", "token")
    list_filter = ("base_url",)
    search_fields = ("base_url",)
    form = ConfigAdminForm

    def __init__(self, *args, **kwargs):
        super(ConfigAdmin, self).__init__(*args, **kwargs)
        self.fieldsets = (
            (_("Config"), {"fields": ("name", "base_url")}),
            (_("Auth"), {"fields": ("auth",)}),
            (_("Token"), {"fields": ("token",)}),
        ) + self.fieldsets


admin.site.register(Config, ConfigAdmin)
