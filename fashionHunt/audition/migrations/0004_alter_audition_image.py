# Generated by Django 4.0.5 on 2023-08-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audition', '0003_alter_audition_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audition',
            name='image',
            field=models.FileField(upload_to='media/Audition/'),
        ),
    ]
