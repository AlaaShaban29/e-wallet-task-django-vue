# Generated by Django 4.0.7 on 2022-09-02 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0005_remove_transfer_receiver_delete_transaction_and_more'),
        ('account', '0063_remove_useraccount_id_alter_useraccount_account_no'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]