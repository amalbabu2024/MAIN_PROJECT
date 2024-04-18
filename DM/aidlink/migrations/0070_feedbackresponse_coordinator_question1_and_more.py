# Generated by Django 4.2.5 on 2024-03-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0069_user_organization_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='coordinator_question9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='manager_question9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='no_disclosure_question9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_leader_question9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='team_member_question9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedbackresponse',
            name='unregistered_question9',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question10',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question7',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question8',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedbackresponse',
            name='civilian_question9',
            field=models.TextField(blank=True, null=True),
        ),
    ]
