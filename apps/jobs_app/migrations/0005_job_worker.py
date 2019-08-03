# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-02 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_dashboard_app', '0001_initial'),
        ('jobs_app', '0004_auto_20190802_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='login_dashboard_app.User'),
        ),
    ]
