# Generated by Django 3.1.5 on 2021-01-26 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210108_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]
