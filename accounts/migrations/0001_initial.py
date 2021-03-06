# Generated by Django 2.0.5 on 2018-05-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('username1', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=2000)),
                ('date_of_creation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email_id', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=512)),
            ],
        ),
    ]
