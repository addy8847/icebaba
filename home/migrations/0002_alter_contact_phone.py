# Generated by Django 3.2.9 on 2021-12-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(max_length=13),
        ),
    ]
