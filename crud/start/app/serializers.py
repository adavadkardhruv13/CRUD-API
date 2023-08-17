from .models import Crop
from rest_framework import serializers

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields ='__all__'