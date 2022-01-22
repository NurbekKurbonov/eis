# Generated by Django 4.0.1 on 2022-01-17 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_ad', '0027_alter_resurslar_nomi'),
        ('foydalanuvchi', '0014_hisobot_hisobot_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hisobot_item',
            name='sotres',
        ),
        migrations.AddField(
            model_name='hisobot_item',
            name='resurs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='s_ad.resurslar', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sotres',
            name='resurs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_ad.resurslar'),
        ),
    ]
