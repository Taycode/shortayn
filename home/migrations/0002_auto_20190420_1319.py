# Generated by Django 2.0.6 on 2019-04-20 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='time_created',
            field=models.DateTimeField(auto_created=True),
        ),
    ]