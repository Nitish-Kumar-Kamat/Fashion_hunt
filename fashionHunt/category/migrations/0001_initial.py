# Generated by Django 4.0.5 on 2023-08-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField()),
                ('cname', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='media/Category/')),
            ],
        ),
    ]
