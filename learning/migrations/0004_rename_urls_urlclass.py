# Generated by Django 4.0.1 on 2023-09-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_urls_url_link'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='urls',
            new_name='urlClass',
        ),
    ]
