# Generated by Django 4.2 on 2023-04-30 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_delete_admins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acc_crt',
            name='password',
        ),
    ]