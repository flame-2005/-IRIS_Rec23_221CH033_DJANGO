# Generated by Django 4.2 on 2023-04-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_poc_crt'),
    ]

    operations = [
        migrations.AddField(
            model_name='poc_crt',
            name='company',
            field=models.CharField(default='oracle', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poc_crt',
            name='subdate',
            field=models.CharField(default='1/1/23', max_length=12),
            preserve_default=False,
        ),
    ]
