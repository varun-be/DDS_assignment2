# Generated by Django 3.1 on 2020-09-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0002_battle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ship_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('class_type', models.CharField(max_length=100)),
                ('class_country', models.CharField(max_length=100)),
                ('num_guns', models.CharField(max_length=100)),
                ('bore', models.CharField(max_length=100)),
                ('displacement', models.CharField(max_length=100)),
            ],
        ),
    ]
