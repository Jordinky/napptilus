# Generated by Django 4.2.3 on 2023-12-05 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_tee_cap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('quantity', models.IntegerField(default=0, max_length=2)),
                ('price', models.FloatField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.cart')),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shopping_cart.product')),
            ],
        ),
    ]
