# Generated by Django 4.0.5 on 2023-08-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0004_alter_audition_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='date',
            field=models.DateField(max_length=30),
        ),
    ]
