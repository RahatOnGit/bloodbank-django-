# Generated by Django 5.0.6 on 2024-07-10 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodGroupsApp', '0002_rename_house_details_donor_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='district',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='house_details',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='upazila',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(max_length=270),
        ),
    ]
