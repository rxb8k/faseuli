# Generated by Django 3.2.3 on 2021-09-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20210925_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
