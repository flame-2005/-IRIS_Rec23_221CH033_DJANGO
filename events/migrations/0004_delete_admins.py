# Generated by Django 4.2 on 2023-04-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_admins_email_remove_admins_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admins',
        ),
    ]
