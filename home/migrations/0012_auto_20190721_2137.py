# Generated by Django 2.2.2 on 2019-07-21 19:37

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_thesign_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komiteer',
            name='post_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
    ]
