# Generated by Django 2.1.7 on 2019-04-03 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0004_mobile_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='service',
        ),
    ]