# Generated by Django 2.2.2 on 2019-06-21 22:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190621_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, null=True),
        ),
    ]