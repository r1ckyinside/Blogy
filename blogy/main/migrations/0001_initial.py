# Generated by Django 3.1.1 on 2022-12-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Content')),
                ('author', models.CharField(max_length=100, verbose_name='Author Name')),
                ('date', models.DateField(verbose_name='Publ. date')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
