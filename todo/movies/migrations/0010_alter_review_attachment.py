# Generated by Django 3.2.9 on 2021-11-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='movie/attachment/review'),
        ),
    ]
