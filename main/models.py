from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    
    report_id = models.IntegerField()
    title = models.CharField(max_length=255)
    cwe = models.CharField(max_length=255)
    severity = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default="resolved")
    url = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.title} {self.is_read}'
