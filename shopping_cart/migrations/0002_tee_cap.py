# Generated by Django 4.2.3 on 2023-12-04 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfFabric', models.CharField(max_length=200)),
                ('sizing', models.CharField(max_length=200)),
                ('sleeves', models.CharField(max_length=200)),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logoColor', models.CharField(max_length=200)),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.product')),
            ],
        ),
    ]
