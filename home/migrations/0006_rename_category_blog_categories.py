# Generated by Django 3.2.9 on 2021-12-07 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_blog_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='categories',
        ),
    ]
