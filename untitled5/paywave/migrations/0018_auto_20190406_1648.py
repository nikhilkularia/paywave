# Generated by Django 2.1.7 on 2019-04-06 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0017_dthcard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dthcard',
            old_name='custmoerid',
            new_name='customerid',
        ),
        migrations.RemoveField(
            model_name='dthcard',
            name='amount',
        ),
    ]
