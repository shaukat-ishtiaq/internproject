# Generated by Django 4.1 on 2022-08-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_image_watermarked_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='original_url',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
