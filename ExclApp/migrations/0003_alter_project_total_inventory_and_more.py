# Generated by Django 5.0.4 on 2024-07-23 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExclApp', '0002_remove_project_configuration_remove_project_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='total_inventory',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='unit_size',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
