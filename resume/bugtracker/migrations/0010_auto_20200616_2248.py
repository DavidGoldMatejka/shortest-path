# Generated by Django 3.0.4 on 2020-06-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0009_auto_20200615_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High')], default=1),
        ),
    ]
