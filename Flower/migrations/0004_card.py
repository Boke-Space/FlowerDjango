# Generated by Django 4.0.5 on 2022-06-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flower', '0003_data_is_delete_recognition_is_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(max_length=0)),
                ('uid', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=False)),
            ],
        ),
    ]