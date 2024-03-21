from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Report(models.Model):
    report_id =  models.IntegerField()
    title = models.CharField(max_length=255)
    cwe = models.CharField(max_length=255)
    severity = models.CharField(max_length=255)
    state = models.CharField(max_length=255, default="resolved")
    url = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class ReportReadStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, null=True, blank=True)
    is_read = models.BooleanField(default=False)