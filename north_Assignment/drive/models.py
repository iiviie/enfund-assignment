from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DriveFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='drive_files')
    file_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=100)
    size = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.file_id})"
