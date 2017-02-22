# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-22 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_fw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_file', models.CharField(max_length=50)),
                ('ln_nr', models.IntegerField()),
                ('cl_address_ul', models.CharField(max_length=50)),
                ('cl_address_nr_d', models.CharField(max_length=50)),
                ('cl_address_nr_m', models.CharField(max_length=50)),
                ('cl_address_rest', models.CharField(max_length=50)),
                ('mac', models.CharField(max_length=17)),
                ('ip_add', models.CharField(max_length=15)),
                ('kl_service', models.CharField(max_length=1)),
                ('downl', models.CharField(max_length=6)),
                ('upl', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'LAN_Client_fw',
            },
        ),
    ]