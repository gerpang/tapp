import uuid

from django.db import models

# Create your models here.
from people_app.models import User, Institution
from timesheet_app.utils.enum_classes import StatusEnums


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ManyToManyField(Institution)
    project_code = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)
    fy = models.DateField(auto_created=False, null=True)
    project_status = models.CharField(choices=StatusEnums.choices(), max_length=200) # temp

    def __str__(self):
        return self.project_name

class Timesheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    time_start = models.DateTimeField(null=True, auto_now_add=False)
    time_end = models.DateTimeField(null=True, auto_now_add=False)
