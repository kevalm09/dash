# Generated by Django 4.0.3 on 2023-06-06 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sale',
            new_name='Sales',
        ),
    ]
