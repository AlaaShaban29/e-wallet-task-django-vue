# Generated by Django 4.0.7 on 2022-09-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0047_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.CharField(blank=True, default='bff', max_length=3, null=True),
        ),
    ]
