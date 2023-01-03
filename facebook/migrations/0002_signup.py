# Generated by Django 4.1.2 on 2022-11-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=200, null=True, unique=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('mobile', models.BigIntegerField(verbose_name='')),
                ('gender', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]