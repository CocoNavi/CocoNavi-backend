# Generated by Django 3.0.8 on 2020-07-30 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=500)),
                ('pet_kind', models.CharField(blank=True, choices=[('고양이', '고양이'), ('강아지', '강아지')], default='강아지', max_length=15, null=True)),
                ('pet_age', models.IntegerField(blank=True, null=True)),
                ('dog_kind', models.CharField(blank=True, choices=[('말티즈', '말티즈'), ('푸들', '푸들'), ('포메라니안', '포메라니안'), ('시츄', '시츄'), ('비숑', '비숑'), ('요크셔테리어', '여크셔테리어'), ('치와와', '치와와'), ('스피츠', '스피츠'), ('믹스견', '믹스견'), ('닥스훈트', '닥스훈트'), ('진도견', '진도견'), ('웰시코기', '웰시코기'), ('시바견', '시바견')], max_length=15, null=True)),
                ('cat_kind', models.CharField(blank=True, choices=[('스코티쉬폴드', '스코티쉬폴드'), ('러시안블루', '러시안블루'), ('먼치킨', '먼치킨'), ('페르시안', '페르시안'), ('샴', '샴'), ('뱅갈', '뱅갈'), ('브리티쉬숏헤어', '브리티쉬숏헤어'), ('터키쉬앙고라', '터키쉬앙고라'), ('아비시니안', '아비시니안'), ('믹스', '믹스')], max_length=15, null=True)),
                ('district_korea', models.CharField(choices=[('서울특별시', '서울특별시'), ('부산광역시', '부산광역시'), ('인천광역시', '인천광역시'), ('대구광역시', '대구광역시'), ('광주광역시', '광주광역시'), ('대전광역시', '대전광역시'), ('울산광역시', '울산광역시'), ('세종특별자치시', '세종특별자치시'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('제주특별자치도', '제주특별자치도')], max_length=15)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='boards.Board')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.ImageField(upload_to='posts_photos')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_photos', to='posts.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
