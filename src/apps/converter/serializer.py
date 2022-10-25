from rest_framework import serializers

from .models import Sample


class SampleAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('filename', 'file')
