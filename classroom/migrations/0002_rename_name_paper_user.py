# Generated by Django 3.2.9 on 2023-04-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='name',
            new_name='user',
        ),
    ]