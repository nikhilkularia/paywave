# Generated by Django 2.1.7 on 2019-04-07 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0025_auto_20190407_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='eletricity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_provider', models.CharField(max_length=128)),
                ('elec_customer_id', models.CharField(max_length=20)),
            ],
        ),
    ]