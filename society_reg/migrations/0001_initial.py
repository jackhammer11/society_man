# Generated by Django 3.1.5 on 2021-02-22 10:43

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Vistor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, null=True)),
                ('vehicle', models.CharField(choices=[('None', 'No vehicle'), ('Bike', 'Bike'), ('Car', 'Car')], max_length=200, null=True)),
                ('in_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('society', models.CharField(max_length=200, null=True)),
                ('purpose', models.CharField(max_length=200, null=True)),
                ('out_time', models.DateTimeField(null=True)),
            ],
        ),
    ]
