# Generated by Django 2.1.4 on 2019-05-20 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_auto_20190519_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content_1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content_2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='content_3',
            field=models.TextField(null=True),
        ),
    ]
