# Generated by Django 4.2.7 on 2023-11-21 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ddapp', '0004_remove_tag_tag_tag_tag_01_tag_tag_02_tag_tag_03_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='ddapp.record', verbose_name='レコード'),
        ),
    ]
