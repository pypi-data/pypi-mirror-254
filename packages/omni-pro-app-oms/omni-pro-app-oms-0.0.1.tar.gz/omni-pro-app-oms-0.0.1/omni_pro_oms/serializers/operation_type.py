from rest_framework import serializers

from omni_pro_oms.models import OperationType


class OperationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperationType
        fields = "__all__"
