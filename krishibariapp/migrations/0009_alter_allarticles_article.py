# Generated by Django 4.0 on 2022-03-02 08:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krishibariapp', '0008_alter_articlecomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allarticles',
            name='article',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]