# Generated by Django 4.2.2 on 2023-07-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_comment_task_alter_comment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
