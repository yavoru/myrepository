# Generated by Django 5.0.3 on 2024-04-17 11:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_account_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AddField(
            model_name='account',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]