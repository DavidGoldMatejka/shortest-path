# Generated by Django 3.0.4 on 2020-06-17 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0013_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bugtracker.Projects'),
            preserve_default=False,
        ),
    ]
