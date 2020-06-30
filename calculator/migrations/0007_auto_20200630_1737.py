# Generated by Django 3.0.7 on 2020-06-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0006_calculation_asked_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='operator',
            field=models.CharField(choices=[('+', 'Add'), ('-', 'Subtract')], default='+', max_length=2),
        ),
    ]