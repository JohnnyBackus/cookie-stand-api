# Generated by Django 4.1.5 on 2024-03-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiestands', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookiestand',
            old_name='location',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='cookiestand',
            old_name='owner',
            new_name='reviewer',
        ),
        migrations.RemoveField(
            model_name='cookiestand',
            name='average_cookies_per_sale',
        ),
        migrations.RemoveField(
            model_name='cookiestand',
            name='hourly_sales',
        ),
        migrations.RemoveField(
            model_name='cookiestand',
            name='maximum_customers_per_hour',
        ),
        migrations.RemoveField(
            model_name='cookiestand',
            name='minimum_customers_per_hour',
        ),
        migrations.AddField(
            model_name='cookiestand',
            name='rating',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='cookiestand',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
