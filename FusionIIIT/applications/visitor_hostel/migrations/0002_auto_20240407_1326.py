# Generated by Django 3.1.5 on 2024-04-07 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_hostel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealrecord',
            name='room',
        ),
        migrations.AddField(
            model_name='bill',
            name='bill_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mealrecord',
            name='breakfast',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mealrecord',
            name='dinner',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mealrecord',
            name='eve_tea',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mealrecord',
            name='lunch',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mealrecord',
            name='morning_tea',
            field=models.IntegerField(default=0),
        ),
    ]