# Generated by Django 3.1.7 on 2021-06-20 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speedracer', '0001_initial'),
        ('Inventory', '0010_auto_20210620_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='product_location',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='speedracer.order'),
        ),
    ]
