# Generated by Django 5.0.1 on 2024-05-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fuel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
