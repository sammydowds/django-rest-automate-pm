# Generated by Django 3.0.7 on 2020-06-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restautomatepm', '0009_auto_20200623_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
