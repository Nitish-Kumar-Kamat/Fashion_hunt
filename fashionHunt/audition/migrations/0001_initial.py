# Generated by Django 4.0.5 on 2023-08-05 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('place', models.CharField(max_length=250)),
                ('date', models.DateField(max_length=30)),
                ('image', models.FileField(upload_to='mymedia2')),
            ],
        ),
    ]