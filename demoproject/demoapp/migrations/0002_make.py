# Generated by Django 4.2.3 on 2023-08-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name1', models.CharField(max_length=250)),
                ('Image1', models.ImageField(upload_to='pics')),
                ('details', models.TextField()),
            ],
        ),
    ]