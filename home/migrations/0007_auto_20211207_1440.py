# Generated by Django 3.2.9 on 2021-12-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_category_blog_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='blogs',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='home.Tag'),
        ),
    ]
