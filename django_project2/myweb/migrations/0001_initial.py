# Generated by Django 4.2.3 on 2023-07-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('itemname', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('pictureurl', models.CharField(max_length=50)),
            ],
        ),
    ]
