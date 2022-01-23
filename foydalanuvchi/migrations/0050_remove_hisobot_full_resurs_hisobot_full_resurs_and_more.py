# Generated by Django 4.0.1 on 2022-01-23 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foydalanuvchi', '0049_manyfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hisobot_full',
            name='resurs',
        ),
        migrations.AddField(
            model_name='hisobot_full',
            name='resurs',
            field=models.ManyToManyField(to='foydalanuvchi.his_ich', verbose_name='Resurslar'),
        ),
        migrations.DeleteModel(
            name='manyfield',
        ),
    ]
