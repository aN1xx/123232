from django.db import models
from django.dispatch import receiver


class Sample(models.Model):
    file = models.FileField(upload_to='samples', max_length=100000, null=True)
    text = models.TextField(blank=True)

    class Meta:
        app_label = 'documentconverter'