# Generated by Django 4.2.5 on 2023-11-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0011_camp_camp_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camp',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
