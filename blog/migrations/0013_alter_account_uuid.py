# Generated by Django 5.0.3 on 2024-04-17 12:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_account_id_account_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False),
        ),
    ]