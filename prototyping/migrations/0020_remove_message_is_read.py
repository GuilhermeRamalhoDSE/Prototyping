# Generated by Django 5.0.2 on 2024-03-26 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0019_message_is_read_delete_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_read',
        ),
    ]
