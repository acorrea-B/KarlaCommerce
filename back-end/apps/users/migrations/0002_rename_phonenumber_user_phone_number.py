# Generated by Django 3.2.5 on 2021-07-29 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phoneNumber',
            new_name='phone_number',
        ),
    ]
