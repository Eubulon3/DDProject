# Generated by Django 4.2.7 on 2023-11-20 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddapp.record', verbose_name='タグ')),
            ],
        ),
    ]
