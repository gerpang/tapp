import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from funds_app.models import Funds
from people_app.utils.enum_classes import ClusterEnums

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Cluster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster_name = models.CharField(max_length=200, choices=ClusterEnums.choices())
    funds = models.ForeignKey(Funds, on_delete=models.SET_NULL, null=True)


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cluster = models.ManyToManyField(Cluster)

