# Generated by Django 2.2.28 on 2023-02-07 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_user_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='users_country_number',
        ),
    ]