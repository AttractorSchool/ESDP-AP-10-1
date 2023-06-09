# Generated by Django 4.2.2 on 2023-07-05 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='review',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]
