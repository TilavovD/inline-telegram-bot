# Generated by Django 4.0.6 on 2022-07-22 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True, max_length=128, null=True),
        ),
    ]