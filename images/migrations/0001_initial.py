# Generated by Django 4.1.5 on 2023-01-09 19:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='%Y/%m/%d/', verbose_name='Изображение')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Локация')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='images.image', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Человек',
                'verbose_name_plural': 'Люди',
            },
        ),
    ]
