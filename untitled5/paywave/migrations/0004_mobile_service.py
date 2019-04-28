# Generated by Django 2.1.7 on 2019-04-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0003_remove_mobile_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='service',
            field=models.CharField(choices=[('prepaid', 'prepaid'), ('postpaid', 'postpaid')], default=-1.0, max_length=128),
            preserve_default=False,
        ),
    ]
