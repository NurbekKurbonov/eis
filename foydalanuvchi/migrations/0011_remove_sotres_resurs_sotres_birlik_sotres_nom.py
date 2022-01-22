# Generated by Django 4.0.1 on 2022-01-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foydalanuvchi', '0010_remove_sotres_birlik_remove_sotres_nom_sotres_resurs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sotres',
            name='resurs',
        ),
        migrations.AddField(
            model_name='sotres',
            name='birlik',
            field=models.CharField(default=1, max_length=100, verbose_name='Resurs birligi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sotres',
            name='nom',
            field=models.TextField(default=1, max_length=100, unique=True, verbose_name='Resurs nomi'),
            preserve_default=False,
        ),
    ]
