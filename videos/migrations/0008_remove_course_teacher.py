# Generated by Django 3.0.10 on 2021-04-01 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20210331_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='teacher',
        ),
    ]
