# Generated by Django 4.0.7 on 2022-09-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0055_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.CharField(max_length=3),
        ),
    ]
