# Generated by Django 4.1.4 on 2023-01-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Landing_Page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading1', models.CharField(max_length=200)),
                ('heading2', models.CharField(max_length=200)),
                ('description1', models.TextField(max_length=1000)),
                ('heading3', models.CharField(max_length=200)),
                ('description2', models.TextField(max_length=1000)),
            ],
        ),
    ]
