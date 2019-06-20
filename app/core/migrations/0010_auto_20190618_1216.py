# Generated by Django 2.2.2 on 2019-06-18 12:16

import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190618_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=django.contrib.postgres.fields.citext.CICharField(db_index=True, error_messages={'unique': 'Category name already exists'}, max_length=50, unique=True),
        ),
    ]
