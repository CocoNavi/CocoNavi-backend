# Generated by Django 3.0.8 on 2020-07-30 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='pet_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='pet_avatars'),
        ),
    ]