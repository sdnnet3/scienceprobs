# Generated by Django 2.1.4 on 2019-04-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='highlight',
            field=models.BooleanField(default=True),
        ),
    ]