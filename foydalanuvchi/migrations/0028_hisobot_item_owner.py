# Generated by Django 4.0.1 on 2022-01-19 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foydalanuvchi', '0027_remove_hisobot_item_hisobot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hisobot_item',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
