# Generated by Django 4.0.7 on 2022-09-01 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_rename_user_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='account_no',
            field=models.IntegerField(default=uuid.uuid4),
        ),
    ]