# Generated by Django 4.0.1 on 2022-01-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foydalanuvchi', '0062_hisobot_full_valyuta'),
    ]

    operations = [
        migrations.AddField(
            model_name='hisobot_full',
            name='tur',
            field=models.CharField(blank=True, default=0, max_length=255, verbose_name='Chart va Birlik'),
        ),
    ]
