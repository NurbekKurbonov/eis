# Generated by Django 4.0.1 on 2022-01-20 06:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foydalanuvchi', '0034_delete_davrich'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hisobot_ich',
            options={'verbose_name_plural': '02_1_Ishlab chiqarish hisoboti'},
        ),
        migrations.AlterModelOptions(
            name='hisobot_ist',
            options={'verbose_name_plural': '02_2_Iste`mol hisoboti'},
        ),
        migrations.AlterModelOptions(
            name='hisobot_item',
            options={'verbose_name': 'hisobot_shakli', 'verbose_name_plural': '02_0_Hisobot shakllari'},
        ),
        migrations.AlterModelOptions(
            name='hisobot_uzat',
            options={'verbose_name_plural': '02_3_Uzatilgan resurs hisoboti'},
        ),
        migrations.AlterModelOptions(
            name='ichres',
            options={'verbose_name_plural': '01_0_Ishlab chiqarish resurslari'},
        ),
        migrations.AlterModelOptions(
            name='istres',
            options={'verbose_name_plural': '01_1_Iste`mol resurslari'},
        ),
        migrations.AlterModelOptions(
            name='sotres',
            options={'verbose_name_plural': '01_2_Uzatiladigan resurslar'},
        ),
        migrations.CreateModel(
            name='allfaqir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=250, verbose_name='Korxona nomi')),
                ('inn', models.CharField(max_length=50, verbose_name='STIR')),
                ('about', models.TextField(blank=True, verbose_name='Korxona haqida qisqacha')),
                ('emblem', models.ImageField(max_length=255, upload_to='profile_emb', verbose_name='Emblemasi')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Egasi')),
            ],
            options={
                'verbose_name': 'Foydalanuvchi',
                'verbose_name_plural': 'Foydalanuvchilar',
            },
        ),
    ]
