import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class People(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Cluster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster_name = models.CharField(max_length=200)