# Generated by Django 4.0 on 2022-04-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krishibariapp', '0021_allquestion_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseslist',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]