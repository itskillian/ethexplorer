# Generated by Django 5.0.6 on 2024-07-10 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_txns_transaction_hash'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Txns',
            new_name='Txn',
        ),
    ]
