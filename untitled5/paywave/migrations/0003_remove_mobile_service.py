# Generated by Django 2.1.7 on 2019-04-03 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0002_auto_20190403_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='service',
        ),
    ]
