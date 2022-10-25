from django.shortcuts import render
from .models import Sample
from .serializer import SampleAPISerializer
from rest_framework import viewsets


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleAPISerializer
