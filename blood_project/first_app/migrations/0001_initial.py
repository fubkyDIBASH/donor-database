# Generated by Django 3.1.4 on 2020-12-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, unique=True)),
                ('address', models.CharField(max_length=264, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneno', models.CharField(max_length=10, unique=True)),
                ('bloodgroup', models.CharField(max_length=3, unique=True)),
                ('date', models.DateField()),
            ],
        ),
    ]
