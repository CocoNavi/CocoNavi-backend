# Generated by Django 3.0.8 on 2020-08-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]