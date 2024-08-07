# Generated by Django 5.0.6 on 2024-07-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, db_collation='utf8_persian_ci', verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_collation='utf8_persian_ci', max_length=100),
        ),
    ]
