# Generated by Django 5.0.2 on 2024-03-18 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0015_component_component_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
