# Generated by Django 2.1.4 on 2019-05-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content_3',
            field=models.TextField(blank=True),
        ),
    ]
