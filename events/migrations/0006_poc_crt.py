# Generated by Django 4.2 on 2023-04-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_acc_crt_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='poc_crt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('registerd', models.CharField(max_length=7)),
                ('date', models.TextField()),
            ],
        ),
    ]
