# Generated by Django 4.0.7 on 2022-09-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0037_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.CharField(blank=True, default='2b7', max_length=3, null=True),
        ),
    ]
