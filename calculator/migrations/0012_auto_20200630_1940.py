# Generated by Django 3.0.7 on 2020-06-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0011_auto_20200630_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='operator',
            field=models.CharField(choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')], default='+', max_length=2),
        ),
    ]
