# Generated by Django 3.0.8 on 2020-08-04 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0004_auto_20200731_1752'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('year', models.CharField(default=1, max_length=4)),
                ('month', models.CharField(default=1, max_length=2)),
                ('date', models.CharField(default=1, max_length=2)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayEvents', to='pets.Pet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dayEvents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
