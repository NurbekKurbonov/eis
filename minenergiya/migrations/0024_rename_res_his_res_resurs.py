# Generated by Django 4.0.5 on 2022-10-24 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minenergiya', '0023_alter_ensamfiltr_e_id_alter_filtr_faqir_e_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='his_res',
            old_name='res',
            new_name='resurs',
        ),
    ]
