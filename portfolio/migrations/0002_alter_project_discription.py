# Generated by Django 4.2.5 on 2023-09-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='discription',
            field=models.CharField(max_length=1000),
        ),
    ]
