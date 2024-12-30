# Generated by Django 5.1.4 on 2024-12-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_currencystats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currencystats',
            name='avg_buy',
        ),
        migrations.RemoveField(
            model_name='currencystats',
            name='avg_sell',
        ),
        migrations.AddField(
            model_name='currencystats',
            name='average_buy',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='currencystats',
            name='average_sell',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='currencystats',
            name='currency',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='currencystats',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='currencystats',
            name='total_buy',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='currencystats',
            name='total_sell',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]