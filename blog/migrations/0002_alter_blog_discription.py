# Generated by Django 4.2.5 on 2023-09-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='discription',
            field=models.TextField(max_length=500),
        ),
    ]
