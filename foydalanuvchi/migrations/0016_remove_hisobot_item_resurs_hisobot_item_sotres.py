# Generated by Django 4.0.1 on 2022-01-17 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foydalanuvchi', '0015_remove_hisobot_item_sotres_hisobot_item_resurs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hisobot_item',
            name='resurs',
        ),
        migrations.AddField(
            model_name='hisobot_item',
            name='sotres',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='foydalanuvchi.sotres', unique=True),
            preserve_default=False,
        ),
    ]
