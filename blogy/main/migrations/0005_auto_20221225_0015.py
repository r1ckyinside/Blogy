# Generated by Django 3.1.1 on 2022-12-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20221224_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(null=True, upload_to='files/', verbose_name='Pics'),
        ),
    ]