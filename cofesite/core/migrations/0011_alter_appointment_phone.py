# Generated by Django 3.2.9 on 2021-12-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.IntegerField(),
        ),
    ]