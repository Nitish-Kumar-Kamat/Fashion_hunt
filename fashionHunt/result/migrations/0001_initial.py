# Generated by Django 4.0.5 on 2023-08-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.CharField(max_length=15)),
                ('cname', models.CharField(max_length=70)),
                ('type', models.CharField(max_length=50)),
                ('team', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('prize', models.CharField(max_length=50)),
            ],
        ),
    ]
