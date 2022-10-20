from django.db import models
from django.dispatch import receiver


class Sample(models.Model):
    file = models.FileField(upload_to='samples', max_length=100000, null=True)

    class Meta:
        app_label = 'documentconverter'


# Define Chapter model
class Chapter(models.Model):
    title = models.CharField(max_length=255, null=False)
    text = models.TextField(blank=True, null=True)
    document = models.ForeignKey(Sample, related_name='chapters', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        app_label = 'documentconverter'
