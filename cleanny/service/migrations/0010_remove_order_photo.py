# Generated by Django 4.2.11 on 2024-04-09 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_remove_order_client_order_email_order_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='photo',
        ),
    ]
