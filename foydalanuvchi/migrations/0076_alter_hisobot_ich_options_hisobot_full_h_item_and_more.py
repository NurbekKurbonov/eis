# Generated by Django 4.0.1 on 2022-02-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foydalanuvchi', '0075_remove_hisobot_full_hisobotlar_hisobot_full_ich_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hisobot_ich',
            options={'ordering': ('vaqt',), 'verbose_name_plural': '02_1_Ishlab chiqarish hisoboti'},
        ),
        migrations.AddField(
            model_name='hisobot_full',
            name='h_item',
            field=models.ManyToManyField(to='foydalanuvchi.hisobot_item', verbose_name='Umumiy hisobot'),
        ),
        migrations.AlterField(
            model_name='hisobot_ich',
            name='qiymat_pul',
            field=models.FloatField(verbose_name='Resurs qiymati so`mda'),
        ),
        migrations.AlterField(
            model_name='hisobot_ist',
            name='qiymat_pul',
            field=models.FloatField(verbose_name='Resurs qiymati so`mda'),
        ),
        migrations.AlterField(
            model_name='hisobot_uzat',
            name='qiymat_pul',
            field=models.FloatField(verbose_name='Resurs qiymati so`mda'),
        ),
    ]
