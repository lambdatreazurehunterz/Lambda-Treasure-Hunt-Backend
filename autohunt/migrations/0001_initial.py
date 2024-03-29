# Generated by Django 2.2.3 on 2019-07-29 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('coordX', models.IntegerField()),
                ('coordY', models.IntegerField()),
                ('exitN', models.IntegerField()),
                ('exitE', models.IntegerField()),
                ('exitS', models.IntegerField()),
                ('exitW', models.IntegerField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
