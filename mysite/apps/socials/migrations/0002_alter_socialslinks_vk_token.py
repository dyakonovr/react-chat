# Generated by Django 4.1.5 on 2023-03-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialslinks',
            name='vk_token',
            field=models.CharField(max_length=500, null=True, unique=True),
        ),
    ]