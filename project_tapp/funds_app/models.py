import uuid

from django.db import models

# Create your models here.
class Funds(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    amount = models.FloatField(null=True)

    class Meta:
        verbose_name_plural = 'Funds'