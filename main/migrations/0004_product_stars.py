# Generated by Django 3.2.6 on 2021-09-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stars',
            field=models.IntegerField(default=0),
        ),
    ]
