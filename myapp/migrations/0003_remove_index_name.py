# Generated by Django 3.1.5 on 2021-01-07 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_index_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='name',
        ),
    ]
