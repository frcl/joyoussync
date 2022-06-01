# Generated by Django 3.2.13 on 2022-05-26 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('joyous', '0014_auto_20190328_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=511)),
                ('active', models.BooleanField(default=True)),
                ('target_calendar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joyous.calendarpage')),
            ],
        ),
    ]
