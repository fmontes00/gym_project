# Generated by Django 4.0.5 on 2022-07-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_routine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='day',
            field=models.DateField(choices=[('lunes', 'martes')]),
        ),
    ]
