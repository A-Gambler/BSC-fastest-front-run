# Generated by Django 3.1.5 on 2021-03-26 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WapsClient', '0012_auto_20210316_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='bwaps_balance',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
