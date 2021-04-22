# Generated by Django 3.1.7 on 2021-04-22 01:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=50)),
                ('music_brand', models.CharField(max_length=50)),
                ('music_price', models.IntegerField(default=0)),
                ('music_buy', models.DateTimeField(default=django.utils.timezone.now)),
                ('music_producer', models.CharField(max_length=50)),
                ('music_quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
