# Generated by Django 3.0.3 on 2020-08-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
