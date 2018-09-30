# Generated by Django 2.0 on 2018-09-30 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('piu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piu',
            old_name='cargo',
            new_name='conteudo',
        ),
        migrations.RenameField(
            model_name='piu',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AddField(
            model_name='piu',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Data'),
        ),
    ]
