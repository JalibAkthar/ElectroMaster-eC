# Generated by Django 4.2.4 on 2023-10-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ElectroMasterUserSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Pass_Word', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Address', models.EmailField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
