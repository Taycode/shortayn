# Generated by Django 2.0.6 on 2019-04-06 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190406_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_code',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
