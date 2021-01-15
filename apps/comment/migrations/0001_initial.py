# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2020-12-24 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='提示时间')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='the_comment', to='comment.ArticleComment', verbose_name='所属评论')),
            ],
            options={
                'verbose_name': '提示信息',
                'verbose_name_plural': '提示信息',
                'ordering': ['-create_date'],
            },
        ),
    ]
