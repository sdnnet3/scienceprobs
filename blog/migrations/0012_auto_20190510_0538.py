# Generated by Django 2.1.4 on 2019-05-10 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_clip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='content',
        ),
    ]