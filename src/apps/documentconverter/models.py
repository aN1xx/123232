from django.db import models


class Sample(models.Model):
    file = models.FileField(upload_to='samples', max_length=100000, null=True)
    text = models.TextField(blank=True)

    class Meta:
        app_label = 'documentconverter'
