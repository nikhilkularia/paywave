# Generated by Django 2.1.7 on 2019-04-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paywave', '0023_auto_20190406_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='creditcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('name_on_card', models.CharField(max_length=128)),
                ('card_number', models.IntegerField()),
                ('expire_month', models.SmallIntegerField()),
                ('expire_year', models.SmallIntegerField()),
                ('cvv_number', models.SmallIntegerField()),
            ],
        ),
    ]
