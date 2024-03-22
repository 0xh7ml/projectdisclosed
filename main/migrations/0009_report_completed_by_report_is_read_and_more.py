# Generated by Django 5.0.3 on 2024-03-22 08:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_report_completed_by_remove_report_is_read_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='completed_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='completed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='ReportReadStatus',
        ),
    ]