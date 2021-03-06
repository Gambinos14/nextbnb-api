# Generated by Django 3.0 on 2020-06-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200625_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
    ]
