# Generated by Django 4.2.11 on 2024-04-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_worker_work_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='experience',
            field=models.IntegerField(blank=True, default=1, help_text='Введите стаж работы', verbose_name='Стаж работы'),
            preserve_default=False,
        ),
    ]
