# Generated by Django 5.1 on 2024-09-01 08:38

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyUser',
            fields=[
            ],
            options={
                'ordering': ('username',),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
