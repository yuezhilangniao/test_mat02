# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-02 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('month', models.IntegerField(verbose_name='月份')),
                ('yeji', models.FloatField(verbose_name='业绩')),
                ('huikuan', models.FloatField(verbose_name='回款')),
                ('hetong', models.FloatField(verbose_name='合同')),
                ('sex', models.BooleanField(default=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'byzoro_man',
                'verbose_name_plural': '员工表',
                'verbose_name': '员工表',
            },
        ),
        migrations.CreateModel(
            name='PartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateField()),
                ('bread', models.IntegerField(default=0)),
                ('bcomment', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'byzoro_part',
                'verbose_name_plural': '部门表',
                'verbose_name': '部门表',
            },
        ),
        migrations.AddField(
            model_name='maninfo',
            name='mpart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demomat.PartInfo'),
        ),
    ]