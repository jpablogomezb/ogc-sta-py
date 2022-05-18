from rest_framework import serializers

from .models import Thing


class ThingSerializer(serializers.ModelSerializer):
    iot = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Thing
        fields = [
            'name',
            'description',
            'properties',
            'iot'
        ]
    
    def get_iot(self, obj):
        if not isinstance(obj, Thing):
            return None
        return obj.iot_id
