# Generated by Django 3.0 on 2020-06-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200623_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='baths',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='guests',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
