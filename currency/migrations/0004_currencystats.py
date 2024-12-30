# Generated by Django 5.1.4 on 2024-12-23 15:52

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_operationhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('total_buy', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('total_sell', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('avg_buy', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('avg_sell', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
                ('profit', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15)),
            ],
        ),
    ]