# Generated by Django 2.2.2 on 2019-06-24 00:52

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20190623_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]
