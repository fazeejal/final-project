# Generated by Django 5.0.2 on 2024-03-19 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookhiveapp', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]