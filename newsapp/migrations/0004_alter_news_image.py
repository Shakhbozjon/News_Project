# Generated by Django 4.2.3 on 2023-07-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/images/'),
        ),
    ]