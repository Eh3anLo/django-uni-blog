# Generated by Django 5.0.6 on 2024-07-09 16:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_article_date_created_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('منتشر شده', 'منتشر شده'), ('پیش نویس', 'پیش نویس')], max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_collation='utf8_persian_ci', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]