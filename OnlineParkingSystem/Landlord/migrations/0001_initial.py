# Generated by Django 2.1.7 on 2020-01-03 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land_detail',
            fields=[
                ('landid', models.AutoField(primary_key=True, serialize=False)),
                ('lattitude', models.FloatField(max_length=25)),
                ('langitude', models.FloatField(max_length=25)),
                ('address', models.CharField(max_length=255)),
                ('images', models.TextField(null=True)),
                ('city', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('no_of_spot', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('availability', models.IntegerField()),
                ('price_per_hour', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('verified', models.BooleanField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.User_detail')),
            ],
        ),
    ]
