# Generated by Django 3.2.12 on 2022-02-10 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s_ad', '0036_alter_viloyatlar_viloyat_kodi'),
        ('foydalanuvchi', '0079_auto_20220209_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allfaqir',
            name='dav',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.davlatlar', verbose_name='Davlat'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='dbibt',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.dbibt', verbose_name='DBIBT'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='emblem',
            field=models.ImageField(blank=True, max_length=255, upload_to='profile_emb', verbose_name='Emblemasi'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='iftum',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.iftum', verbose_name='IFTUM'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='inn',
            field=models.CharField(max_length=50, verbose_name='STIR'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='manzil',
            field=models.TextField(blank=True, verbose_name='Manzil'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='mobil',
            field=models.CharField(blank=True, max_length=9, verbose_name='Korxona raqami'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='savol1',
            field=models.BooleanField(blank=True, verbose_name='Ishlab chiqarish/servis'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='savol2',
            field=models.BooleanField(blank=True, verbose_name='Uzatish/sotish'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='tel',
            field=models.CharField(blank=True, max_length=9, verbose_name='Korxona raqami'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='thst',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.thst', verbose_name='DBIBT'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='tum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.tumanlar', verbose_name='Tuman'),
        ),
        migrations.AlterField(
            model_name='allfaqir',
            name='vil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='s_ad.viloyatlar', verbose_name='Viloyat'),
        ),
    ]
