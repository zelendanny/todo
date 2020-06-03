from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=300, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_at = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True)
