# Generated by Django 3.2.6 on 2021-08-26 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210826_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='not-found.jpg', upload_to='images/products')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.productcategory')),
            ],
        ),
    ]
