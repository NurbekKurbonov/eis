# Generated by Django 4.0.5 on 2022-11-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_ad', '0060_alter_elon_masala'),
    ]

    operations = [
        migrations.AddField(
            model_name='elon',
            name='jbvaqt',
            field=models.DateTimeField(default=1, verbose_name='Javob vaqti'),
            preserve_default=False,
        ),
    ]
