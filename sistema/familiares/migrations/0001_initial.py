# Generated by Django 4.0.6 on 2022-07-30 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
