# Generated by Django 2.2 on 2019-04-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
