# Generated by Django 5.1.2 on 2024-12-11 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_course_chapter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.course'),
        ),
    ]
