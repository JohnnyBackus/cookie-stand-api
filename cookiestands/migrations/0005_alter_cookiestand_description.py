# Generated by Django 4.1.5 on 2024-03-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookiestands', '0004_alter_cookiestand_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookiestand',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
