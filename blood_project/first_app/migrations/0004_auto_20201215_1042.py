# Generated by Django 3.1.4 on 2020-12-15 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20201214_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='name',
            old_name='date',
            new_name='lastdonateddate',
        ),
    ]
