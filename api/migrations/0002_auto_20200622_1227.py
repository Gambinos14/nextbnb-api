# Generated by Django 3.0 on 2020-06-22 16:27

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=5000)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amenities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), blank=True, default=list, null=True, size=None)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=3000)),
                ('house_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.House')),
            ],
        ),
        migrations.DeleteModel(
            name='Mango',
        ),
        migrations.AddField(
            model_name='booking',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.House'),
        ),
    ]