# Generated by Django 3.2 on 2021-09-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Challenge', '0002_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='now',
            field=models.PositiveIntegerField(null=True),
        ),
    ]