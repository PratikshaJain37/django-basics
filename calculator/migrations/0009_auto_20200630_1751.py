# Generated by Django 3.0.7 on 2020-06-30 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0008_auto_20200630_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calculation',
            old_name='operator_text',
            new_name='operator',
        ),
    ]
