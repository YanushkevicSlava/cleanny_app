# Generated by Django 4.2.11 on 2024-04-08 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_alter_client_photo_alter_worker_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='comments',
            field=models.TextField(blank=True, help_text='Введите отзыв о заказе', verbose_name='Отзыв о заказе'),
        ),
    ]
