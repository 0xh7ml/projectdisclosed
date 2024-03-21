# Generated by Django 5.0.3 on 2024-03-21 10:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_reports_report'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='status',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user',
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