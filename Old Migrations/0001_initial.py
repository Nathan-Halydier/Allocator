# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-11 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField(default=django.utils.timezone.now)),
                ('allocated_hours', models.IntegerField(default=0)),
                ('actual_hours', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_name', models.CharField(max_length=150)),
                ('holiday_date', models.DateField()),
                ('hours_lost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pw_string', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('pm_scope', models.IntegerField()),
                ('dev_scope', models.IntegerField()),
                ('design_scope', models.IntegerField()),
                ('testing_scope', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=150)),
                ('active', models.BooleanField()),
                ('email_address', models.EmailField(max_length=254)),
                ('weekly_copacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(choices=[(6, '6AM'), (7, '7AM'), (8, '8AM'), (9, '9AM'), (10, '10AM'), (11, '11AM'), (12, '12PM'), (13, '1PM'), (14, '2PM'), (15, '3PM'), (16, '4PM'), (17, '5PM'), (18, '6PM')], default=8)),
                ('end_time', models.IntegerField(choices=[(6, '6AM'), (7, '7AM'), (8, '8AM'), (9, '9AM'), (10, '10AM'), (11, '11AM'), (12, '12PM'), (13, '1PM'), (14, '2PM'), (15, '3PM'), (16, '4PM'), (17, '5PM'), (18, '6PM')], default=17)),
                ('lunch', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_name', models.CharField(max_length=250)),
                ('setting_int', models.IntegerField(null=True)),
                ('setting_bool', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Time_Off',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hours_lost', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='User_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Workdays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(choices=[('Sun', 'Sunday'), ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], default='Mon', max_length=10)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Workdays'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Resource'),
        ),
        migrations.AddField(
            model_name='resource',
            name='resource_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Resource_Type'),
        ),
        migrations.AddField(
            model_name='resource',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.User_Type'),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Project_Type'),
        ),
        migrations.AddField(
            model_name='passwords',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Resource'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Project'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='copacity.Resource'),
        ),
    ]
