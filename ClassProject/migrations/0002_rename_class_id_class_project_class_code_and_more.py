# Generated by Django 5.0.7 on 2024-07-19 12:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassProject', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class_project',
            old_name='class_id',
            new_name='class_code',
        ),
        migrations.RenameField(
            model_name='class_project',
            old_name='class_description',
            new_name='class_goals',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_capacity',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_end_date',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_location',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_start_date',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_status',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_students',
        ),
        migrations.RemoveField(
            model_name='class_project',
            name='class_time',
        ),
        migrations.AddField(
            model_name='class_project',
            name='class_meeting',
            field=models.CharField(default='Monday', max_length=100),
        ),
        migrations.AddField(
            model_name='class_project',
            name='class_representative',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='class_project',
            name='no_of_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='class_project',
            name='no_of_tables',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='class_project',
            name='period_entity',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_project',
            name='room_allocation',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class_project',
            name='class_name',
            field=models.CharField(max_length=100),
        ),
    ]