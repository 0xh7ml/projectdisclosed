# Generated by Django 5.0.3 on 2024-03-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_report_status_remove_report_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='state',
            field=models.CharField(default='resolved', max_length=255),
        ),
    ]
