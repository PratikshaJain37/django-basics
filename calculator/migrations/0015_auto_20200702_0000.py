# Generated by Django 3.0.7 on 2020-07-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0014_auto_20200701_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculation',
            name='operator',
            field=models.CharField(choices=[('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide'), ('!', 'Find Factorial'), ('%', 'Find percentage'), ('**', 'Find exponent'), ('//', 'Find quotient and remainder')], default='+', max_length=2),
        ),
    ]
