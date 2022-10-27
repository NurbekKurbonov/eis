# Generated by Django 4.0.5 on 2022-10-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minenergiya', '0014_alter_klassifikator_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ensamfiltr',
            name='resurs',
        ),
        migrations.AddField(
            model_name='ensamfiltr',
            name='E_ID',
            field=models.TextField(blank=True, unique=True, verbose_name='E_ID'),
        ),
        migrations.AddField(
            model_name='guruh',
            name='E_ID',
            field=models.TextField(blank=True, unique=True, verbose_name='E_ID'),
        ),
        migrations.AddField(
            model_name='klassifikator',
            name='E_ID',
            field=models.TextField(blank=True, unique=True, verbose_name='E_ID'),
        ),
        migrations.AddField(
            model_name='tur',
            name='E_ID',
            field=models.TextField(blank=True, unique=True, verbose_name='E_ID'),
        ),
    ]
