# Generated by Django 4.2.5 on 2025-04-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_code',
            field=models.CharField(default='default_code', max_length=20, unique=True, verbose_name='Код на поръчката'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'В очакване'), ('completed', 'Завършена')], default='pending', max_length=20, verbose_name='Статус на поръчката'),
        ),
    ]
