# Generated by Django 5.1.2 on 2024-12-11 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_course_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='class_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.class'),
        ),
    ]
