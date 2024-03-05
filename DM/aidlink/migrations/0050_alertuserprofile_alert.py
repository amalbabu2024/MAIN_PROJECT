# Generated by Django 4.2.5 on 2024-03-02 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0049_task_status_delete_taskstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_email_alerts', models.BooleanField(default=True)),
                ('receive_popup_alerts', models.BooleanField(default=True)),
                ('receive_dashboard_alerts', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_type', models.CharField(choices=[('POPUP', 'Popup Message'), ('DASHBOARD', 'Dashboard Message'), ('EMAIL', 'Email')], max_length=10)),
                ('priority', models.CharField(choices=[('HIGH', 'High'), ('MEDIUM', 'Medium'), ('LOW', 'Low')], max_length=10)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('recipients', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
