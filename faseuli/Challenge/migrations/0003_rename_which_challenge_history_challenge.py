# Generated by Django 3.2.3 on 2021-09-25 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Challenge', '0002_auto_20210925_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='which_challenge',
            new_name='Challenge',
        ),
    ]
