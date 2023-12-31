# Generated by Django 4.0.5 on 2023-08-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='mymedia1/')),
            ],
        ),
    ]
