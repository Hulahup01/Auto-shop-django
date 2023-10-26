# Generated by Django 4.2.5 on 2023-09-28 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Content news')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time')),
                ('image', models.ImageField(null=True, upload_to='news/images/', verbose_name='News image')),
            ],
        ),
    ]
