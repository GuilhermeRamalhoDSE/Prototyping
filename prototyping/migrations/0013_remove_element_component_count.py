# Generated by Django 5.0.2 on 2024-03-11 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0012_componentrelease'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='component_count',
        ),
    ]
