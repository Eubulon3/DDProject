# Generated by Django 4.2.7 on 2023-11-18 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ddapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='contet',
            new_name='content',
        ),
    ]