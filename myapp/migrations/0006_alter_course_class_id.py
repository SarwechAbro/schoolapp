# Generated by Django 5.1.2 on 2024-12-11 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_chapter_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='class_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.class'),
        ),
    ]
