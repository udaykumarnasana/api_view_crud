from rest_framework import serializers
from app.models import *


class pcserializers(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'