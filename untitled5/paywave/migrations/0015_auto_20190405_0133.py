# Generated by Django 2.1.7 on 2019-04-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0014_auto_20190404_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='service_type',
            field=models.BooleanField(),
        ),
    ]