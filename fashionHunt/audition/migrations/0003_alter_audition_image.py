# Generated by Django 4.0.5 on 2023-08-05 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0002_alter_audition_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='image',
            field=models.FileField(upload_to='mymedia2/'),
        ),
    ]
