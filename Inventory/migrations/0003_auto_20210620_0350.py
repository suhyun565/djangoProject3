# Generated by Django 3.1.7 on 2021-06-19 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speedracer', '0001_initial'),
        ('Inventory', '0002_auto_20210620_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='price',
            new_name='current_amount',
        ),
        migrations.AddField(
            model_name='position',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='speedracer.order'),
        ),
    ]
