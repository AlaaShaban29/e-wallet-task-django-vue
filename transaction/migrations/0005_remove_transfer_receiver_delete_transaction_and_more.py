# Generated by Django 4.0.7 on 2022-09-02 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_alter_transfer_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='receiver',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transfer',
        ),
    ]
