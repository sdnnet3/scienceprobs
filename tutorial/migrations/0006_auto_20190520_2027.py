# Generated by Django 2.1.4 on 2019-05-21 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_topic_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='content_2',
            new_name='mnemonic',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='image_2',
            new_name='mnemonic_image',
        ),
    ]
