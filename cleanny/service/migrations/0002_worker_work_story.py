# Generated by Django 4.2.11 on 2024-04-05 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='work_story',
            field=models.TextField(blank=True, help_text='Введите историю о заказе', verbose_name='История о заказе'),
        ),
    ]
