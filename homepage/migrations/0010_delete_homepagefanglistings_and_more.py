# Generated by Django 5.0.2 on 2024-11-22 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomepageFanglistings',
        ),
        migrations.AlterModelOptions(
            name='listingimage',
            options={'managed': False},
        ),
    ]
