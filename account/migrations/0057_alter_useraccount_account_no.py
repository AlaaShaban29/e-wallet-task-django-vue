# Generated by Django 4.0.7 on 2022-09-02 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0056_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.CharField(default=uuid.uuid4, max_length=3),
        ),
    ]
