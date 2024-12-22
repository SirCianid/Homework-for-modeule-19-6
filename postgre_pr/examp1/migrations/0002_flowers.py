# Generated by Django 4.2.17 on 2024-12-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flowers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('height', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
