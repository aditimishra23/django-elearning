# Generated by Django 3.0.10 on 2021-03-25 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20210319_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='timestamp',
        ),
    ]
