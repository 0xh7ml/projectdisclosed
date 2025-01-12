# Generated by Django 5.0.3 on 2024-03-22 06:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_report_completed_by_report_is_read_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='completed_by',
        ),
        migrations.RemoveField(
            model_name='report',
            name='is_read',
        ),
        migrations.CreateModel(
            name='ReportReadStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.report')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
