# Generated by Django 2.1.7 on 2019-04-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0010_mobiles_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='service_type',
            field=models.CharField(choices=[('prepaid', 'prepaid'), ('postpaid', 'postpaid')], max_length=128),
        ),
    ]
