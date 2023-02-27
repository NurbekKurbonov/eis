# Generated by Django 4.0.5 on 2023-02-25 20:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s_ad', '0066_remove_elon_masala_elon_birlik_elon_hajm_elon_maqsad_and_more'),
        ('foydalanuvchi', '0133_hisobot_full_qanday'),
    ]

    operations = [
        migrations.CreateModel(
            name='hisobot_samaradorlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50, verbose_name='Hisobot nomi')),
                ('vaqt', models.DateTimeField(verbose_name='Vaqti')),
                ('oraliq_min', models.CharField(max_length=50, verbose_name='Maksimal oraliq')),
                ('oraliq_max', models.CharField(max_length=50, verbose_name='Minimal oraliq')),
                ('qanday', models.TextField(blank=True, verbose_name='Qanday turdagi')),
                ('tur', models.CharField(blank=True, max_length=255, verbose_name='Hisobot turi')),
                ('h_item', models.ManyToManyField(to='foydalanuvchi.hisobot_item', verbose_name='Umumiy hisobot')),
                ('ich', models.ManyToManyField(to='foydalanuvchi.hisobot_ich', verbose_name='Ishlab chiqarish hisobotlari')),
                ('ist', models.ManyToManyField(to='foydalanuvchi.hisobot_ist', verbose_name="Iste'mol hisobotlari")),
                ('koef', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.yaxlitlash', verbose_name='Koeffitsient')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Egasi')),
                ('resurs', models.ManyToManyField(to='s_ad.resurslar', verbose_name='Resurslar')),
                ('sot', models.ManyToManyField(to='foydalanuvchi.hisobot_uzat', verbose_name='Sotish hisobotlari')),
            ],
            options={
                'verbose_name': 'hisobot_samaradorlik',
                'verbose_name_plural': '04_0_hisobot_samaradorlik',
            },
        ),
    ]
