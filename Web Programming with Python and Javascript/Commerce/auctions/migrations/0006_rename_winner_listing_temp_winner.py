# Generated by Django 3.2.9 on 2021-12-19 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='winner',
            new_name='temp_winner',
        ),
    ]
