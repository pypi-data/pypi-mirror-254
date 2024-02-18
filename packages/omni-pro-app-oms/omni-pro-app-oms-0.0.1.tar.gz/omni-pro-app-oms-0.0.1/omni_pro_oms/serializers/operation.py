from rest_framework import serializers

from omni_pro_oms.models import Operation


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = "__all__"
