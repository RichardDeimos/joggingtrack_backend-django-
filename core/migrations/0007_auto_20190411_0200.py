# Generated by Django 2.2 on 2019-04-11 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190410_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='userid',
            new_name='user_id',
        ),
    ]