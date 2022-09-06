# Generated by Django 4.0.7 on 2022-09-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='receiver_account_no',
            field=models.CharField(default='001', max_length=3),
        ),
        migrations.AddField(
            model_name='transfer',
            name='sender_account_no',
            field=models.CharField(default='000', max_length=3),
        ),
    ]
