# Generated by Django 4.2 on 2023-04-22 12:46

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
