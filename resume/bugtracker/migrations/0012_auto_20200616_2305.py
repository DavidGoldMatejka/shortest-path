# Generated by Django 3.0.4 on 2020-06-17 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0011_post_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='project',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
