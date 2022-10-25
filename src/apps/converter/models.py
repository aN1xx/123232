from django.db import models


class Sample(models.Model):
    filename = models.CharField(max_length=20)
    file = models.FileField()

    class Meta:
        app_label = 'converter'
