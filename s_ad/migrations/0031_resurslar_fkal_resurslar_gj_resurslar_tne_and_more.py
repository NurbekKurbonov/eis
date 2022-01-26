# Generated by Django 4.0.1 on 2022-01-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_ad', '0030_alter_valyuta_checker'),
    ]

    operations = [
        migrations.AddField(
            model_name='resurslar',
            name='fkal',
            field=models.FloatField(blank=True, default=0.0, verbose_name='TSHY'),
        ),
        migrations.AddField(
            model_name='resurslar',
            name='gj',
            field=models.FloatField(blank=True, default=0.0, verbose_name='TSHY'),
        ),
        migrations.AddField(
            model_name='resurslar',
            name='tne',
            field=models.FloatField(blank=True, default=0.0, verbose_name='TNE'),
        ),
        migrations.AddField(
            model_name='resurslar',
            name='tshy',
            field=models.FloatField(blank=True, default=0.0, verbose_name='TSHY'),
        ),
    ]
