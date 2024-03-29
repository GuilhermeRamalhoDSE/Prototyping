# Generated by Django 5.0.2 on 2024-02-27 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototyping', '0002_chassis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand', models.CharField(choices=[('left', 'sinistra'), ('right', 'destra')], max_length=10, verbose_name='mano')),
                ('mac_address', models.CharField(max_length=17, verbose_name='indirizzo MAC')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prototyping.license', verbose_name='licenza')),
            ],
            options={
                'verbose_name': 'Aptica',
                'verbose_name_plural': 'Aptiche',
            },
        ),
    ]
