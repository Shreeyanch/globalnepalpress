# Generated by Django 3.2.4 on 2021-08-10 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='details',
            field=models.CharField(default='some_value', max_length=50),
        ),
    ]
