# Generated by Django 3.1.5 on 2021-02-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society_reg', '0008_auto_20210222_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='phone',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=200, null=True),
        ),
    ]