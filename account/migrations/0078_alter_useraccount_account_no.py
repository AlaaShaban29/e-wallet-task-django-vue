# Generated by Django 4.0.7 on 2022-09-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0077_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.CharField(default='667', max_length=3),
        ),
    ]
