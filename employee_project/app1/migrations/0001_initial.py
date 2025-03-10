# Generated by Django 5.1 on 2024-08-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=34)),
                ('email', models.EmailField(max_length=254)),
                ('registered_time', models.DateTimeField(auto_now_add=True)),
                ('registered_by', models.CharField(max_length=34)),
            ],
        ),
    ]
