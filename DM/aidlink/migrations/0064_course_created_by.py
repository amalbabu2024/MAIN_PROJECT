# Generated by Django 4.2.5 on 2024-03-14 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0063_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
