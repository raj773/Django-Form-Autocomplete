# Generated by Django 3.1.5 on 2021-01-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='pub_date',
        ),
    ]
