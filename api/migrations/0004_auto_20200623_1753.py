# Generated by Django 3.0 on 2020-06-23 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_house_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='api.House'),
        ),
    ]
