from rest_framework import serializers

from omni_pro_oms.models import TenantOperation


class TenantOperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TenantOperation
        fields = "__all__"
