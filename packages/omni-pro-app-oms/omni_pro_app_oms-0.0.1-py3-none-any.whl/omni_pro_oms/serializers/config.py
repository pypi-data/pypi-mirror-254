from rest_framework import serializers

from omni_pro_oms.models import Config


class ConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"
