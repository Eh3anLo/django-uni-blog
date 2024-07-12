# Generated by Django 5.0.6 on 2024-07-12 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_github_url_userprofile_linkedin_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='درباره من'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='github_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name=' گیت هاب'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin_url',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name=' لینکدین'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='major',
            field=models.CharField(blank=True, choices=[('کاردانی', 'کاردانی نرم افزار'), ('کارشناسی', 'کارشناسی نرم افزار'), ('شبکه', 'شبکه و سخت و افزار')], max_length=200, verbose_name='رشته تحصیلی'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, max_length=200, verbose_name='سمت شغلی'),
        ),
    ]
