# Generated by Django 3.0.3 on 2020-02-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.CharField(default='aa', max_length=10, primary_key=True, serialize=False)),
                ('a1', models.IntegerField(default=0)),
                ('a2', models.IntegerField(default=0)),
                ('a3', models.IntegerField(default=0)),
                ('a4', models.IntegerField(default=0)),
                ('a5', models.IntegerField(default=0)),
                ('a6', models.IntegerField(default=0)),
                ('a7', models.IntegerField(default=0)),
                ('a8', models.IntegerField(default=0)),
                ('a9', models.IntegerField(default=0)),
                ('a10', models.IntegerField(default=0)),
            ],
        ),
    ]
