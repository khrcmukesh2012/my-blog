# Generated by Django 3.0.5 on 2020-04-13 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmspages',
            name='upload',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
