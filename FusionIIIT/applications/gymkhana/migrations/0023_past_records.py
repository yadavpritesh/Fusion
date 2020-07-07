# Generated by Django 3.0.7 on 2020-07-07 03:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0005_auto_20200522_1851'),
        ('gymkhana', '0022_auto_20200704_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Past_records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(default=datetime.date.today)),
                ('club_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_held', to='gymkhana.Club_info')),
                ('past_co', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastco', to='academic_information.Student')),
                ('past_coco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pastcoco', to='academic_information.Student')),
            ],
        ),
    ]
