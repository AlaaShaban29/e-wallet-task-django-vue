# Generated by Django 4.0.7 on 2022-09-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.CharField(blank=True, default='c4b', max_length=3, null=True),
        ),
    ]
