# Generated by Django 4.0.1 on 2022-01-26 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_ad', '0034_alter_resurslar_gj_alter_resurslar_gkal'),
        ('foydalanuvchi', '0061_alter_hisobot_full_vaqt_alter_hisobot_ich_vaqt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hisobot_full',
            name='valyuta',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='s_ad.valyuta', verbose_name='valyuta'),
            preserve_default=False,
        ),
    ]
