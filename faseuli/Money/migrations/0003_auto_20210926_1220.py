# Generated by Django 3.2.3 on 2021-09-26 03:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Money', '0002_auto_20210925_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
