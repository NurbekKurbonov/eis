# Generated by Django 4.0.5 on 2022-11-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_ad', '0061_elon_jbvaqt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elon',
            name='masala',
            field=models.TextField(blank=True, null=True, verbose_name='masala'),
        ),
    ]
