# Generated by Django 3.0.1 on 2019-12-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('text', models.TextField()),
            ],
        ),
    ]
