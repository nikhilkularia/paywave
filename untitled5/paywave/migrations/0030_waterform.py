# Generated by Django 2.1.7 on 2019-04-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0029_auto_20190407_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='waterform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_operator', models.CharField(max_length=128)),
                ('wnumber', models.CharField(max_length=20)),
            ],
        ),
    ]