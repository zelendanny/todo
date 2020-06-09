from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=300, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_at = models.DateTimeField(null=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True)

    def save(self, **kwargs):
        self.completed_at = datetime.now() if self.is_completed else None
        super().save(**kwargs)
